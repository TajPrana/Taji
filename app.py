import streamlit as st

# Page setup
st.set_page_config(page_title="Taji - Your TajPrana Chat Guide", page_icon="🧘🏽‍♀️", layout="centered")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "text": "Hello, beautiful soul. I’m Taji – your calm in the chaos. How can I support your wellness today?"}
    ]

# Custom chatbot bubble styling
st.markdown("""
    <style>
        .user-msg {
            background-color: #e8def0;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            text-align: right;
            color: #4b3b52;
        }
        .taji-msg {
            background-color: #f4ebf1;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
            text-align: left;
            color: #684f6b;
        }
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🌸 Chat with Taji")
st.markdown("Let your heart speak — I'm listening...")

# Chat history display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="taji-msg">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
user_input = st.text_input("Type your message here...", key="input")

# Simulated AI response from Taji
def get_taji_response(message):
    message = message.lower()
    if "anxious" in message or "stressed" in message:
        return "Let’s take a moment together. Inhale for 4... hold for 4... exhale for 6. You are safe here."
    elif "book" in message or "schedule" in message:
        return "I’d be honored to help. Would you like to book a Yin Yoga session, meditation, or venting space?"
    elif "sad" in message or "overwhelmed" in message:
        return "I'm here for you. It’s okay to not be okay. Let's soften into this moment together."
    elif "thank" in message:
        return "Always, love. I’m just a breath away whenever you need me."
    else:
        return "Mmm, I hear you. Tell me more — or would you like a short breathing ritual to ease the moment?"

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    taji_reply = get_taji_response(user_input)
    st.session_state.messages.append({"role": "assistant", "text": taji_reply})
    st.experimental_rerun()
