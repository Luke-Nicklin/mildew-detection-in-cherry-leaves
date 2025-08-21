import streamlit as st

def project_hypothesis_body():
    """Display the project hypothesis page."""
    st.title("Project Hypothesis")
    st.write("This page outlines the hypothesis of the project related to cherry leaf mildew detection.")

    # Placeholder for future content
    st.image("https://via.placeholder.com/600x400.png?text=Project+Hypothesis+Placeholder", caption="Project Hypothesis Placeholder")

    st.write("""
        **Hypothesis:**
        The hypothesis of this project is that machine learning models can effectively detect powdery mildew on cherry leaves based on visual features.
        
        **Objectives:**
        - To collect a dataset of cherry leaves with and without powdery mildew.
        - To train machine learning models to classify the presence of powdery mildew.
        - To evaluate the performance of these models using various metrics.
        
        More features will be added soon!
    """)