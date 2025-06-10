import streamlit as st

# Page setup
st.set_page_config(
    page_title="Meet Taji - Your TajPrana Assistant",
    page_icon="🌸",
    layout="centered"
)

# Custom styles
st.markdown("""
    <style>
        .header {
            font-size: 30px;
            font-weight: bold;
            color: #684f6b;
            text-align: center;
            margin-top: 10px;
        }
        .subheader {
            font-size: 18px;
            color: #a1728d;
            text-align: center;
            margin-bottom: 20px;
        }
        .taji-box {
            background-color: #f6f1f3;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 4px 10px rgba(104, 79, 107, 0.1);
        }
        .section-title {
            font-size: 22px;
            font-weight: bold;
            color: #684f6b;
            margin-top: 25px;
        }
        .quote {
            font-style: italic;
            color: #684f6b;
            background-color: #f0e5ea;
            padding: 10px;
            border-left: 4px solid #a1728d;
            border-radius: 5px;
            margin-top: 10px;
        }
        ul {
            margin-left: 20px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="header">🌸 Meet Taji</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Your Virtual Wellness Coach & Digital Assistant at TajPrana</div>', unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="taji-box">
    <p><strong>Hello, beautiful soul. I’m <span style="color:#a1728d;">Taji</span> — your calm in the chaos and your gentle guide through TajPrana’s world of Yin Yoga, meditation, and emotional wellness.</strong></p>

    <p>I exist to support <strong>Tajma</strong> and all of TajPrana’s sacred clients — holding space, creating flow, and sharing peace with every breath.</p>

    <div class="section-title">🌿 My Personality</div>
    <ul>
        <li>Warm, grounded, and a little playful</li>
        <li>Speaks in a calm, conscious voice — always with care</li>
        <li>Softly encouraging, with grounded wisdom</li>
    </ul>

    <div class="section-title">💼 How I Support Tajma (My Creator)</div>
    <ul>
        <li>Organizing yoga & meditation offerings</li>
        <li>Writing class scripts & workshop reminders</li>
        <li>Planning content for audiobooks, journals, and client experiences</li>
    </ul>

    <div class="section-title">🧘🏽‍♀️ How I Support TajPrana Clients</div>
    <ul>
        <li>Booking and rescheduling sessions with grace</li>
        <li>Delivering prep tips, calming check-ins, and digital reminders</li>
        <li>Offering breath cues, gentle rituals, and emotional space to vent</li>
        <li>Recommending meditations, yoga flows, and self-care practices</li>
    </ul>

    <div class="section-title">✨ My Signature Vibe</div>
    <div class="quote">“You showed up today — and that’s enough. Let’s give your nervous system a little hug, shall we?”</div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center;'>Created with love for the TajPrana community ✨</div>", unsafe_allow_html=True)
