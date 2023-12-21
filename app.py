import streamlit as st
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet_v2 import preprocess_input

# Load the trained model
model = load_model('model/ResNet50V2_model.h5')

# Define the class names in the order as per the training generator
class_names = ['glioma_tumor', 'meningioma_tumor', 'normal', 'pituitary_tumor']

# Function to preprocess the image
def preprocess_image(image, target_size=(224, 224)):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = np.array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

# Streamlit app layout
st.title('MRI Brain Tumor Classification')
st.write("Upload an MRI image to classify it as normal, pituitary, meningioma, or glioma.")

# File uploader
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI Image', use_column_width=True)
    
    # Preprocess the image and predict
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)

    # Display the prediction
    class_index = np.argmax(predictions)
    prediction_text = f"Prediction: {class_names[class_index]}"

    # Display the prediction in a larger font and inside a box
    st.markdown(
        f"<div style='padding: 10px; border-radius: 5px; border: 2px solid #4CAF50; font-size: 20px; text-align: center;'>"
        f"{prediction_text}"
        f"</div>", 
        unsafe_allow_html=True
    )