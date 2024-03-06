import datetime
import streamlit as st
import os

dir="./data/known"
log_dir ="./data/log"
log=os.path.join(log_dir,"register_log.txt")
if not os.path.exists('./data'):
    os.mkdir('./data')
if not os.path.exists(dir):
    os.mkdir(dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)



def register():
    with open(name, 'wb') as file:
        file.write(picture.getbuffer())
    with open(log, 'a') as f:
        f.write(f"{input_name}, {datetime.datetime.now()}")
    if os.path.exists(name):
        st.sidebar.success('Registered Successfully!')
    else:
        st.sidebar.error('please try again')


picture = st.camera_input("")
if picture:
    st.image(picture)
    input_name = st.text_input('Enter your name')
    name = os.path.join(dir, '{}.jpg'.format(input_name))
    if st.button('Register'):
        register()


