"""Model performance page."""

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import image as imread



def ml_performance_body():
    """Display the machine learning performance page."""
    st.title("Machine Learning Performance")
    st.write("Below shows the performance metrics of the machine "
             "learning models used in this project.")
    
    st.write("### Train, Validation and Test Set: Labels Distribution")
    st.image("streamlit_images/labels-distribution.png",
             caption="Labels Distribution in Train, Validation and Test Sets",
             use_container_width=True)
