
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Car Price Prediction </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

#sidebar
st.sidebar.title("Select Car Features")

# Machine learning model
import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))
transformer = pickle.load(open('transformer', 'rb'))

make_model_list = ['Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia',
       'Renault Clio', 'Renault Duster', 'Renault Espace']
make_model = st.sidebar.selectbox("Make and Model", make_model_list)

horse_power =st.sidebar.slider("Horse Power (kW)",40,300,150,1)

km =st.sidebar.slider("km",0,317000,10000,1)

age =st.sidebar.slider("age",0,3,2,1)

gear_list = ['Automatic', 'Manual', 'Semi-automatic']
Gearing_Type = st.sidebar.selectbox("Gearing Type", gear_list)

gears =st.sidebar.slider("Gears",5,8,6,1)

Type_list = ['Used', "Employee's car", 'New', 'Demonstration', 'Pre-registered']
Type = st.sidebar.selectbox("Type", Type_list)

package_list = ['Safety Premium Package', 'Safety Premium Plus Package',
       'Safety Standard Package']
Safety_Package = st.sidebar.selectbox("Safety Package", package_list)

my_dict = {
    "make_model": make_model,
    "hp_kW": horse_power,
    "km": km,
    "age": age,
    "Gearing_Type": Gearing_Type,
    "Gears": gears,
    "Type": Type,
    "Safety_Security_Package": Safety_Package,
}

df=pd.DataFrame.from_dict([my_dict])
st.table(df)

if st.button("Predict"):
    pred = model.predict(df)
    st.write(pred[0])
