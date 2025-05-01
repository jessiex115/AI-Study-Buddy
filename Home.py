# app.py - Your main home page
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Welcome to AI Study Buddy",
    layout="wide",
    initial_sidebar_state="expanded"  # Show sidebar by default
)

# Custom CSS for button styling
st.markdown("""
<style>
    .centered {
        text-align: center;
    }
    .nav-button {
        width: 100%;
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        font-size: 16px;
        transition: all 0.3s;
    }
    .nav-button:hover {
        transform: scale(1.02);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main Header - Centered
st.markdown("<h1 class='centered'>Welcome to AI Study Buddy</h1>", unsafe_allow_html=True)
st.markdown("""
<p class='centered'><em>Your personal assistant to learn, reflect, and engage with AI responsibly!</em></p>
""", unsafe_allow_html=True)

# Button Navigation Section
st.markdown("## Quick Navigation")

# Create columns for better button layout
col1, col2 = st.columns(2, gap="large")

with col1:
    # Button 1 - AI Usage Reflection
    if st.button(
        "AI Usage Reflection",
        key="btn_reflection",
        help="Reflect on your AI usage patterns",
        use_container_width=True
    ):
        st.switch_page("pages/1_AI_Usage_Reflection.py")
    
    # Button 2 - AI Literacy Modules
    if st.button(
        "AI Literacy Modules",
        key="btn_literacy",
        help="Learn essential AI concepts",
        use_container_width=True
    ):
        st.switch_page("pages/2_AI_Literacy_Modules.py")

with col2:
    # Button 3 - AI Challenges
    if st.button(
        "AI Challenges & Activities",
        key="btn_challenges",
        help="Practice your AI skills",
        use_container_width=True
    ):
        st.switch_page("pages/3_AI_Challenges_and_Activities.py")
    
    # Button 4 - Community Forum
    if st.button(
        "Community Forum",
        key="btn_forum",
        help="Connect with other learners",
        use_container_width=True
    ):
        st.switch_page("pages/4_Community_Forum.py")

# Full-width About button
if st.button(
    "About This Platform",
    key="btn_about",
    help="Learn about this platform",
    use_container_width=True
):
    st.switch_page("pages/5_About.py")

# Optional: Add some spacing and instructions
st.markdown("---")
st.markdown("""
**Tip:** You can also navigate using the sidebar on the left, 
or click any of the buttons above to jump directly to a section.
""")