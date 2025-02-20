import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import date

# Set up Streamlit page
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💌 Message of the Day 💌</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FF1493;'>for Ayoy</h2>", unsafe_allow_html=True)

# Debugging: Check Google Sheets connection
try:
    secrets_dict = st.secrets["google_service_account"]
    credentials = Credentials.from_service_account_info(
        dict(secrets_dict), 
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    client = gspread.authorize(credentials)
    SHEET_NAME = "Messages"  # Change if your sheet has a different name
    sheet = client.open(SHEET_NAME).sheet1

    st.success("✅ Google Sheets connection successful!")

except gspread.exceptions.APIError as e:
    st.error(f"❌ Google Sheets API Error: {str(e)}")
    st.stop()
except KeyError:
    st.error("❌ Google Sheets API credentials are missing! Please add them to Streamlit Secrets.")
    st.stop()
except Exception as e:
    st.error(f"❌ General Error: {str(e)}")
    st.stop()

# Function to load messages
def load_messages():
    try:
        records = sheet.get_all_records()
        return records
    except Exception as e:
        st.error(f"❌ Error loading messages: {str(e)}")
        return []

# Function to save messages
def save_message(author, message):
    try:
        today = date.today().strftime("%Y-%m-%d")
        sheet.append_row([today, author, message])
        st.success(f"✅ Message from {author.strip()} has been saved successfully!")
    except Exception as e:
        st.error(f"❌ Error saving message: {str(e)}")

# Form for adding a message
with st.form("message_form"):
    author = st.text_input("Your name (e.g., You or Her):", "")
    new_message = st.text_area("Write your message below:", height=150)
    submitted = st.form_submit_button("Save Message 💾")
    
    if submitted:
        if author.strip() and new_message.strip():
            save_message(author.strip(), new_message.strip())
        else:
            st.error("❌ Please fill in both the name and the message.")

# Load messages from Google Sheets
messages = load_messages()

# Show today's messages
today = date.today().strftime("%Y-%m-%d")
today_messages = [msg for msg in messages if msg["Date"] == today]

st.markdown("<h3 style='text-align: center;'>📅 Today's Messages</h3>", unsafe_allow_html=True)
if today_messages:
    for msg in today_messages:
        st.write(f"💖 From {msg['Author']}: {msg['Message']} 💖")
else:
    st.write("No messages for today yet. 💌")

# Show past messages
if messages:
    st.markdown("<h3 style='text-align: center;'>📜 Past Messages</h3>", unsafe_allow_html=True)
    for msg in sorted(messages, key=lambda x: x["Date"], reverse=True):
        st.write(f"📅 **{msg['Date']}** - 💌 From {msg['Author']}: {msg['Message']}")

