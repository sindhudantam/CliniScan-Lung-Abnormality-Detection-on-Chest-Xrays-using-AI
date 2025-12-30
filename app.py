import streamlit as st
import os
from PIL import Image

# --------------------------------------------------
# MUST BE FIRST STREAMLIT COMMAND
# --------------------------------------------------
st.set_page_config(
    page_title="Abnormality Detection Results",
    layout="wide"
)

# --------------------------------------------------
# Paths
# --------------------------------------------------
OUTPUT_DIR = "output_images"

# --------------------------------------------------
# UI
# --------------------------------------------------
st.title("🩻 Abnormality Detection Results Viewer")
st.write(
    "Upload any image to view previously detected abnormality results.\n\n"
    "**Note:** Detection is NOT performed again."
)

uploaded_file = st.file_uploader(
    "Upload any image (used only as a trigger)",
    type=["png", "jpg", "jpeg"]
)

# --------------------------------------------------
# Show existing outputs
# --------------------------------------------------
if uploaded_file:

    st.success("Showing abnormality detections from output_images folder")

    image_files = [
        f for f in os.listdir(OUTPUT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not image_files:
        st.warning("No annotated images found in output_images/")
    else:
        for img_name in image_files:
            img_path = os.path.join(OUTPUT_DIR, img_name)
            img = Image.open(img_path)

            st.markdown("---")
            st.subheader(f"🧠 Detected Abnormalities: {img_name}")
            st.image(img, use_column_width=True)

else:
    st.info("Please upload any image to display detection results.")
