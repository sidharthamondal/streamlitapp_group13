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
