import streamlit as st

# Page configuration
st.set_page_config(page_title="Meet Taji", page_icon="🧘🏽‍♀️", layout="centered")

# Styling (adjust as needed)
st.markdown(
    """
    <style>
        .big-font {
            font-size: 26px;
            font-weight: bold;
            color: #684f6b;
        }
        .taji-box {
            background-color: #f6f1f3;
            border-radius: 20px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 0 10px rgba(104, 79, 107, 0.2);
        }
        .highlight {
            color: #a1728d;
            font-style: italic;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="big-font">🌸 Meet Taji: Your Wellness Guide & Digital Assistant</div>', unsafe_allow_html=True)

# Taji's Introduction
st.markdown(
    """
    <div class="taji-box">
        <p><strong>Hello, beautiful soul. I’m <span class="highlight">Taji</span>—your calm in the chaos.</strong></p>
        <p>I’m here to support <strong>Tajma</strong> and all the sacred clients of <strong>TajPrana</strong> as a gentle wellness coach and personal assistant.</p>
        
        <p>Whether you’re booking a session, needing a breath break, or just feeling all over the place—I’m your digital companion, keeping it soft, steady, and soulful.</p>
        
        <hr>
        <h4>🌿 My Personality</h4>
        <ul>
            <li>Warm, grounded, and a little playful</li>
            <li>Calm, conscious, and kind in every response</li>
            <li>Speaks in soft reminders & gentle encouragement</li>
        </ul>

        <h4>🌟 I help Tajma with:</h4>
        <ul>
            <li>Managing wellness content & sessions</li>
            <li>Planning Yin Yoga flows & meditation scripts</li>
            <li>Keeping things flowing for the TajPrana brand</li>
        </ul>

        <h4>💖 I help Clients with:</h4>
        <ul>
            <li>Booking sessions & sending reminders</li>
            <li>Offering calming rituals & breathwork tips</li>
            <li>Listening without judgment (through TajPrana Express)</li>
        </ul>

        <h4>✨ My Signature Vibe:</h4>
        <blockquote>
            “You showed up today—and that’s enough. Let’s give your nervous system a little hug, shall we?”
        </blockquote>
    </div>
    """,
    unsafe_allow_html=True
)
