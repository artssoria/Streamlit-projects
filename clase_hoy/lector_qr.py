import streamlit as st
from PIL import Image
import io
import pyzbar.pyzbar as pyzbar

st.title("🔍 Lector de Códigos QR")

uploaded_file = st.file_uploader("Sube una imagen con un QR", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_container_width=True)

    # Convertir a bytes
    img_bytes = io.BytesIO(uploaded_file.getvalue())
    img_pil = Image.open(img_bytes)

    # Detectar QR
    decoded_objects = pyzbar.decode(img_pil)

    if decoded_objects:
        for obj in decoded_objects:
            st.success(f"Contenido del QR: {obj.data.decode('utf-8')}")
    else:
        st.warning("No se encontró un código QR en la imagen.")