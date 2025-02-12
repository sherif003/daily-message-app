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

# Load existing messages or initialize as an empty list
if os.path.exists(MESSAGES_FILE):
    try:
        with open(MESSAGES_FILE, "r") as file:
            messages = json.load(file)
        if not isinstance(messages, list):
            messages = []  # Reset to empty list if the file contents are not a list
    except json.JSONDecodeError:
        messages = []  # Reset to empty list if the file is not valid JSON
else:
    messages = []

# Valentine's Day CSS for a cute, mobile-friendly layout with animations
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #FFE6E6;
    }
    .title {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #FF1493;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #FF69B4;
        text-align: center;
        font-size: 1.5rem;
        margin-top: -10px;
    }
    .message-box {
        font-family: "Arial", sans-serif;
        background-color: #FFF0F5;
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
    .heart {
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: red;
        transform: rotate(-45deg);
        animation: float 5s infinite ease-in-out;
    }
    .heart:before, .heart:after {
        content: '';
        position: absolute;
        width: 10px;
        height: 10px;
        background-color: red;
        border-radius: 50%;
    }
    .heart:before {
        top: -5px;
        left: 0;
    }
    .heart:after {
        left: 5px;
        top: 0;
    }
    @keyframes float {
        0%, 100% {
            transform: translateY(0) rotate(-45deg);
        }
        50% {
            transform: translateY(-20px) rotate(-45deg);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add floating hearts animation
st.markdown(
    """
    <div>
        <div class="heart" style="top: 10%; left: 20%;"></div>
        <div class="heart" style="top: 20%; left: 50%;"></div>
        <div class="heart" style="top: 30%; left: 80%;"></div>
        <div class="heart" style="top: 40%; left: 10%;"></div>
        <div class="heart" style="top: 50%; left: 70%;"></div>
        <div class="heart" style="top: 60%; left: 30%;"></div>
        <div class="heart" style="top: 70%; left: 90%;"></div>
        <div class="heart" style="top: 80%; left: 40%;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display the app title
st.markdown('<h1 class="title">💌 Message of the Day 💌</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">for Ayoy</h2>', unsafe_allow_html=True)

# Form for writing a new message
with st.form("message_form"):
    author = st.text_input("Your name (e.g., You or Her):", "")
    new_message = st.text_area("Write your message below:", height=150)
    submitted = st.form_submit_button("Save Message 💾", help="Save today's message")
    
    if submitted:
        today = date.today().strftime("%Y-%m-%d")
        if author.strip() and new_message.strip():
            messages.append({"date": today, "author": author.strip(), "message": new_message.strip()})
            
            # Save to file
            with open(MESSAGES_FILE, "w") as file:
                json.dump(messages, file)
            
            st.success(f"Message from {author.strip()} has been saved successfully!")
        else:
            st.error("Please fill in both the name and the message.")

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
    st.markdown("<h2 style='text-align: center;'>Past Messages</h2>", unsafe_allow_html=True)
    for msg in sorted(messages, key=lambda x: x["date"], reverse=True):
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.write(f"**{msg['date']}**")
        st.write(f"💌 From {msg['author']}: {msg['message']}")
        st.markdown('</div>', unsafe_allow_html=True)
