import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="My Love for You", page_icon="❤️", layout="centered")

# Single Love Message
love_message = "You are my heart, my soul, my everything! ❤️💖 Forever and always, you are my greatest treasure! Happy valantine's day ya Ayoy 💝"

# Header
st.markdown("<h1 style='text-align: center; color: #ff4d94;'>لَا الأَيَّامُ مَعَكَ كَمَا كَانَتْ قَبْلَكِ، وَلَا الدُّنْيَا مَعَكَ مِنَ الجَمَالِ تُوصَفُ ❤️</h1>", unsafe_allow_html=True)

# Display a single big message in white color
st.markdown(f"<h2 style='text-align: center; color: #ff3385; background-color: #000000; padding: 15px; border-radius: 10px;'>{love_message}</h2>", unsafe_allow_html=True)

# Countdown to next Valentine's Day
next_valentine = datetime(datetime.now().year + 1, 2, 14)
time_remaining = next_valentine - datetime.now()
days, seconds = divmod(time_remaining.total_seconds(), 86400)
hours, seconds = divmod(seconds, 3600)
minutes, _ = divmod(seconds, 60)
st.markdown(f"<h3 style='text-align: center; color: #ff3385;'>Countdown to next Valentine's Day: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes 💘</h3>", unsafe_allow_html=True)

# Surprise Button - Redirects to Memories Page
if st.button("Click for a Surprise! 🎁"):
    st.switch_page("pages/2_Memories.py")

# Footer
st.markdown("<p style='text-align: center; color: #ff66b2;'>Made with ❤️ just for you!</p>", unsafe_allow_html=True)
