import streamlit as st
from datetime import date
import json
import os

# Set page configuration for mobile compatibility
st.set_page_config(
    page_title="Valentine's Message", 
    page_icon="❤️", 
    layout="centered"
)

# File to store messages
MESSAGES_FILE = "messages.json"

# Load existing messages or initialize as an empty list
if os.path.exists(MESSAGES_FILE):
    try:
        with open(MESSAGES_FILE, "r", encoding="utf-8") as file:
            messages = json.load(file)
        if not isinstance(messages, list):
            messages = []  # Reset to empty list if the file contents are not a list
    except json.JSONDecodeError:
        messages = []  # Reset to empty list if the file is not valid JSON
else:
    messages = []

# Valentine's Day Theme and Animation
st.markdown(
    """
    <style>
    @keyframes floating-hearts {
        0% { transform: translateY(0) scale(1); opacity: 1; }
        100% { transform: translateY(-100vh) scale(0.5); opacity: 0; }
    }
    body {
        font-family: Arial, sans-serif;
        background-color: #FFEEF0;
    }
    .title {
        font-family: "Dancing Script", cursive;
        color: #E91E63;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-family: "Dancing Script", cursive;
        color: #D81B60;
        text-align: center;
        font-size: 2rem;
        margin-top: -10px;
    }
    .message-box {
        font-family: "Arial", sans-serif;
        background-color: #FFEBEE;
        color: #C2185B;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        margin: 15px auto;
        max-width: 90%;
        text-align: center;
        font-size: 1.2rem;
    }
    .save-button {
        background-color: #E91E63 !important;
        color: white !important;
        border-radius: 5px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the app title
st.markdown('<h1 class="title">&#10084;&#65039; Valentine\'s Message &#10084;&#65039;</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">For My Love &#128149;</h2>', unsafe_allow_html=True)

# Form for writing a new message
with st.form("message_form"):
    author = st.text_input("Your name (e.g., You or Her):", "")
    new_message = st.text_area("Write your love message below:", height=150)
    submitted = st.form_submit_button("Save Message 💌", help="Save your sweet message")
    
    if submitted:
        today = date.today().strftime("%Y-%m-%d")
        if author.strip() and new_message.strip():
            messages.append({"date": today, "author": author.strip(), "message": new_message.strip()})
            
            # Save to file
            with open(MESSAGES_FILE, "w", encoding="utf-8") as file:
                json.dump(messages, file, ensure_ascii=False, indent=4)
            
            st.success(f"Message from {author.strip()} has been saved successfully! 💕")
        else:
            st.error("Please fill in both the name and the message. 💖")

# Show today's message
today = date.today().strftime("%Y-%m-%d")
today_messages = [msg for msg in messages if msg["date"] == today]

st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.write(f"✨ **{today}** ✨")
if today_messages:
    for msg in today_messages:
        st.write(f"💖 From {msg['author']}: {msg['message']} 💖")
else:
    st.write("No messages for today yet. 💌")
st.markdown('</div>', unsafe_allow_html=True)

# Show all past messages
if messages:
    st.markdown("<h2 style='text-align: center;'>Past Love Notes 💝</h2>", unsafe_allow_html=True)
    for msg in sorted(messages, key=lambda x: x["date"], reverse=True):
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.write(f"**{msg['date']}**")
        st.write(f"💌 From {msg['author']}: {msg['message']}")
        st.markdown('</div>', unsafe_allow_html=True)
