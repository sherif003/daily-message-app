import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

# Set up Streamlit page
st.set_page_config(page_title="Message of the Day", page_icon="💌", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF69B4;'>💌 Message of the Day 💌</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FF1493;'>for Ayoy</h2>", unsafe_allow_html=True)

# Connect to SQLite database
conn = sqlite3.connect("messages.db")
cursor = conn.cursor()

# Create the messages table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        author TEXT,
        message TEXT
    )
""")
conn.commit()

# Function to load messages from the database
def load_messages():
    cursor.execute("SELECT date, author, message FROM messages ORDER BY date DESC")
    return cursor.fetchall()

# Function to save a message
def save_message(author, message):
    today = date.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO messages (date, author, message) VALUES (?, ?, ?)", (today, author, message))
    conn.commit()
    st.success(f"✅ Message from {author.strip()} has been saved successfully!")

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

# Load messages from SQLite
messages = load_messages()

# Show today's messages
today = date.today().strftime("%Y-%m-%d")
today_messages = [msg for msg in messages if msg[0] == today]

st.markdown("<h3 style='text-align: center;'>📅 Today's Messages</h3>", unsafe_allow_html=True)
if today_messages:
    for msg in today_messages:
        st.write(f"💖 From {msg[1]}: {msg[2]} 💖")
else:
    st.write("No messages for today yet. 💌")

# Show past messages (same format as before)
if messages:
    st.markdown("<h3 style='text-align: center;'>📜 Past Messages</h3>", unsafe_allow_html=True)
    for msg in sorted(messages, key=lambda x: x[0], reverse=True):
        st.write(f"📅 **{msg[0]}** - 💌 From {msg[1]}: {msg[2]}")

# Export messages as CSV
messages_df = pd.DataFrame(messages, columns=["Date", "Author", "Message"])
csv = messages_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Messages as CSV", csv, "messages.csv", "text/csv")

# Close the database connection
conn.close()
