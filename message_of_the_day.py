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

# Valentine's Day CSS for a cute, interactive, and mobile-friendly layout
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');
    body {
        font-family: 'Indie Flower', cursive;
        background: linear-gradient(45deg, #FF9AA2, #FFB7B2, #FFDAC1, #E2F0CB);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .title {
        font-family: 'Indie Flower', cursive;
        color: #FF1493;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-family: 'Indie Flower', cursive;
        color: #FF69B4;
        text-align: center;
        font-size: 2rem;
        margin-top: -10px;
    }
    .message-box {
        font-family: 'Indie Flower', cursive;
        background-color: rgba(255, 255, 255, 0.8);
        color: #FF1493;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px auto;
        max-width: 90%;
        text-align: center;
        font-size: 1.2rem;
    }
    .save-button {
        background-color: #FF69B4 !important;
        color: white !important;
        border-radius: 15px !important;
        font-family: 'Indie Flower', cursive;
        font-size: 1.2rem;
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
    .sparkle {
        position: absolute;
        width: 5px;
        height: 5px;
        background-color: gold;
        border-radius: 50%;
        animation: sparkle 1s infinite ease-in-out;
    }
    @keyframes sparkle {
        0%, 100% { opacity: 0; }
        50% { opacity: 1; }
    }
    .balloon {
        position: absolute;
        width: 50px;
        height: 70px;
        background-color: #FF69B4;
        border-radius: 50%;
        animation: floatBalloon 10s infinite ease-in-out;
    }
    .balloon:before {
        content: '';
        position: absolute;
        width: 10px;
        height: 20px;
        background-color: #FF69B4;
        bottom: -20px;
        left: 20px;
    }
    @keyframes floatBalloon {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add floating hearts, sparkles, and balloons
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
        <div class="sparkle" style="top: 15%; left: 25%;"></div>
        <div class="sparkle" style="top: 35%; left: 75%;"></div>
        <div class="sparkle" style="top: 55%; left: 45%;"></div>
        <div class="balloon" style="top: 5%; left: 15%;"></div>
        <div class="balloon" style="top: 25%; left: 85%;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display the app title
st.markdown('<h1 class="title">💌 Message of the Day 💌</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">for Ayoy</h2>', unsafe_allow_html=True)

# Interactive buttons for virtual kisses and hugs
col1, col2 = st.columns(2)
with col1:
    if st.button("💋 Send a Kiss"):
        st.balloons()
        st.write("💖 Mwah! A virtual kiss has been sent to Ayoy! 💖")
with col2:
    if st.button("🤗 Send a Hug"):
        st.snow()
        st.write("💖 A warm virtual hug has been sent to Ayoy! 💖")

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
