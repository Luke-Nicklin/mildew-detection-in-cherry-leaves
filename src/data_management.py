"""Data management utilities for Streamlit applications."""


from io import BytesIO
from datetime import datetime
import pickle
import streamlit as st
import pandas as pd


def download_dataframe_as_csv(df: pd.DataFrame, **kwargs):
    """
    Generates a download button for a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to download.
        **kwargs: Additional keyword arguments to pass to st.download_button,
                  including 'key' for a unique widget identifier.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    file_name = f"prediction-results-{timestamp}.csv"

    # Create an in-memory buffer to hold the CSV data
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Use Streamlit's built-in download button, passing all keyword arguments
    st.download_button(
        label="Download Results as CSV",
        data=csv_buffer,
        file_name=file_name,
        mime='text/csv',
        **kwargs
    )


def load_pkl_file(file_path):
    """Load a pickle file and return the object."""
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"Error: Pickle file not found at '{file_path}'.")
        return None
