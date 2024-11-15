import streamlit as st

st.title("Contador de Palabras")

texto = st.text_area("Ingrese un texto:")

if st.button("Contar Palabras"):
    if texto:
        palabras = texto.split()
        st.write(f"El texto contiene {len(palabras)} palabras.")
    else:
        st.write("Por favor, ingrese un texto.")