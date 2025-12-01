import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AI Usage Reflection",
    layout="wide",
)

# Custom CSS
st.markdown("""
<style>
    .module-btn {
        transition: all 0.3s ease;
        margin: 0.5rem 0;
    }
    .module-btn:hover {
        transform: scale(1.02);
    }
    .reflection-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 1.5rem;
        border-left: 4px solid #1e88e5;
    }
    .question-card {
        padding: 1rem;
        border-radius: 8px;
        background-color: #ffffff;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .report-section {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f4f8;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    session_defaults = {
        "selected_module": None,
        "reflection1": "",
        "reflection2": "",
        "reflection3": "",
        "habit_questions": [],
        "user_answers": {},
        "journal_entries": [],
        "last_saved": None
    }
    
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Page Header
st.title("AI Usage Reflection")
st.markdown("""
Reflect on your AI usage experience and habits to improve your learning practices.
Track your progress and receive personalized feedback.
""")
st.markdown("---")

# Module selection
st.markdown("### Select a Reflection Module")
cols = st.columns(3)
module_data = [
    {"name": "Usage Experience Journal", "key": "experience", "desc": "Record your AI-assisted learning experiences"},
    {"name": "Usage Habit Assessment", "key": "assessment", "desc": "Evaluate your AI usage patterns"},
    {"name": "Your Personal Report", "key": "report", "desc": "Get personalized feedback"}
]

for i, module in enumerate(module_data):
    with cols[i]:
        if st.button(
            module["name"],
            key=module["key"],
            help=module["desc"],
            use_container_width=True
        ):
            st.session_state.selected_module = module["key"]
            st.rerun()

st.markdown("---")


# --- Usage Experience Journal ---
if st.session_state.selected_module == "experience":
    st.header("Usage Experience Journal")
    st.markdown("Reflect on your recent experiences using AI for learning tasks.")
    
    with st.container():
        st.subheader("New Journal Entry")
        with st.form("journal_form"):
            st.session_state.reflection1 = st.text_area(
                "1. What learning task did you use AI for?",
                placeholder="e.g., reading an article, writing a proposal, etc.",
                value=st.session_state.reflection1
            )
            st.session_state.reflection2 = st.text_area(
                "2. Which AI tool did you use?",
                placeholder="e.g., ChatGPT, DeepSeek, Grammarly, etc.",
                value=st.session_state.reflection2
            )
            st.session_state.reflection3 = st.text_area(
                "3. How did you use it?",
                placeholder="e.g., I asked AI to summarize key ideas of an article...",
                value=st.session_state.reflection3
            )
            
            submitted = st.form_submit_button("Save Entry")
            if submitted:
                if st.session_state.reflection1 and st.session_state.reflection2 and st.session_state.reflection3:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                    entry = {
                        "task": st.session_state.reflection1,
                        "tool": st.session_state.reflection2,
                        "usage": st.session_state.reflection3,
                        "date": timestamp
                    }
                    st.session_state.journal_entries.append(entry)
                    st.session_state.last_saved = timestamp
                    st.success("Journal entry saved successfully!")
                else:
                    st.warning("Please complete all fields before saving.")
    
    if st.session_state.journal_entries:
        st.subheader("Your Journal Entries")
        for idx, entry in enumerate(reversed(st.session_state.journal_entries)):
            with st.expander(f"Entry {len(st.session_state.journal_entries)-idx} - {entry['date']}"):
                st.markdown(f"""
                <div class="reflection-card">
                    <p><strong>Task:</strong> {entry['task']}</p>
                    <p><strong>Tool:</strong> {entry['tool']}</p>
                    <p><strong>Usage:</strong> {entry['usage']}</p>
                </div>
                """, unsafe_allow_html=True)


# --- Usage Habit Assessment ---
elif st.session_state.selected_module == "assessment":
    st.header("Usage Habit Assessment")
    st.markdown("Evaluate your patterns and habits when using AI for learning.")
    
    if not st.session_state.habit_questions:
        st.info("Generate questions to begin your assessment.")
        
        # Use sample issues (to avoid API problems)
        if st.button("Generate Assessment Questions"):
            # Locally generated sample issues
            sample_questions = [
                {
                    'text': "How often do you use AI tools for academic work?",
                    'options': [
                        "A. Never",
                        "B. Rarely (1-2 times per week)",
                        "C. Regularly (3-5 times per week)",
                        "D. Daily"
                    ]
                },
                {
                    'text': "Which type of tasks do you most commonly use AI for?",
                    'options': [
                        "A. Brainstorming ideas",
                        "B. Writing assistance",
                        "C. Research and information gathering",
                        "D. Problem solving and analysis"
                    ]
                },
                {
                    'text': "How do you feel about using AI for academic work?",
                    'options': [
                        "A. It's essential for my learning",
                        "B. It's helpful but I use it cautiously",
                        "C. I prefer traditional methods",
                        "D. I'm concerned about over-reliance"
                    ]
                },
                {
                    'text': "When using AI, how often do you verify the information provided?",
                    'options': [
                        "A. Always - I check multiple sources",
                        "B. Usually - for important information",
                        "C. Sometimes - if I have doubts",
                        "D. Rarely - I trust the AI's output"
                    ]
                },
                {
                    'text': "How has AI usage affected your learning process?",
                    'options': [
                        "A. Greatly improved efficiency",
                        "B. Some improvements with some concerns",
                        "C. Mixed results - helpful but distracting",
                        "D. Negative impact - reduced my own thinking"
                    ]
                }
            ]
            
            st.session_state.habit_questions = sample_questions
            st.rerun()
    
    else:
        with st.form("assessment_form"):
            st.write("**Please answer the following questions:**")
            
            for idx, question in enumerate(st.session_state.habit_questions):
                with st.container():
                    st.markdown(f"<div class='question-card'><strong>Question {idx+1}: {question['text']}</strong></div>", unsafe_allow_html=True)
                    
                    answer_key = f"q{idx}"
                    
                    # Extract option texts
                    options_display = []
                    for opt in question['options']:
                        if ". " in opt:
                            options_display.append(opt)
                        else:
                            option_letter = ['A', 'B', 'C', 'D'][len(options_display)]
                            options_display.append(f"{option_letter}. {opt}")
                    
                    # Store selected answer
                    selected_option = st.radio(
                        "Select your answer:",
                        options_display,
                        key=answer_key,
                        index=None,
                        label_visibility="collapsed"
                    )
                    
                    if selected_option:
                        st.session_state.user_answers[answer_key] = selected_option
            
            col1, col2 = st.columns(2)
            with col1:
                submitted = st.form_submit_button("Submit Assessment")
                if submitted:
                    unanswered = [k for k, v in st.session_state.user_answers.items() if not v]
                    if not unanswered:
                        st.success("✅ Assessment submitted successfully!")
                        
                        # Display results summary
                        with st.expander("View Your Responses"):
                            for idx, question in enumerate(st.session_state.habit_questions):
                                answer_key = f"q{idx}"
                                st.write(f"**Q{idx+1}: {question['text']}**")
                                st.write(f"Your answer: {st.session_state.user_answers.get(answer_key, 'Not answered')}")
                                st.write("---")
                    else:
                        st.warning(f"Please answer {len(unanswered)} remaining question(s).")
            
            with col2:
                if st.form_submit_button("🔄 Reset Assessment"):
                    st.session_state.habit_questions = []
                    st.session_state.user_answers = {}
                    st.rerun()


# --- Personal Usage Report ---
elif st.session_state.selected_module == "report":
    st.header("AI Usage Pattern Report")
    st.markdown("View your personalized feedback and usage insights.")
    
    # Journal Summary Section
    with st.container():
        st.subheader("Your Journal Entries Summary")
        if st.session_state.journal_entries:
            # Display the most recent journal entry
            latest_entry = st.session_state.journal_entries[-1]
            st.markdown(f"""
            <div class="report-section">
                <p><strong>Most Recent Entry:</strong> {latest_entry['date']}</p>
                <p><strong>Task:</strong> {latest_entry['task']}</p>
                <p><strong>Tool:</strong> {latest_entry['tool']}</p>
                <p><strong>Usage:</strong> {latest_entry['usage']}</p>
                <p><strong>Total Entries:</strong> {len(st.session_state.journal_entries)}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Optional: Show all entries in an expander
            with st.expander("View All Journal Entries"):
                for idx, entry in enumerate(st.session_state.journal_entries):
                    st.write(f"**Entry {idx+1} ({entry['date']}):**")
                    st.write(f"Task: {entry['task']}")
                    st.write(f"Tool: {entry['tool']}")
                    st.write(f"Usage: {entry['usage']}")
                    st.write("---")
        else:
            st.warning("No journal entries found. Complete the Usage Experience Journal first.")

    # Assessment Summary Section
    if st.session_state.habit_questions and st.session_state.habit_questions:
        st.subheader("Your Assessment Results")
        
        # Initialize scoring variables
        total_score = 0
        max_possible_score = 0
        answered_questions = 0
        
        # Display each question and its answer with scoring
        for idx, question in enumerate(st.session_state.habit_questions):
            answer_key = f"q{idx}"
            if answer_key in st.session_state.user_answers and st.session_state.user_answers[answer_key]:
                answer_text = st.session_state.user_answers[answer_key]
                option_letter = answer_text[0] if answer_text else ""
                
                # Calculate score based on question type and answer
                if "how often" in question['text'].lower() or "frequency" in question['text'].lower():
                    # Frequency questions: A=0, B=1, C=2, D=3 (more frequent = higher score)
                    score = ord(option_letter.upper()) - ord('A') if option_letter in ['A','B','C','D'] else 0
                elif "feel" in question['text'].lower() or "ethical" in question['text'].lower():
                    # Ethical questions: Reverse score (A=3, B=2, C=1, D=0)
                    score = 3 - (ord(option_letter.upper()) - ord('A')) if option_letter in ['A','B','C','D'] else 0
                elif "task" in question['text'].lower() or "use" in question['text'].lower():
                    # Usage type questions: All options score 1 (neutral)
                    score = 1
                else:
                    # Default scoring: Middle options score more (A=1, B=2, C=2, D=1)
                    score_map = {'A': 1, 'B': 2, 'C': 2, 'D': 1}
                    score = score_map.get(option_letter.upper(), 0)
                
                # Update totals
                total_score += score
                max_possible_score += 3  # Maximum score per question is 3
                answered_questions += 1
                
                # Display question with answer and score
                st.markdown(f"""
                <p><strong>{idx+1}. {question['text']}</strong><br>
                <em>Your answer:</em> {answer_text} (Score: {score}/3)</p>
                """, unsafe_allow_html=True)
        
        # Display overall assessment results
        if answered_questions > 0:
            percentage = (total_score / max_possible_score) * 100 if max_possible_score > 0 else 0
            
            st.markdown("---")
            
            # Display score metric
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                st.metric(
                    "Your AI Usage Score", 
                    f"{total_score}/{max_possible_score}"
                )
            with col2:
                st.metric(
                    "Percentage", 
                    f"{percentage:.1f}%"
                )
            
            # Contextual interpretation based on score
            st.markdown("### Interpretation")
            if percentage >= 80:
                st.success("**Highly Strategic AI User** - You leverage AI effectively while maintaining academic integrity. You demonstrate advanced understanding of when and how to use AI tools appropriately.")
            elif percentage >= 60:
                st.success("**Balanced AI Usage** - You have a good mix of practical AI use and ethical consideration. You're exploring AI's potential while maintaining critical thinking skills.")
            elif percentage >= 40:
                st.info("**Developing AI Skills** - You're growing more comfortable with AI tools, but there's room for more strategic and effective use. Consider exploring different applications.")
            elif percentage >= 20:
                st.warning("**Limited AI Engagement** - You could benefit from exploring more AI applications. Consider how AI might help with specific learning challenges.")
            else:
                st.warning("**Novice AI User** - Significant opportunity to learn about AI's educational potential. Start with simple tasks like brainstorming or research assistance.")
            
            # Additional insights based on patterns
            if percentage < 40:
                st.info("💡 **Tip**: Consider starting with AI tools for brainstorming or research to build confidence.")
            elif percentage > 70:
                st.info("💡 **Tip**: Share your effective AI usage strategies with peers who are just starting out.")
                
        else:
            st.warning("No answers submitted for the assessment. Please complete the assessment first.")
    elif st.session_state.habit_questions:
        st.info("Assessment questions are available but no answers have been submitted yet.")
    else:
        st.info("Complete the Usage Habit Assessment to see your results here.")

    # Generate AI-Powered Feedback Section
    st.markdown("---")
    st.subheader("Generate Personalized Feedback")
    
    # Check if there's enough data for analysis
    has_journal_data = len(st.session_state.journal_entries) > 0
    has_assessment_data = any(st.session_state.user_answers.values())
    
    if st.button("Generate Comprehensive Feedback", type="primary", use_container_width=True):
        if has_journal_data or has_assessment_data:
            try:
                # Configure the Gemini API
                genai.configure(api_key=st.secrets["google"]["api_key"])
                
                # Try different model names - use gemini-pro as it's more widely available
                try:
                    model = genai.GenerativeModel("gemini-pro")
                except:
                    # Fallback to other model names
                    try:
                        model = genai.GenerativeModel("models/gemini-pro")
                    except:
                        try:
                            model = genai.GenerativeModel("gemini-1.0-pro")
                        except Exception as model_error:
                            st.error(f"Model error: {model_error}")
                            # Use sample feedback if API fails
                            st.subheader("Personalized Feedback Report (Sample)")
                            st.markdown("""
                            **Usage Patterns Analysis:**
                            Based on your journal entries and assessment responses, you're exploring various AI tools for academic tasks.
                            
                            **Strengths in AI Utilization:**
                            - You're actively experimenting with different AI applications
                            - Showing awareness of ethical considerations
                            
                            **Areas for Improvement:**
                            - Consider more strategic integration of AI in your workflow
                            - Explore specific tools for different types of tasks
                            
                            **Recommended Strategies:**
                            1. Create a weekly plan for AI-assisted learning
                            2. Try different AI tools for specific purposes
                            3. Reflect on what works best for your learning style
                            
                            **Suggested Tools and Resources:**
                            - ChatGPT for brainstorming
                            - Grammarly for writing assistance
                            - Wolfram Alpha for computational tasks
                            """)
                            return
                
                # Prepare journal context for the prompt
                journal_context = "\n".join(
                    f"Entry {idx+1} ({entry['date']}):\nTask: {entry['task']}\nTool: {entry['tool']}\nUsage: {entry['usage']}\n---"
                    for idx, entry in enumerate(st.session_state.journal_entries[-5:])  # Limit to last 5 entries
                ) if has_journal_data else "No journal entries available"
                
                # Prepare assessment context for the prompt
                assessment_context = "\n".join(
                    f"Q{i+1}: {q['text']}\nA: {st.session_state.user_answers.get(f'q{i}', 'Not answered')}\n---"
                    for i, q in enumerate(st.session_state.habit_questions)
                    if f'q{i}' in st.session_state.user_answers
                ) if has_assessment_data else "No assessment answers available"
                
                # Create the prompt for the AI
                prompt = f"""
                Analyze this student's AI usage patterns and provide personalized feedback:
                
                JOURNAL ENTRIES (most recent):
                {journal_context}
                
                ASSESSMENT RESPONSES:
                {assessment_context}
                
                Please provide a comprehensive analysis with these sections:
                
                1. **Usage Patterns Analysis**
                   - Identify trends in how they use AI
                   - Note frequency and types of tasks
                
                2. **Strengths in AI Utilization**
                   - Highlight what they're doing well
                   - Note positive habits and approaches
                
                3. **Areas for Improvement**
                   - Suggest specific areas to develop
                   - Identify potential blind spots
                
                4. **Recommended Strategies**
                   - Provide 3-5 actionable recommendations
                   - Suggest specific next steps
                
                5. **Suggested Tools and Resources**
                   - Recommend specific AI tools for their needs
                   - Suggest learning resources
                
                Tone: Professional, encouraging, and constructive
                Length: Approximately 300-400 words
                Focus: On practical, actionable advice
                """
                
                with st.spinner("Analyzing your usage patterns and generating feedback..."):
                    response = model.generate_content(prompt)
                    
                    if response and response.text:
                        st.subheader("Personalized Feedback Report")
                        
                        # Display the feedback in a nicely formatted container
                        st.markdown(f"""
                        <div style="
                            background-color: #f8f9fa;
                            padding: 20px;
                            border-radius: 10px;
                            border-left: 5px solid #4CAF50;
                            margin: 20px 0;
                        ">
                        {response.text}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add download option
                        feedback_text = f"AI Usage Feedback Report\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{response.text}"
                        st.download_button(
                            label="📥 Download Feedback Report",
                            data=feedback_text,
                            file_name=f"ai_usage_feedback_{datetime.now().strftime('%Y%m%d')}.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("The AI model did not return any feedback. Please try again.")
                        
            except Exception as e:
                st.error(f"An error occurred while generating feedback: {str(e)}")
                st.info("""
                **Troubleshooting tips:**
                1. Ensure your API key is valid and has access to Gemini models
                2. Try updating the library: `pip install --upgrade google-generativeai`
                3. Check if the model name needs to be updated
                4. Consider using the sample feedback option below
                """)
                
                # Provide sample feedback as fallback
                if st.button("Show Sample Feedback Instead"):
                    st.subheader("Personalized Feedback Report (Sample)")
                    st.markdown("""
                    ### Usage Patterns Analysis
                    Based on your usage patterns, you're in the early stages of exploring AI tools for academic work. 
                    You're primarily using AI for basic tasks and are developing an understanding of how these tools can support your learning.
                    
                    ### Strengths in AI Utilization
                    - **Exploratory Mindset**: You're willing to try different AI tools and applications
                    - **Ethical Awareness**: You show consideration for responsible AI use
                    - **Task-Specific Applications**: You're beginning to match tools to specific learning needs
                    
                    ### Areas for Improvement
                    - **Integration Strategy**: Consider how AI can be more systematically integrated into your workflow
                    - **Advanced Features**: Explore beyond basic usage to discover more powerful features
                    - **Critical Evaluation**: Develop stronger skills in evaluating AI-generated content
                    
                    ### Recommended Strategies
                    1. **Create an AI Learning Plan**: Dedicate specific times each week to explore new AI tools
                    2. **Tool Specialization**: Identify 2-3 AI tools that work best for your specific subjects
                    3. **Peer Learning**: Join or create a study group focused on effective AI usage
                    4. **Reflection Practice**: Keep a weekly log of what AI strategies worked best
                    
                    ### Suggested Tools and Resources
                    - **For Writing**: Grammarly, Hemingway Editor, ChatGPT for brainstorming
                    - **For Research**: Consensus, Elicit, Google Scholar with AI assistance
                    - **For Coding**: GitHub Copilot, Replit, Codeium
                    - **Learning Resources**: Coursera's "AI for Everyone", edX AI courses, AI tool tutorials on YouTube
                    
                    **Next Steps**: Try one new AI tool this week and reflect on how it affected your productivity.
                    """)
        else:
            st.warning("Please complete at least one module (Journal or Assessment) before generating feedback.")
            
    # Optional: Add a refresh button
    if st.session_state.journal_entries or st.session_state.user_answers:
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Refresh Report Data"):
                st.rerun()
        with col2:
            if st.button("Clear All Data"):
                st.session_state.journal_entries = []
                st.session_state.habit_questions = []
                st.session_state.user_answers = {}
                st.success("All data cleared successfully!")
                st.rerun()

else:
    st.info("Please select a module from the options above to begin your reflection.")
