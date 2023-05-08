import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title = 'Daily Commodity Prices', layout = 'centered', page_icon = "house")
st.write(""" # All Tech Inc
All-Tech Inc. is an international company with its headquarters in Nigeria and branches in South Africa,Kenya and the United Kingdom.

This web application leverages the datasets to unpack key insights and trends to be used by buyers (e.g
            . retailers) and sellers (farmers) to set and negotiate their price on a given day. 😉
""")
    

c1 = st.columns(1),
layout = "centered"
logo = Image.open("pics/AllTech.PNG")
st.image(logo, width=500)