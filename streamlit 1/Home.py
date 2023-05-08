import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title = 'Daily Commodity Prices', layout = 'centered', page_icon = "house")
logo = Image.open("pics/Alltech.PNG")
st.image(logo, width=500)

menu = ["Login", "SignUp"]
choice = st.selectbox("Menu", menu)

if choice == "Login":
    st.subheader("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success("Logged In As {}".format(username))
        
    
elif choice == "SignUp":
    st.subheader("Create New Account")





