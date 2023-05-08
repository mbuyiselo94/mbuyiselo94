import streamlit as st
from PIL import Image

st.title("About Us")

st.write("Alltech Inc. is an International company with headquarters in Nigeria and branches in South Africa,Kenya and Uk.")
st.write("Our team is made of Data Scientist, Data Engineers and UI team.")
st.write("Our Services includes but not limited to Data extraction, Data Cleaning, Data Processing and Model Building in solving real world problems.")
st.write("This web application leverages the datasets to unpack key insights and trends to be used by buyers (e.g. retailers) and sellers (farmers) to set and negotiate their price on a given day. 😉")
st.write('Bringing you the best of insights')

st.header('Meet Our Team')
c1, c2, c3 = st.columns(3)
with c1:
    logo = Image.open("pics/Bukola.PNG")
    st.image(logo, width=150)
    st.write("Bukola Badeji")
    st.write("Data Engineer")
    
    logo = Image.open("pics/Praise.PNG")
    st.image(logo, width=150)
    st.write("Praise Taiwo")
    st.write("Data Engineer")
with c2:     
    logo = Image.open("pics/Chisom.PNG")
    st.image(logo, width=150)
    st.write("Chisom Nwankwo")
    st.write("Data Scientist")
    
    logo = Image.open("pics/Michael.PNG")
    st.image(logo, width=157)
    st.write("Micheal Benjamin")
    st.write("UI Specialist")
with c3:     
    logo = Image.open("pics/Simon.PNG")
    st.image(logo, width=178)
    st.write("Sello Simon")
    st.write("Data Scientist")
    
    logo = Image.open("pics/Mbusela.PNG")
    st.image(logo, width=169)
    st.write("Mbuyiselo Mkwanazi")
    st.write("UI Specialist")
            
        ##  st.image('https://www.scoopbyte.com/wp-content/uploads/2019/12/tom-and-jerry.jpg', width=300)
        ##with c2:
        #    st.image('https://github.com/Explore-AI/internship-project-2207-09/tree/main/streaamlit/pics/Chisom.PNG', width=200)
        #   st.image('https://im.indiatimes.in/media/content/itimes/blog/2014/Jul/9/1404917161_mickey+mouse.jpg', width=200)
        #   st.image('https://images6.fanpop.com/image/polls/1578000/1578435_1470083461280_full.jpg' ,width=250)
    ##st.caption('You can add images filepath using both online links (like above 👆) & from your hard disk!')    
    ################################################################################################