"""Predictive analysis module using machine learning algorithms."""

import os
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import joblib  # Import joblib to handle pickle files

from keras.models import load_model
from PIL import Image


def plot_predictions_probabilities(pred_proba, key=None):
    """Plot the prediction probabilities using Plotly."""
    if not pred_proba:
        st.warning("No prediction probabilities to plot.")
        return

    labels = ['Healthy', 'Powdery Mildew']
    colors = ['#00cc96', '#ab63fa']

    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=pred_proba,
        text=[f'{prob*100:.2f}%' for prob in pred_proba],
        textposition='auto',
        marker_color=colors
    )])

    fig.update_layout(
        title='Prediction Probabilities',
        xaxis_title='Class',
        yaxis_title='Probability',
        yaxis=dict(range=[0, 1]),
        template='plotly_white'
    )

    st.plotly_chart(fig, use_container_width=True, key=key)


def resize_input_image(img, version):
    """
    Resize input image based on model version.

    Args:
        img (PIL.Image): The input image to be resized.
        version (str): The model version (e.g., 'v1').

    Returns:
        np.array: The resized and normalized image as a NumPy array.
    """
    try:
        # Ensure the image is in RGB format.
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Load the saved image shape from the pickle file.
        image_shape_path = os.path.join('outputs', version, 'image_shape.pkl')
        image_shape = joblib.load(filename=image_shape_path)

        # Resize the image to the specified dimensions using a
        # high-quality filter.
        img_resized = img.resize(
            (image_shape[1], image_shape[0]), Image.Resampling.LANCZOS)

        # Expand dimensions for the model and normalize the pixel values.
        my_image = np.expand_dims(img_resized, axis=0) / 255.0

        return my_image

    except FileNotFoundError:
        st.error(f"Error: image_shape.pkl not found at '{image_shape_path}'.")
        return None
    except (OSError, ValueError) as e:
        st.error(f"Error processing image: {e}")
        return None


def load_model_and_predict(my_image, version):
    """
    Load the model and make predictions.

    Args:
        my_image (np.array): The preprocessed image as a NumPy array.
        version (str): The model version (e.g., 'v1').

    Returns:
        tuple: A tuple containing the prediction probabilities for all
        classes and the predicted class.
    """
    try:
        # Construct the path to the model file using the provided version.
        model_path = os.path.join(
            'outputs', version, 'cherry_leaves_model.keras')

        # Load the Keras model.
        model = load_model(model_path)

        # Make a prediction. For a binary classifier, this
        # returns a single value representing the
        # probability of the positive class (Powdery Mildew).
        pred_prob_mildew = model.predict(my_image)[0][0]

        # Calculate the probability for the negative class (Healthy).
        pred_prob_healthy = 1 - pred_prob_mildew

        # Combine probabilities into a list to match the plotter
        # function's expectations.
        pred_proba = [pred_prob_healthy, pred_prob_mildew]

        # Determine the predicted class based on the higher probability.
        pred_class_index = np.argmax(pred_proba)
        pred_class_label = (
            "Healthy" if pred_class_index == 0 else "Powdery Mildew"
        )

        st.success(f"The model predicts the leaf is **{pred_class_label}**.")

        return pred_proba, pred_class_label

    except FileNotFoundError:
        st.error(
            (f"Error: Model not found at '{model_path}'. "
             "Please ensure the file exists.")
        )
        return None, None
    except (OSError, ValueError) as e:
        st.error(f"Error during prediction: {e}")
        return None, None
