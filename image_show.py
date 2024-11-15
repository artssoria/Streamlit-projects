import streamlit as st

st.title("Aplicación de Mostrar Imagen")

imagenes = {
    "Gato": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg",
    "Perro": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Golden_Retriever_with_tennis_ball.jpg/1200px-Golden_Retriever_with_tennis_ball.jpg",
    "Pájaro": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Eopsaltria_australis_-_Mogo_Campground.jpg/1200px-Eopsaltria_australis_-_Mogo_Campground.jpg"
}

seleccion = st.selectbox("Seleccione una imagen:", list(imagenes.keys()))

if seleccion:
    st.image(imagenes[seleccion], caption=seleccion, use_column_width=True)