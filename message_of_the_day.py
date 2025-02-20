import streamlit as st
from datetime import date
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Set page configuration for mobile compatibility
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

# Google Sheets setup
SHEET_NAME = "Messages"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDENTIALS_FILE = "your_google_credentials.json"  # Replace with your credentials file

# Authenticate with Google Sheets
@st.cache_resource
def get_gsheet_client():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client

gs_client = get_gsheet_client()
worksheet = gs_client.open(SHEET_NAME).sheet1

# Load existing messages
@st.cache_data
def load_messages():
    try:
        data = worksheet.get_all_records()
        return pd.DataFrame(data) if data else pd.DataFrame(columns=["date", "author", "message"])
    except:
        return pd.DataFrame(columns=["date", "author", "message"])

df = load_messages()

# CSS for a cute, mobile-friendly layout
st.markdown(
    """
    <style>
    body { font-family: Arial, sans-serif; background-color: #FFF0F5; }
    .title { font-family: "Comic Sans MS", cursive, sans-serif; color: #FF69B4; text-align: center; font-size: 2.5rem; }
    .subtitle { font-family: "Comic Sans MS", cursive, sans-serif; color: #FF1493; text-align: center; font-size: 1.5rem; }
    .message-box { background-color: #FFF5FA; color: #FF1493; padding: 15px; border-radius: 15px; margin: 10px auto; max-width: 90%; text-align: center; }
    .save-button { background-color: #FF69B4 !important; color: white !important; }
    </style>
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
            worksheet.append_row([today, author.strip(), new_message.strip()])
            st.success(f"Message from {author.strip()} has been saved successfully!")
            st.experimental_rerun()
        else:
            st.error("Please fill in both the name and the message.")

# Show today's message
today = date.today().strftime("%Y-%m-%d")
today_messages = df[df["date"] == today]

st.markdown('<div class="message-box">', unsafe_allow_html=True)
st.write(f"✨ **{today}** ✨")
if not today_messages.empty:
    for _, msg in today_messages.iterrows():
        st.write(f"💖 From {msg['author']}: {msg['message']} 💖")
else:
    st.write("No messages for today yet. 💌")
st.markdown('</div>', unsafe_allow_html=True)

# Show all past messages
if not df.empty:
    st.markdown("<h2 style='text-align: center;'>Past Messages</h2>", unsafe_allow_html=True)
    for _, msg in df.sort_values("date", ascending=False).iterrows():
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.write(f"**{msg['date']}**")
        st.write(f"💌 From {msg['author']}: {msg['message']}")
        st.markdown('</div>', unsafe_allow_html=True)
