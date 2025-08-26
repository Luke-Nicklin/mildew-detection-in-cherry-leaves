"""Predictive analysis module using machine learning algorithms."""

import streamlit as st
import numpy as np
import pandas as pd
import plotly
from plotly import graph_objs
import plotly.graph_objects as go

from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """Plot the prediction probabilities using Plotly."""
    labels = ['Healthy', 'Powdery Mildew']
    colors = ['#00cc96', '#ab63fa']

    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=pred_proba[0],
        text=[f'{prob*100:.2f}%' for prob in pred_proba[0]],
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

    st.plotly_chart(fig, use_container_width=True)


def resize_input_image(img, version):
    """Resize input image based on model version."""
    image_shape = load_pkl_file(file_path=f"outputs/{version}image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]),
                             Image.Resampling.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """Load the model and make predictions."""
    model = load_model(f'outputs/{version}cherry_leaves_model.keras')
    pred_proba = model.predict(my_image)[0, 0]
    pred_class = np.argmax(pred_proba, axis=1)

    st.write(
        f"The model predicts the leaf is {'Healthy' if pred_class == 0 else
                                          'Powdery Mildew'}"
    )

    return pred_proba, pred_class
