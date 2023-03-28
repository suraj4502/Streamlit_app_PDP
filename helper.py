
import streamlit_authenticator as stauth



hashed_passwords = stauth.Hasher(['admin123', 'suraj123']).generate()



from PIL import Image
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

