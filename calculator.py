import streamlit as st

st.title("Calculadora Simple")

num1 = st.number_input("Ingrese el primer número:", min_value=0.0)
num2 = st.number_input("Ingrese el segundo número:", min_value=0.0)

operaciones = ["Suma", "Resta", "Multiplicación", "División"]
operacion = st.selectbox("Seleccione la operación:", operaciones)

if st.button("Calcular"):
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: División por cero"
    
    st.write(f"El resultado de la {operacion.lower()} es: {resultado}")