"""Module to evaluate a classification model using Streamlit."""

from src.data_management import load_pkl_file


def load_evaluation_metrics(version):
    """
    Load evaluation metrics from a pickle file.

    Args:
        version (str): The model version (e.g., 'v1').

    Returns:
        dict: A dictionary containing evaluation metrics.
    """
    metrics_path = f'outputs/{version}/evaluation.pkl'
    return load_pkl_file(metrics_path)
