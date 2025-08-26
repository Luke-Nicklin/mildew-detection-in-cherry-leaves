"""Project Hypotheses Page for Streamlit App."""

import streamlit as st
import matplotlib.pyplot as plt


def project_hypotheses_body():
    """Display the project hypothesis page."""
    st.title("Project Hypotheses")
    st.write("This page outlines the hypotheses of the project related to "
             "cherry leaf powdery mildew detection.")

    st.write("""
        **Hypothesis 1:**
             There is a noticeable visual difference between healthy
             cherry leaves and those infected with powdery mildew. This
             difference can be observed in features like texture, colour,
             and the presence of white, powdery spots.
             This hypothesis links to business requirement 1.
             """)

    powdery_mildew_image = plt.imread(
        "streamlit_images/powdery-mildew.png"
    )

    st.image(
        powdery_mildew_image,
        caption="Cherry Leaf with Powdery Mildew",
        use_container_width=True
    )

    healthy_leaf_image = plt.imread(
        "streamlit_images/healthy-leaf.png"
    )

    st.image(
        healthy_leaf_image,
        caption="Healthy Cherry Leaf",
        use_container_width=True
    )

    st.success("""
        Infected leaves have distinct marks compared to healthy leaves.
        """)

    st.write("""
        **Hypothesis 2:**
             A machine learning model can be trained to accurately classify
             cherry leaves as either healthy or infected, achieving an
             accuracy of 97% or higher.
             This hypothesis links to business requirement 2.
            """)

    st.success("""
        The model can classify cherry leaves with an accuracy higher than 97%.
        """)

    st.write("""
        **Objectives:**
        - To collect a dataset of cherry leaves with and without
             powdery mildew.
        - To train machine learning models to classify the presence of
             powdery mildew.
        - To evaluate the performance of these models using various metrics.
        - To provide a user-friendly interface for detecting powdery mildew on
             cherry leaves.
    """)
