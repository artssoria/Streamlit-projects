import streamlit as st
import random
import string

st.title("Generador de Contraseñas Aleatorias")

longitud = st.number_input("Longitud de la contraseña:", min_value=4, max_value=20, value=8)

incluir_mayusculas = st.checkbox("Incluir letras mayúsculas")
incluir_minusculas = st.checkbox("Incluir letras minúsculas")
incluir_numeros = st.checkbox("Incluir números")
incluir_simbolos = st.checkbox("Incluir símbolos")

if st.button("Generar Contraseña"):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if caracteres:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        st.write(f"Contraseña generada: {contraseña}")
    else:
        st.write("Por favor, seleccione al menos un tipo de carácter.")