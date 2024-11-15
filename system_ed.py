import streamlit as st
import os

st.title("Aplicación de Mostrar Información del Sistema")

st.write(f"Nombre de usuario: {os.getlogin()}")
st.write(f"Sistema operativo: {os.name}")
st.write(f"Directorio actual: {os.getcwd()}")