import streamlit as st
import os

# Set page config
st.set_page_config(page_title="Our Memories", page_icon="📸", layout="centered")

# Memories Storage Directory
memories_dir = "memories"
if not os.path.exists(memories_dir):
    os.makedirs(memories_dir)

st.markdown("<h1 style='text-align: center; color: #ff4d94;'>💞 Our Shared Memories 💞</h1>", unsafe_allow_html=True)

# Upload Section (Images & Videos)
uploaded_files = st.file_uploader(
    "Upload your favorite pictures and videos together!", 
    accept_multiple_files=True, 
    type=["jpg", "png", "jpeg", "mp4"]
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(memories_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
    st.success("Memories uploaded successfully! ❤️")

# Display stored images & videos
media_files = os.listdir(memories_dir)
if media_files:
    st.markdown("### 📸 Your Uploaded Memories")
    for file in sorted(media_files):
        file_path = os.path.join(memories_dir, file)
        if file.lower().endswith(("jpg", "png", "jpeg")):
            st.image(file_path, caption="A beautiful memory ❤️", use_container_width=True)
        elif file.lower().endswith("mp4"):
            st.video(file_path)
else:
    st.info("No memories uploaded yet. Start adding some! 💖")
