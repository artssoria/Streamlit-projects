import streamlit as st
import requests

st.title("Conversor de Moneda")

# Lista de monedas disponibles
monedas = ["USD", "EUR", "MXN", "ARS", "COP"]

# Widgets de entrada
cantidad = st.number_input("Ingrese la cantidad:", min_value=0.0)
moneda_origen = st.selectbox("Moneda de origen:", monedas)
moneda_destino = st.selectbox("Moneda de destino:", monedas)

# Botón para realizar la conversión
if st.button("Convertir"):
    try:
        # Llamada a la API de conversión
        url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
        response = requests.get(url)
        data = response.json()
        
        # Obtener la tasa de conversión
        tasa = data["rates"][moneda_destino]
        
        # Calcular la cantidad convertida
        cantidad_convertida = cantidad * tasa
        
        # Mostrar el resultado
        st.metric(f"{cantidad} {moneda_origen} equivale a:", f"{cantidad_convertida:.2f} {moneda_destino}")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")