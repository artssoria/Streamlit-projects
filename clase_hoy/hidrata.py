import streamlit as st
from datetime import datetime

st.title("💧 Control de Hidratación Diaria")

if 'vasos' not in st.session_state:
    st.session_state.vasos = 0

st.subheader(f"Vasos bebidos: {st.session_state.vasos}")

if st.button("➕ Añadir 1 vaso (250ml)"):
    st.session_state.vasos += 1
    st.rerun()

META = 8
porcentaje = min(100, (st.session_state.vasos / META) * 100)
st.progress(porcentaje / 100)
st.write(f"**Progreso:** {st.session_state.vasos}/{META} vasos")

if st.session_state.vasos >= META:
    st.balloons()
    st.success("🎉 ¡Meta cumplida! ¡Bien hecho!")