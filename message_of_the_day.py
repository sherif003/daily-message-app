import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import date

# ✅ Securely Load Google Sheets Authentication
try:
    secrets_dict = st.secrets["google_service_account"]
    credentials = Credentials.from_service_account_info(dict(secrets_dict), scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(credentials)
except KeyError:
    st.error("Google Sheets API credentials are missing! Please add them to Streamlit Secrets.")
    st.stop()

# ✅ Google Sheet Name
SHEET_NAME = "Messages"  # Change this to match your sheet name
sheet = client.open(SHEET_NAME).sheet1

# ✅ Function to load messages
def load_messages():
    records = sheet.get_all_records()
    return records

# ✅ Function to save a new message
def save_message(author, message):
    today = date.today().strftime("%Y-%m-%d")
    sheet.append_row([today, author, message])

# ✅ Set up Streamlit UI
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💌 Message of the Day 💌</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FF1493;'>for Ayoy</h2>", unsafe_allow_html=True)

# ✅ Form for adding a message
with st.form("message_form"):
    author = st.text_input("Your name (e.g., You or Her):", "")
    new_message = st.text_area("Write your message below:", height=150)
    submitted = st.form_submit_button("Save Message 💾")
    
    if submitted:
        if author.strip() and new_message.strip():
            save_message(author.strip(), new_message.strip())
            st.success(f"Message from {author.strip()} has been saved successfully!")
        else:
            st.error("Please fill in both the name and the message.")

# ✅ Load messages **once**
messages = load_messages()

# ✅ Display today's messages
today = date.today().strftime("%Y-%m-%d")
today_messages = [msg for msg in messages if msg.get("Date", "") == today]

st.markdown("<h3 style='text-align: center;'>Today's Messages</h3>", unsafe_allow_html=True)
if today_messages:
    for msg in today_messages:
        st.write(f"💖 From {msg.get('Author', 'Unknown')}: {msg.get('Message', 'No message')} 💖")
else:
    st.write("No messages for today yet. 💌")

# ✅ Display past messages
if messages:
    st.markdown("<h3 style='text-align: center;'>Past Messages</h3>", unsafe_allow_html=True)
    for msg in sorted(messages, key=lambda x: x.get("Date", ""), reverse=True):
        st.write(f"📅 **{msg.get('Date', 'Unknown Date')}** - 💌 From {msg.get('Author', 'Unknown')}: {msg.get('Message', 'No message')}")
