import streamlit as st
import datetime
import os
import subprocess

dir="./data/known"
undir="./data/unknown"
command = f"face_recognition {dir} {undir}"
log_dir ="./data/log"
log=os.path.join(log_dir,"login_log.txt")
if not os.path.exists('./data'):
    os.mkdir('./data')
if not os.path.exists(undir):
    os.mkdir(undir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

def login():
    output = str(subprocess.check_output(['face_recognition', dir, undir]))
    out_name = output.split(',')[1][:-3]
    st.write(out_name)

    if out_name=='unknown_user':
        st.sidebar.error("unknown_user")
    if out_name == 'no_persons_found':
        st.sidebar.error("no_persons_found")

    if out_name in['unknown_user', 'no_persons_found']:
        st.write("unknown user, try again")
    else:
        st.sidebar.success("Logged in successfully")
        with open(log, 'a') as f:
            f.write(f"{out_name}, {datetime.datetime.now()}")
    os.remove(name)



picture = st.camera_input("")
if picture:
    st.image(picture)
    name = os.path.join(undir, 'unknown.jpg')
    if st.button('Login'):
        with open(name, 'wb') as file:
            file.write(picture.getbuffer())
        login()

