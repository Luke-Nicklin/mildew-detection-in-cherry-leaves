import streamlit as st

def summary_body():
    """Display the summary page."""
    st.title("Project Summary")
    st.write("This page provides a summary of the project, "
             "including key findings and conclusions.")
    
    st.write(
        "This project focuses on detecting powdery mildew on"
        " cherry leaves using machine learning techniques.\n\n"
        "The goal is to provide a reliable method for farmers"
        " and researchers to identify and manage this disease effectively.")
    
    # Placeholder for future content
    st.image("https://via.placeholder.com/600x400.png?text=Project+Summary+Placeholder", caption="Project Summary Placeholder")
    
    st.write("More features will be added soon!")
    st.write("""
        **Key Findings:**
        - Machine learning models can effectively classify cherry leaves based 
        "on the presence of powdery mildew.
        - The dataset used for training and testing includes various images of 
        "cherry leaves with and without the disease.
        
        **Conclusions:**
        - The project demonstrates the potential of using machine learning for 
        "agricultural disease detection.
        - Future work will focus on improving model accuracy and expanding the 
        "dataset.
    """)