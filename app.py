import streamlit as st
from app_pages.multipage import MultiPage  # Ensure MultiPage is defined in app_pages/multipage.py or correct the import path

# Load all pages here
from app_pages.leaves_visualiser import leaves_visualiser
from app_pages.ml_performance import ml_performance
from app_pages.powdery_mildew_detector import powdery_mildew_detector
from app_pages.project_hypothesis import project_hypothesis
from app_pages.summary import summary

app = MultiPage(app_name="Cherry Leaf Mildew Detector")

# Add all your pages here
app.add_page("Leaves Visualiser", leaves_visualiser)
app.add_page("ML Performance", ml_performance)
app.add_page("Powdery Mildew Detector", powdery_mildew_detector)
app.add_page("Project Hypothesis", project_hypothesis)
app.add_page("Summary", summary)