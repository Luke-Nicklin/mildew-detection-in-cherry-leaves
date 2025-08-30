"""Module for the leaves visualiser page in a Streamlit app."""


import os
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import image as imread
import random


def leaves_visualiser_body():
    """Display the leaves visualiser page."""

    # Correctly finding the project's root directory.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)

    st.title("Leaves Visualiser")
    st.write("""A study that visually analyses cherry leaves to
             differentiate between healthy and powdery mildew infected leaves.
             """)

    if st.checkbox("""Difference between average and variability image"""):
        st.write("Checking for average image files at these locations:")

        # Paths for the average images are constructed from the root_dir
        average_healthy_path = os.path.join(
            root_dir, "streamlit_images", "average-image-for-healthy.png")
        st.write(f"- Healthy image path: `{average_healthy_path}`")

        average_powdery_mildew_path = os.path.join(
            root_dir, "streamlit_images",
            "average-image-for-powdery-mildew.png")
        st.write(
            f"- Powdery Mildew image path: `{average_powdery_mildew_path}`")

        try:
            average_healthy_image = plt.imread(average_healthy_path)
            st.image(
                average_healthy_image,
                caption="Average healthy cherry leaf image",
                use_container_width=True
            )
        except FileNotFoundError:
            st.error("Error: Could not find average healthy image file.")

        try:
            average_powdery_mildew_image = plt.imread(
                average_powdery_mildew_path)
            st.image(
                average_powdery_mildew_image,
                caption="Average powdery mildew cherry leaf image",
                use_container_width=True
            )
        except FileNotFoundError:
            st.error("Error: Could not find average "
                     "powdery mildew image file.")

        st.write("""
            The average images show the general characteristics of
                 healthy and infected leaves.
            The healthy leaf image has a smooth texture, while the infected
                 leaf image shows a
            rough texture with white stripes.
            This visual difference supports the hypothesis that there is a
                 noticeable visual difference""")

    if st.checkbox("""Differences between average infected leaves and average
                   healthy leaves"""):
        st.write("Checking for average difference image at this location:")

        average_difference_path = os.path.join(
            root_dir, "streamlit_images", "average-difference-image.png")
        st.write(f"- Difference image path: `{average_difference_path}`")

        try:
            average_difference_image = plt.imread(average_difference_path)
            st.image(
                average_difference_image,
                caption="Average difference between healthy and "
                "infected leaves",
                use_container_width=True
            )
        except FileNotFoundError:
            st.error("Error: Could not find average difference image file.")

        st.write("""
            The differences between the average infected leaves and
                 average healthy leaves
            images didn't show any significant patterns.
            """)

    def image_montage(dir_path, nrows, ncols, figsize):
        """Creates and displays a montage of images from a directory."""
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        # Get a list of files and filter for image files (case-insensitive)
        all_files = os.listdir(dir_path)
        image_files = [f for f in all_files if f.lower().endswith(
            ('.png', '.jpg', '.jpeg'))]

        if not image_files:
            st.error("No image files found in the specified directory.")
            return

        # Randomly select images to display
        n_images_to_display = nrows * ncols
        if len(image_files) > n_images_to_display:
            selected_images = random.sample(image_files, n_images_to_display)
        else:
            selected_images = image_files
            random.shuffle(selected_images)

        st.write(f"Displaying a montage of {len(selected_images)} images...")

        for ax, img_file in zip(axes.flatten(), selected_images):
            img_path = os.path.join(dir_path, img_file)
            try:
                img = imread.imread(img_path)
                ax.imshow(img)
                ax.axis('off')
            except (FileNotFoundError, OSError) as e:
                st.error(f"Error reading image file: {img_path}. Error: {e}")
                ax.axis('off')

        plt.tight_layout()
        st.pyplot(fig)

    if st.checkbox("""Image montage"""):
        st.info(
            """To refresh the image montage, please select the
            'Create montage' button.""")

        my_data_dir = os.path.join(
            root_dir, 'inputs', 'cherry-leaves', 'cherry-leaves')

        validation_dir = os.path.join(my_data_dir, 'validation')

        st.write("Checking for image montage data at this location:")
        st.write(f"- Data directory path: `{validation_dir}`")

        try:
            labels = os.listdir(validation_dir)
            label_to_display = st.selectbox(
                label="Select label to display", options=labels, index=0)

            if st.button("Create montage"):

                dir_to_display = os.path.join(
                    validation_dir, label_to_display)

                image_montage(
                    dir_path=dir_to_display,
                    nrows=5, ncols=5, figsize=(10, 10))
        except FileNotFoundError:
            st.error(
                "Error: Could not find the main data directory. "
                "Please check the path displayed above.")
    st.write("""---""")
