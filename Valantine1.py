import streamlit as st
import random
from datetime import datetime

# Set page config
st.set_page_config(page_title="My Love for You", page_icon="❤️", layout="centered")

# Love Messages
love_messages = [
    "You are my heart, my soul, my everything! ❤️",
    "Every moment with you is like a dream come true! 💖",
    "You light up my world like no one else! ✨",
    "I love you more than words can ever express! 💕",
    "Forever and always, you are my greatest treasure! 🎁",
]

# Function to play romantic sound
def play_romantic_sound():
    sound_file = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    st.markdown(f"""
        <audio autoplay loop>
        <source src="{sound_file}" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

play_romantic_sound()

# Header
st.markdown("<h1 style='text-align: center; color: #ff4d94;'>Happy Valentine's Day! ❤️</h1>", unsafe_allow_html=True)

# Display a random love message
st.markdown(f"<h2 style='text-align: center; color: #ff3385;'>{random.choice(love_messages)}</h2>", unsafe_allow_html=True)

# Countdown to next Valentine's Day
next_valentine = datetime(datetime.now().year + 1, 2, 14)
time_remaining = next_valentine - datetime.now()
days, seconds = divmod(time_remaining.total_seconds(), 86400)
hours, seconds = divmod(seconds, 3600)
minutes, _ = divmod(seconds, 60)
st.markdown(f"<h3 style='text-align: center; color: #ff3385;'>Countdown to next Valentine's Day: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes 💘</h3>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #ff66b2;'>Made with ❤️ just for you!</p>", unsafe_allow_html=True)
