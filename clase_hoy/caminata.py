import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title("🚀 Seguimiento de Caminata Diaria")
st.subheader("Registra tus pasos y ve cuánto has caminado hoy")

# Configuración inicial
if 'pasos_hoy' not in st.session_state:
    st.session_state.pasos_hoy = 0
if 'historial' not in st.session_state:
    st.session_state.historial = []

# Input para ingresar pasos
pasos = st.number_input("¿Cuántos pasos caminaste ahora?", min_value=0, step=100, value=1000)

# Botón para registrar
if st.button("✅ Registrar pasos"):
    st.session_state.pasos_hoy += pasos
    # Guardar en historial
    st.session_state.historial.append({
        "Hora": datetime.now().strftime("%H:%M"),
        "Pasos": pasos,
        "Total Acumulado": st.session_state.pasos_hoy
    })
    st.success(f"¡Registrados {pasos} pasos! Total: {st.session_state.pasos_hoy:,} pasos")

# Mostrar progreso
META_DIARIA = 8000  # pasos objetivo
porcentaje = min(100, (st.session_state.pasos_hoy / META_DIARIA) * 100)
st.progress(porcentaje / 100)
st.write(f"**Avance:** {st.session_state.pasos_hoy:,} pasos / {META_DIARIA:,} ({'✔️' if st.session_state.pasos_hoy >= META_DIARIA else '💪'} {int(porcentaje)}%)")

# Mostrar historial
if st.session_state.historial:
    st.subheader("📅 Historial de hoy")
    df_historial = pd.DataFrame(st.session_state.historial)
    st.dataframe(df_historial, use_container_width=True)

# Convertir pasos a distancia (1 paso ≈ 0.75 m)
distancia_km = (st.session_state.pasos_hoy * 0.75) / 1000
st.metric("📍 Distancia recorrida", f"{distancia_km:.1f} km")

# Botón para reiniciar
if st.button("🔄 Reiniciar día"):
    st.session_state.pasos_hoy = 0
    st.session_state.historial = []
    st.rerun()

# Pie de página
st.markdown("---")
st.caption("App educativa | Ideal para aprender Streamlit y lógica de estado")