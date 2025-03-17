import streamlit as st
import os
from PIL import Image

# Define the directories
base_dir = "retinopathy_heatmaps"
categories = ["mild_retinopathy", "no_retinopathy"]

# Load images from directories
def load_images():
    images = {}
    for category in categories:
        folder_path = os.path.join(base_dir, category)
        if os.path.exists(folder_path):
            images[category] = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('png', 'jpg', 'jpeg'))]
    return images

images_dict = load_images()

st.set_page_config(layout="wide")
st.title("Early Retinopathy Detection Heatmap Gallery")
st.markdown("<h3 style='text-align: right; color: #f5e1a4;'>93% Validation Accuracy with MobileNetV3 on Kaggle dataset </h3>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

enlarged_image = st.empty()

st.markdown("#### Red areas received more attention from the model, indicating potential retinopathy.")
for category, images in images_dict.items():
    st.subheader(category.replace("_", " ").title())
    cols = st.columns(6)  # Increase the number of columns to use more horizontal space
    for i, image_path in enumerate(images):
        with cols[i % 6]:  # Adjusted to 6 columns for better spacing
            img = Image.open(image_path)
            img_thumb = img.copy()
            img_thumb.thumbnail((100, 100))  # Create a small thumbnail
            if st.button(image_path, key=image_path):
                enlarged_image.image(img, use_container_width=True)
            st.image(img_thumb, use_container_width=True)