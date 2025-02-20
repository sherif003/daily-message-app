import streamlit as st
import sqlite3
from datetime import date

# Set up Streamlit page
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💌 Message of the Day 💌</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FF1493;'>for Ayoy</h2>", unsafe_allow_html=True)

# Connect to SQLite Database
@st.cache_resource
def get_db_connection():
    conn = sqlite3.connect("messages.db", check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            author TEXT,
            message TEXT
        )
    """)
    conn.commit()
    return conn

conn = get_db_connection()

# Function to load messages
@st.cache_data(ttl=300)  # Cache data for 5 minutes
def load_messages():
    cursor = conn.cursor()
    cursor.execute("SELECT date, author, message FROM messages ORDER BY date DESC")
    messages = cursor.fetchall()
    return messages

# Function to save messages
def save_message(author, message):
    today = date.today().strftime("%Y-%m-%d")
    conn.execute("INSERT INTO messages (date, author, message) VALUES (?, ?, ?)", (today, author, message))
    conn.commit()
    st.success(f"✅ Message from {author.strip()} has been saved successfully!")
    st.rerun()  # Refresh to show new messages immediately

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

# Load messages
messages = load_messages()

# Show today's messages
today = date.today().strftime("%Y-%m-%d")
today_messages = [msg for msg in messages if msg[0] == today]

st.markdown("<h3 style='text-align: center;'>📅 Today's Messages</h3>", unsafe_allow_html=True)
if today_messages:
    for msg in today_messages:
        st.markdown(f"💖 **From {msg[1]}**: {msg[2]} 💖")
else:
    st.write("No messages for today yet. 💌")

# Show past messages
if messages:
    st.markdown("<h3 style='text-align: center;'>📜 Past Messages</h3>", unsafe_allow_html=True)
    for msg in messages:
        st.markdown(f"📅 **{msg[0]}** - 💌 **From {msg[1]}**: {msg[2]}")
