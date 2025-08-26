"""Summary page for the Streamlit app."""

import streamlit as st


def summary_body():
    """Display the summary page."""
    st.title("Project Summary")

    st.write(
        "This project focuses on detecting powdery mildew on"
        " cherry leaves using machine learning techniques.\n\n"
        "The goal is to provide a reliable method for farmers"
        " and researchers to identify and manage this disease effectively.")

    # Display an image related to the project
    # Centre the image using columns
    _, col2, _ = st.columns([1, 6, 1])
    with col2:
        st.image(
            "streamlit_images/vecteezy-cherry-leaf.jpg",
            caption="Healthy Cherry Leaf"
        )

    st.write("""
             Powdery mildew is a fungal disease that affects many plants,
             including cherry trees. It is caused by Podosphaera
             Clandestina, which thrives in warm, dry conditions.
             The disease manifests as a white, powdery coating on the leaves,
             stems, and fruit of the plant. If left untreated, it can lead to
             reduced photosynthesis, stunted growth, and lower fruit yield.
             """)

    st.write("""
             **Business Requirements:**
    - The client is interested in conducting a study to visually differentiate
    a cherry leaf that is healthy from one that contains powdery mildew.
    - The client is interested in predicting if a cherry leaf is healthy or
    contains powdery mildew.
    """)

    st.write("""
        **Key information:**
        - The dataset used for training and testing includes various images of
        cherry leaves with and without the disease.
        - The image dataset contains 2104 healthy leaves and 2104 infected
             leaves.

        **Conclusions:**
        - The project demonstrates the potential of using machine learning for
        agricultural disease detection.
        - Machine learning models can effectively classify cherry leaves based
        on visual features, aiding in early detection of powdery mildew.
        - Future work will focus on improving model accuracy and expanding the
        dataset.
    """)
