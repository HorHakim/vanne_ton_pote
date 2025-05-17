import streamlit as st
from PIL import Image
from backend import vanne_mon_pote


st.title("Chargeur d'image")

# Charger une image
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Lire et afficher l'image
    image = Image.open(uploaded_file)
    st.image(image, caption="Image chargée avec succès", use_container_width =True)
    
    st.write(vanne_mon_pote(image))