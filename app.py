import streamlit as st
from app_pages.multipage import MultiPage  # Ensure MultiPage is defined in app_pages/multipage.py or correct the import path

# Load all pages here
from app_pages.summary import summary_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.leaves_visualiser import leaves_visualiser_body
from app_pages.powdery_mildew_detector import powdery_mildew_detector_body
from app_pages.ml_performance import ml_performance_body

app = MultiPage(app_name="Cherry Leaf Mildew Detector")

# Add all pages here
app.add_page("Summary", summary_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("Leaves Visualiser", leaves_visualiser_body)
app.add_page("Powdery Mildew Detector", powdery_mildew_detector_body)
app.add_page("ML Performance", ml_performance_body)

# Run the app
app.run()

# This is the main entry point for the Streamlit app.
