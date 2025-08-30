"""Powdery Mildew Detector Page"""

import uuid
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    plot_predictions_probabilities,
    resize_input_image,
    load_model_and_predict
)


def powdery_mildew_detector_body():
    """Display the powdery mildew detector page."""
    st.title("Powdery Mildew Detector")
    st.write("Upload one or more cherry leaf images to detect the presence of "
             "powdery mildew using a machine learning model.")

    st.write(
        "You can download a set of healthy and infected leaf images from "
        "[Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
    )

    # File uploader for image input with multiple file support
    uploaded_files = st.file_uploader(
        "Choose an image file(s) (JPG, PNG)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    # Define the model version
    version = 'v1'

    if uploaded_files:
        if st.button('Predict'):
            with st.spinner('Processing...'):
                for uploaded_file in uploaded_files:
                    # Create a unique key for each element in the loop
                    unique_key = str(uuid.uuid4())

                    # Display the uploaded image
                    st.image(
                        uploaded_file,
                        caption=f'Uploaded Image: {uploaded_file.name}',
                        use_container_width=True
                    )

                    # Open the image file
                    image = Image.open(uploaded_file)

                    # Resize and preprocess the image
                    my_image = resize_input_image(image, version)

                    # Check if image processing was successful
                    if my_image is not None:
                        # Load model and make predictions
                        pred_proba, _ = load_model_and_predict(
                            my_image=my_image, version=version
                        )

                        if pred_proba is not None:
                            # Ensure pred_proba is a list for the
                            # plotting function
                            if isinstance(pred_proba, np.ndarray):
                                pred_proba = pred_proba.tolist()

                            st.write(
                                f"### Prediction for {uploaded_file.name}")

                            # Plot prediction probabilities with a unique key
                            plot_predictions_probabilities(
                                pred_proba, key=f"plotly-chart-{unique_key}")

                            # Prepare results for download
                            results_df = pd.DataFrame({
                                'Class': ['Healthy', 'Powdery Mildew'],
                                'Probability': pred_proba
                            })

                            # Download button for results, with a unique key
                            download_dataframe_as_csv(
                                results_df,
                                key=f"download-button-{unique_key}"
                            )

                st.success("Prediction complete for all images!")
