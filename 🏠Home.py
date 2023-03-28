import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import requests
import json
import time
from PIL import Image
import helper as hp
from streamlit_extras.app_logo import add_logo

url = "https://us-central1-light-ratio-381415.cloudfunctions.net/predict"



st.set_page_config(page_title="A SkY product", page_icon="🌳", layout="centered")
fn = open('SKY1.PNG', 'r')

add_logo(fn)

with open('cred.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')



    

if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
    
    col1, col2 = st.columns([1,1])
    with col1:
        try:
            username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
            if username_forgot_pw:
                    st.success('New password sent securely')
            # Random password to be transferred to user securely
            elif username_forgot_pw == False:
                    st.error('Username not found')
        except Exception as e:
                st.error(e)
        with open('cred.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)   
    
    with col2:    
        try:
            username_forgot_username, email_forgot_username = authenticator.forgot_username('Forgot username')
            if username_forgot_username:
                st.success('Username sent securely')
            # Username to be transferred to user securely
            elif username_forgot_username == False:
                st.error('Email not found')
        except Exception as e:
            st.error(e)
        with open('cred.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)   
    
            
            
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
    with st.expander("Add a new user"):
        try:
            if authenticator.register_user('Register user', preauthorization=False):
                st.success('User registered successfully')
                with open('cred.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False) 
        except Exception as e:
            st.error(e)  
          
    
elif st.session_state["authentication_status"]:
    
    
    st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout('Logout', 'sidebar')
    st.title('Plant Disease Prediction Using Deep Learning 🌳🤖.')
    
    f_expand = st.expander("Uploading an image of the plant")
    
    with f_expand:
    
        image_1 = st.file_uploader("Upload the plants Image:" ,type = ['jpg', 'jpeg', 'png'])
        if image_1 is not None:
            my_bar = st.progress(0, text='uploding...')
            for percent_complete in range(100):
                time.sleep(0.001)
                my_bar.progress(percent_complete + 1, text='uploding')
        if image_1 is not None:
            try:
                response = requests.post(url, files={'file': image_1})
                if response.status_code == 200:
                    st.image(image_1)
                    json_obj = json.loads(response.content)
                    st.success(f'###### predicted Class of plant : _**{json_obj["class"]}**_')
                    st.success(f"###### with confidence : _**{json_obj['confidence']}**_")
                else:
                    st.error(f'Error processing image: *{response.text}*')
            except Exception as e:
                st.error(f'Error processing image: {e}')
                
    c_expand = st.expander("Taking an image of the plant")
    
    
    image_1 = st.camera_input(" Take a plants Image:")
    if image_1 is not None:
            try:
                response = requests.post(url, files={'file': image_1})
                if response.status_code == 200:
                    json_obj = json.loads(response.content)
                    st.success(f'###### predicted Class of plant : _**{json_obj["class"]}**_')
                    st.success(f"###### with confidence : _**{json_obj['confidence']}**_")
                else:
                    st.error(f'Error processing image: {response.text}')
            except Exception as e:
                st.error(f'Error processing image: {e}')
    
   
        
    
    
st.sidebar.markdown("\n")   
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")  
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n") 


st.sidebar.markdown("\n")   
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")  
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")  
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")   
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")  
st.sidebar.markdown("\n") 
st.sidebar.markdown("\n")  



# st.sidebar.markdown("---")
st.sidebar.markdown("- Developed by `SKY`.   ⇨[github ](https://github.com/suraj4502), [Linkedin](https://www.linkedin.com/in/surajkumar-yadav-6ab2011a4/), [Ig](https://www.instagram.com/suraj452/).")
# st.sidebar.markdown("---")
    
    
