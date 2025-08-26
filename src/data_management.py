"""Data management utilities for Streamlit applications."""

import pickle
from io import BytesIO
import streamlit as st


def download_dataframe_as_csv(df):
    """
    Creates a download button in Streamlit to download a
    DataFrame as a CSV file.
    """
    # Create an in-memory buffer to hold the CSV data
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)

    # use Streamlit's built-in download button
    st.download_button(
        label="Download data as CSV",
        data=csv_buffer,
        file_name='data.csv',
        mime='text/csv'
                    )


def load_pkl_file(file_path):
    """Load a pickle file and return the object."""
    with open(file_path, 'rb') as file:
        return pickle.load(file)
