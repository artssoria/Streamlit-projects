import streamlit as st

st.title("Aplicación de Contador Simple")

if 'contador' not in st.session_state:
    st.session_state.contador = 0

incrementar = st.button("Incrementar")
decrementar = st.button("Decrementar")

if incrementar:
    st.session_state.contador += 1

if decrementar:
    st.session_state.contador -= 1

st.write(f"Contador: {st.session_state.contador}")