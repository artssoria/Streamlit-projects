import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analizador de Gastos Personales")

# Inicializar historial
if 'gastos' not in st.session_state:
    st.session_state.gastos = []

# Formulario para ingresar gastos
with st.form("form_gasto"):
    descripcion = st.text_input("Descripción")
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Ocio", "Salud", "Educación"])
    monto = st.number_input("Monto", min_value=0.0, step=0.01)
    fecha = st.date_input("Fecha", value=pd.Timestamp.now().date())
    submitted = st.form_submit_button("Agregar Gasto")

if submitted:
    st.session_state.gastos.append({
        "Fecha": fecha,
        "Descripción": descripcion,
        "Categoría": categoria,
        "Monto": monto
    })
    st.success("Gasto agregado")

# Mostrar historial
if st.session_state.gastos:
    df = pd.DataFrame(st.session_state.gastos)
    st.subheader("Historial de Gastos")
    st.dataframe(df, use_container_width=True)

    # Gráfico
    st.subheader("Gasto por Categoría")
    gasto_categoria = df.groupby("Categoría")["Monto"].sum()
    fig = px.bar(gasto_categoria, labels={"value": "Monto", "index": "Categoría"})
    st.plotly_chart(fig, use_container_width=True)

    # Total
    total = df["Monto"].sum()
    st.metric("Total Gastado", f"${total:,.2f}")