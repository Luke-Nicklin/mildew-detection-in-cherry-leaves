"""Model performance page."""

import os
import streamlit as st
import pandas as pd
from src.machine_learning.evaluate_clf import load_evaluation_metrics


def ml_performance_body():
    """ML performance metrics page."""
    st.title("Machine Learning Performance")

    # Find the root directory
    st.write("### Train, Validation and Test Set: Labels Distribution")
    st.image(os.path.join("outputs", "v1", "label_distribution_bar.png"),
             caption="Labels Distribution in Train, Validation and Test Sets",
             use_container_width=True)

    st.write("### Model history")
    col1, col2 = st.columns(2)
    with col1:
        st.image(os.path.join("outputs", "v1", "model_training_acc.png"),
                 caption="Model training accuracy",
                 use_container_width=True)
    with col2:
        st.image(os.path.join("outputs", "v1", "model_training_losses.png"),
                 caption="Model training losses",
                 use_container_width=True)

    st.write("### Genralised performance on the test set")
    version = "v1"
    metrics_df = pd.DataFrame(
        load_evaluation_metrics(version),
        index=['Loss', 'Accuracy'],
        columns=['Value']
    )
    st.dataframe(metrics_df)

    st.write("---")

    st.success("""
        The model achieved an accuracy of 99.68% on the test set, indicating
        strong generalisation capabilities.
        """)
