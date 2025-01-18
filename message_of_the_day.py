import streamlit as st
from datetime import date

# Set page configuration
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

# Main container
st.markdown(
    """
    <style>
    .title {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #FF69B4;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .message-box {
        font-family: "Arial", sans-serif;
        background-color: #FFF0F5;
        color: #FF1493;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="title">💌 Message of the Day 💌 for Ayoy</h1>', unsafe_allow_html=True)

# Functionality to write and save the message
if "message" not in st.session_state:
    st.session_state["message"] = "Welcome! Write a message for your special someone. 💖"

# Input for new message
with st.form("message_form"):
    new_message = st.text_area("Write your message below:", st.session_state["message"], height=150)
    submitted = st.form_submit_button("Save Message 💾")

    if submitted:
        st.session_state["message"] = new_message
        st.success("Your message has been saved successfully!")

# Display the saved message
st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.write(f"✨ **{date.today().strftime('%A, %B %d, %Y')}** ✨")
st.write(f"💖 {st.session_state['message']} 💖")
st.markdown('</div>', unsafe_allow_html=True)
