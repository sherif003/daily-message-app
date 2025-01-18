import streamlit as st
from datetime import date
import json
import os

# Set page configuration for mobile compatibility
st.set_page_config(
    page_title="Message of the Day", 
    page_icon="💌", 
    layout="centered"
)

# File to store messages
MESSAGES_FILE = "messages.json"

# Load existing messages
if os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, "r") as file:
        messages = json.load(file)
else:
    messages = {}

# CSS for a cute, mobile-friendly layout
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #FFF0F5;
    }
    .title {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #FF69B4;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .message-box {
        font-family: "Arial", sans-serif;
        background-color: #FFF5FA;
        color: #FF1493;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px auto;
        max-width: 90%;
        text-align: center;
        font-size: 1rem;
    }
    .save-button {
        background-color: #FF69B4 !important;
        color: white !important;
        border-radius: 5px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the app title
st.markdown('<h1 class="title">💌 Message of the Day 💌</h1>', unsafe_allow_html=True)

# Form for writing a new message
with st.form("message_form"):
    new_message = st.text_area("Write your message below:", height=150)
    submitted = st.form_submit_button("Save Message 💾", help="Save today's message")
    
    if submitted:
        today = date.today().strftime("%Y-%m-%d")
        messages[today] = new_message
        
        # Save to file
        with open(MESSAGES_FILE, "w") as file:
            json.dump(messages, file)
        
        st.success("Your message has been saved successfully!")

# Show today's message
today = date.today().strftime("%Y-%m-%d")
st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.write(f"✨ **{today}** ✨")
st.write(f"💖 {messages.get(today, 'No message for today yet.')} 💖")
st.markdown('</div>', unsafe_allow_html=True)

# Show all past messages
if messages:
    st.markdown("<h2 style='text-align: center;'>Past Messages</h2>", unsafe_allow_html=True)
    for msg_date, msg_content in sorted(messages.items(), reverse=True):
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.write(f"**{msg_date}**: {msg_content}")
        st.markdown('</div>', unsafe_allow_html=True)
