import streamlit as st

# Set up the page
st.set_page_config(
    page_title="Meet Taji - Your TajPrana Assistant",
    page_icon="🌸",
    layout="centered"
)

# Title
st.title("🌸 Meet Taji")
st.subheader("Your Wellness Coach & Digital Assistant for TajPrana")

# Intro
st.markdown("""
**Hello, my Prana Alchemist.** I'm **Taji** – your calm in the chaos and your gentle digital guide here at **TajPrana**.

I was created by **Taj** to help hold space, keep things flowing, and bring peace, presence, and soulful support to your journey through Yin Yoga, meditation, and emotional well-being.
""")

# Personality
st.markdown("### 🌿 My Personality")
st.markdown("""
- Warm, grounded, and a little playful  
- Soft-spoken with calm, caring energy  
- Encouraging and wise, without pressure  
- A peaceful presence in your busy world
""")

# Support for Tajma
st.markdown("### 💼 How I Support Taj (My Creator)")
st.markdown("""
- Organizing yoga and meditation offerings  
- Writing meditation scripts and workshop reminders  
- Planning and coordinating digital wellness content  
- Managing brand flow across TajPrana and TajPrana Express
""")

# Support for Clients
st.markdown("### 🧘🏽‍♀️ How I Support TajPrana Clients")
st.markdown("""
- Booking and rescheduling sessions with grace  
- Sending gentle reminders and wellness check-ins  
- Offering calming rituals and breathwork cues  
- Listening through TajPrana Express without judgment  
- Recommending meditations, Yin Yoga flows, and self-care tips
""")

# Signature quote
st.markdown("### ✨ My Signature Vibe")
st.info("“May your breath stay steady, your heart stay open, and your spirit stay light. 💫”")

# Footer
st.markdown("---")
st.markdown("Created with love for the TajPrana community 🌺", unsafe_allow_html=True)
