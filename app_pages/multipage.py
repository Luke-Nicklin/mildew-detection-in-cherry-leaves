"""Multipage page management for Streamlit apps."""

import streamlit as st

# MultiPage class to manage multiple pages in a Streamlit app


class MultiPage:
    """Framework for combining multiple Streamlit applications."""

    def __init__(self, app_name) -> None:
        """Initialize the MultiPage app with a name."""
        self.app_name = app_name
        self.pages = []

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":cherry_blossom:")

    def add_page(self, title, func) -> None:
        """Add a new page to the app."""
        self.pages.append({"title": title, "function": func})

    def run(self):
        """Run the multi-page app."""
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
