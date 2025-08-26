"""Powdery Mildew Detector Page"""

import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict, plot_predictions_probabilities,
    resize_input_image
)


def powdery_mildew_detector_body():
    """Display the powdery mildew detector page."""
    st.title("Powdery Mildew Detector")
    st.write("Upload an image of a cherry leaf to detect the presence of "
             "powdery mildew using a machine learning model.")

    # File uploader for image input
    uploaded_file = st.file_uploader(
        "Choose an image file (JPG, PNG)", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        # Select model version
        version = st.selectbox(
            'Select Model Version',
            ('v1_', 'v2_', 'v3_')
        )

        if st.button('Predict'):
            with st.spinner('Processing...'):
                # Resize and preprocess the image
                my_image = resize_input_image(image, version)

                # Load model and make predictions
                pred_proba = load_model_and_predict(my_image, version)

                # Plot prediction probabilities
                plot_predictions_probabilities(np.array([pred_proba]))

                # Prepare results for download
                results_df = pd.DataFrame({
                    'Class': ['Healthy', 'Powdery Mildew'],
                    'Probability': pred_proba
                })

                # Download button for results
                download_dataframe_as_csv(results_df)
                st.success("Prediction complete! You can download the results above.")
                
