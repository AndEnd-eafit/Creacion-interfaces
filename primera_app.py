import streamlit as st
from PIL import Image

st.title(" Primer ejercicio")

st.header("en este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('Volvi.png')

st.image(image, caption='Mini Yoru')

texto = st.text_input('Venga, escribe algo, lo que se te de la gana', 'Observe')
st.write('EL texto escrito es', texto)

st.subheader("Ahora usemos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Yesssssssss')
