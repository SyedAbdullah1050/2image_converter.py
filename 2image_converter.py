import streamlit as st
from PIL import Image, ImageOps

def convert_to_grayscale(image):
    return ImageOps.grayscale(image)

def convert_to_negative(image):
    return ImageOps.invert(image)

def convert_to_blur(image):
    return image.filter(ImageFilter.BLUR)

st.set_page_config(page_title="Image Converter API", page_icon=":guardsman:", layout="wide")

st.title("Image Converter API")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    conversion_options = ["Grayscale", "Negative", "Blur"]
    selected_option = st.selectbox("Select a conversion option", conversion_options)

    if selected_option == "Grayscale":
        converted_image = convert_to_grayscale(image)
    elif selected_option == "Negative":
        converted_image = convert_to_negative(image)
    elif selected_option == "Blur":
        converted_image = convert_to_blur(image)

    st.image(converted_image, caption=f"Converted Image ({selected_option})", use_column_width=True)