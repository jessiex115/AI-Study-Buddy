import streamlit as st

def main():
    st.set_page_config(page_title="AI Challenges", layout="wide")

    st.title("AI Challenges & Activities")
    st.markdown("""
    Apply what you've learned through interactive challenges that develop critical thinking 
    and human-AI collaboration skills. Choose any challenge to begin.
    """)
    st.markdown("---")
    
    # Initialize session state for selected challenge
    if "selected_challenge" not in st.session_state:
        st.session_state.selected_challenge = None
    
    # Challenge Selection Buttons
    st.markdown("### Select a Challenge or Activity")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Writing Challenge"):
            st.session_state.selected_challenge = "writing"
    
    with col2:
        if st.button("Reading Challenge"):
            st.session_state.selected_challenge = "reading"
    
    with col3:
        if st.button("Coding Challenge"):
            st.session_state.selected_challenge = "coding"
    
    with col4:
        if st.button("Ethics Debate"):
            st.session_state.selected_challenge = "ethics"
    
    st.markdown("---")
    
    # Writing Challenge
    if st.session_state.selected_challenge == "writing":
        st.subheader("Writing Challenge")
        st.markdown("""
        **Task:** Evaluate and refine an AI-generated paragraph to improve clarity and accuracy.
        
        **Instructions:**
        1. Review the AI-generated text below
        2. Identify areas needing improvement
        3. Rewrite the problematic sections
        4. Explain your changes
        """)
        
        ai_writing = st.text_area("AI-Generated Paragraph:", 
                                "Artificial intelligence is when computers can think like humans. " +
                                "All AI systems are completely objective and never make mistakes. " +
                                "Machine learning is the same as artificial intelligence.",
                                height=150)
        
        user_rewrite = st.text_area("Your Improved Version:", height=150)
        user_explanation = st.text_area("Explain your changes:", height=100)
        
        if st.button("Submit Writing Challenge"):
            if user_rewrite and user_explanation:
                st.success("Writing challenge submitted! Your critical thinking skills are developing well.")
            else:
                st.warning("Please complete both the rewrite and explanation.")
    
    # Reading Challenge
    elif st.session_state.selected_challenge == "reading":
        st.subheader("Reading Challenge")
        st.markdown("""
        **Task:** Analyze an AI-generated summary for accuracy and potential biases.
        
        **Instructions:**
        1. Read both the original text and AI summary
        2. Identify any inaccuracies or biases
        3. Highlight problematic sections
        4. Suggest improvements
        """)
        
        original_text = st.text_area("Original Text:", 
                                   "The Industrial Revolution brought major technological advances " +
                                   "but also created poor working conditions. While productivity increased, " +
                                   "many workers faced long hours in dangerous environments for low pay.",
                                   height=150)
        
        ai_summary = st.text_area("AI-Generated Summary:", 
                                 "The Industrial Revolution was entirely positive, bringing only " +
                                 "technological progress and economic growth for all members of society.",
                                 height=150)
        
        user_critique = st.text_area("Your Analysis:", 
                                   "Identify at least 3 issues in the AI summary...",
                                   height=150)
        
        if st.button("Submit Reading Challenge"):
            if user_critique:
                st.success("Excellent analysis! You've demonstrated strong critical reading skills.")
            else:
                st.warning("Please provide your analysis of the AI summary.")
    
    # Coding Challenge
    elif st.session_state.selected_challenge == "coding":
        st.subheader("Coding Challenge")
        st.markdown("""
        **Task:** Debug and improve AI-generated code while explaining your changes.
        
        **Instructions:**
        1. Review the AI-generated code
        2. Identify and fix any errors
        3. Improve the code's efficiency/readability
        4. Explain your modifications
        """)
        
        ai_code = st.text_area("AI-Generated Code:", 
                             "def calculate_average(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total / len(numbers)",
                             height=150)
        
        user_code = st.text_area("Your Improved Code:", height=150)
        code_explanation = st.text_area("Explanation of Changes:", height=100)
        
        if st.button("Submit Coding Challenge"):
            if user_code and code_explanation:
                st.success("Code improvements submitted! You've demonstrated authentic understanding.")
            else:
                st.warning("Please complete both the code improvements and explanation.")
    
    # Ethics Debate
    elif st.session_state.selected_challenge == "ethics":
        st.subheader("Ethics Debate")
        st.markdown("""
        **Task:** Construct arguments about AI ethics based on your knowledge.
        
        **Instructions:**
        1. Choose a debate prompt below
        2. Develop arguments for both sides
        3. State your personal position
        4. Justify your reasoning
        """)
        
        debate_prompt = st.selectbox(
            "Select a Debate Topic:",
            ["Should students be required to disclose AI assistance in all academic work?",
             "Is it ethical to use AI tools that may have been trained on copyrighted materials?",
             "Does AI do more harm than good in education?"]
        )
        
        pro_args = st.text_area("Arguments FOR the proposition:", height=100)
        con_args = st.text_area("Arguments AGAINST the proposition:", height=100)
        personal_position = st.text_area("Your Position and Justification:", height=150)
        
        if st.button("Submit Ethics Debate"):
            if pro_args and con_args and personal_position:
                st.success("Debate submitted! You've shown thoughtful consideration of AI ethics.")
            else:
                st.warning("Please complete all debate sections.")
    
    # Default message when no challenge selected
    else:
        st.info("Please select a challenge from the buttons above to begin.")

if __name__ == "__main__":
    main()