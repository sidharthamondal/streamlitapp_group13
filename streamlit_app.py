
# Main layout
col1, col2 = st.columns([1, 3])

# Left panel - Model capabilities
with col1:
    st.image("Images/image.png", use_column_width=True)
    st.title("Model Capabilities")
    st.write("This model can predict the following:")
    st.write(class_labels)

# Right panel - Image upload and prediction
with col2:
    st.title("Object Classification")
    st.write("Upload an image and get a prediction!")

    # Image upload section
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Perform prediction on the uploaded image
    if uploaded_image is not None:
        # Read the image
        img = image.load_img(uploaded_image, target_size=(32, 32))
        img_ss = image.load_img(uploaded_image, target_size=(256, 256))
        
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Preprocess the image
        img_array = img_array / 255.0

        # Make prediction
        prediction = model.predict(img_array)
        predicted_label = np.argmax(prediction)

        # Display the predicted label
        st.write(f"Predicted label: {class_labels[predicted_label]}")
        st.image(img_ss, caption="Uploaded Image", use_column_width=False)
