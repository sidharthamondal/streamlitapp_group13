import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import ntpath

# Get the full path to the model file
# model_path = 'c:\\Users\\SIDHARTH\\Documents\\maths_mini_project\\animal_classification_model.h5'
# Load the saved model
model = tf.keras.models.load_model( 'model/classification_model.h5')

# Define the labels for prediction
class_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                'dog', 'frog', 'horse', 'ship', 'truck']

# Configure Streamlit layout
st.set_page_config(page_title="Object Classification", layout="wide")

# Custom CSS to enhance the appearance
st.markdown(
    """
    <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #F63366;
            color: #FFFFFF;
            font-weight: bold;
            padding: 0.75rem 2rem;
            border-radius: 0.25rem;
            border: none;
            box-shadow: none;
        }
        .st-file-uploader {
            padding: 1rem 0;
        }
        .st-file-uploader>div>div:first-child {
            width: 100%;
        }
        .stImage>img {
            object-fit: contain;
            max-width: 100%;
            max-height: 500px;
        }
    </style>
    """,
    unsafe_allow_html=True
)