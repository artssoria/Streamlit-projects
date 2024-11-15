import streamlit as st

st.title("Aplicación de Saludo Personalizado")

nombre = st.text_input("Ingrese su nombre:")

if st.button("Saludar"):
    if nombre:
        st.write(f"¡Hola, {nombre}! Bienvenido a Streamlit.")
    else:
        st.write("Por favor, ingrese su nombre.")