import streamlit as st

st.title("Markets")

st.write("This web application leverages the datasets to unpack key insights and trends to be used by buyers (e.g. retailers) and sellers (farmers) to set and negotiate their price on a given day. 😉")

st.write('Insights from the Livestock, Horticulture, and Grain datasets')

datasets = ['Grain', 'Horticulture', 'Livestock']

provinces = ["Gauteng", "North West", "Limpopo", "Free State", "Kwa Zulu Natal", "Northern Cape", "Western Cape", "Eastern Cape", "Mpumalanga"]

cities = ["Bloemfontein", "Johannesburg", "George", "Klerksdorp"]

st.header('Market Price Insights')

dataset_selected = st.selectbox("Select Markets", options = datasets)
        
if dataset_selected == "Horticulture":
    st.write()
if dataset_selected == "Grain":
    st.write()
if dataset_selected == "Livestock":
    st.write()
   
    
dataset_selected = st.selectbox("Select Province", options = provinces)
        
if dataset_selected == "Gauteng":
    st.write()
if dataset_selected == "North West":
    st.write()
if dataset_selected == "Limpopo":
    st.write()
if dataset_selected == "Free State":
    st.write()
if dataset_selected == "Kwa Zulu Natal":
    st.write()
if dataset_selected == "Northern Cape":
    st.write()
if dataset_selected == "Western Cape":
    st.write()
if dataset_selected == "Eastern Cape":
    st.write()
if dataset_selected == "Mpumalanga":
    st.write()
    
dataset_selected = st.selectbox("Select City", options = cities)