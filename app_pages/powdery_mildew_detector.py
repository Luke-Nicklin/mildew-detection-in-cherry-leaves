"""Powdery Mildew Detector Page"""

import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    plot_predictions_probabilities,
    resize_input_image,
)
from src.machine_learning.predictive_analysis import load_model_and_predict


def powdery_mildew_detector_body():
    """Display the powdery mildew detector page."""
    st.title("Powdery Mildew Detector")
    st.write("Upload an image of a cherry leaf to detect the presence of "
             "powdery mildew using a machine learning model.")

    st.write(
        "You can download a set of healthy and infected leaf images from "
        "[Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
    )

    # File uploader for image input
    uploaded_file = st.file_uploader(
        "Choose an image file (JPG, PNG)", type=["jpg", "jpeg", "png"]
    )

    # Define the model version
    version = 'v1'

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        if st.button('Predict'):
            with st.spinner('Processing...'):
                # Resize and preprocess the image
                my_image = resize_input_image(image, version)

                # Check if image processing was successful
                if my_image is not None:
                    # Load model and make predictions
                    pred_proba, _ = load_model_and_predict(
                        my_image=my_image, version=version
                    )

                    if pred_proba is not None:
                        # Ensure pred_proba is a list for the plotting function
                        if isinstance(pred_proba, np.ndarray):
                            pred_proba = pred_proba.tolist()

                        # Plot prediction probabilities
                        plot_predictions_probabilities(pred_proba)

                        # Prepare results for download
                        results_df = pd.DataFrame({
                            'Class': ['Healthy', 'Powdery Mildew'],
                            'Probability': pred_proba
                        })

                        # Download button for results
                        st.write(download_dataframe_as_csv(results_df))
                        st.success(
                            "Prediction complete! "
                            "You can download the results above."
                        )
