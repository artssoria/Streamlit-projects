import streamlit as st
from datetime import datetime

st.title("Aplicación de Mostrar Fecha y Hora")

if st.button("Actualizar"):
    ahora = datetime.now()
    st.write(f"Fecha y Hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")