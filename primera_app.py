import streamlit as st
from PIL import Image

st.title(" Primer ejercicio")

st.header("en este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('Volvi.png')

st.image(image, caption='Mini Yoru')
