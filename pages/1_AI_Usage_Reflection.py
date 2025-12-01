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
# 修改你的代码，添加模型检查：

elif st.session_state.selected_module == "assessment":
    st.header("Usage Habit Assessment")
    st.markdown("Evaluate your patterns and habits when using AI for learning.")
    
    if not st.session_state.habit_questions:
        st.info("Generate questions to begin your assessment.")
        if st.button("Generate Assessment Questions"):
            try:
                # Configure API with your key
                genai.configure(api_key=st.secrets["google"]["api_key"])
                
                # 先检查可用的模型
                st.write("Checking available models...")
                available_models = []
                for model in genai.list_models():
                    if "generateContent" in model.supported_generation_methods:
                        available_models.append(model.name)
                        st.write(f"✓ {model.name}")
                
                if not available_models:
                    st.error("No models with generateContent found! Check your API key permissions.")
                    
                    # 尝试使用备用的text-bison模型（如果可用）
                    try:
                        # 尝试旧版API的模型名称
                        import requests
                        API_KEY = st.secrets["google"]["api_key"]
                        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
                        response = requests.get(url)
                        if response.status_code == 200:
                            models = response.json().get('models', [])
                            st.write("Available models from API:")
                            for model in models:
                                st.write(f"- {model.get('name')}")
                    except Exception as api_error:
                        st.write(f"API check error: {api_error}")
                    
                    return
                
                # 尝试不同的模型名称
                model_candidates = [
                    "gemini-pro",
                    "models/gemini-pro",
                    "gemini-1.0-pro",
                    "gemini-1.0-pro-001",
                    "text-bison-001",  # 旧版模型，可能仍然可用
                    "models/text-bison-001"
                ]
                
                selected_model = None
                for candidate in model_candidates:
                    if any(candidate in model for model in available_models):
                        selected_model = candidate
                        break
                
                if not selected_model:
                    # 使用第一个可用的模型
                    selected_model = available_models[0].split('/')[-1]  # 只取模型名称部分
                
                st.info(f"Using model: {selected_model}")
                
                # 创建模型实例
                try:
                    model = genai.GenerativeModel(selected_model)
                except:
                    # 如果失败，尝试带完整路径
                    if "models/" not in selected_model:
                        model = genai.GenerativeModel(f"models/{selected_model}")
                    else:
                        raise
                
                prompt = """Generate exactly 5 multiple-choice questions about AI usage habits for students. 
                Each question should have 4 options (A-D) and cover different aspects of AI usage including:
                - Frequency of use
                - Types of tasks
                - Ethical considerations
                - Learning effectiveness
                - Dependence on AI
                - Critical thinking development
                
                Format each question like this example:
                Question: How often do you use AI tools for academic work?
                A. Never
                B. Rarely (1-2 times per week)
                C. Regularly (3-5 times per week)
                D. Daily
                
                IMPORTANT: 
                1. Always start questions with "Question:"
                2. Options must start with A., B., C., D.
                3. Generate exactly 5 questions"""
                
                with st.spinner("Generating personalized questions..."):
                    response = model.generate_content(prompt)
                    
                    if response.text:
                        questions = []
                        current_question = {}
                        
                        # Parse the response
                        lines = response.text.strip().split('\n')
                        
                        for line in lines:
                            line = line.strip()
                            if line.startswith("Question:"):
                                if current_question:
                                    questions.append(current_question)
                                current_question = {
                                    'text': line.replace("Question:", "").strip(),
                                    'options': []
                                }
                            elif line and len(line) > 2 and line[0] in ['A', 'B', 'C', 'D'] and line[1] == '.':
                                current_question['options'].append(line)
                        
                        if current_question:
                            questions.append(current_question)
                        
                        # Ensure we have exactly 5 questions
                        if len(questions) > 5:
                            questions = questions[:5]
                        
                        # Validate each question has 4 options
                        valid_questions = []
                        for q in questions:
                            if q.get('text') and len(q.get('options', [])) >= 4:
                                valid_questions.append({
                                    'text': q['text'],
                                    'options': q['options'][:4]
                                })
                        
                        if len(valid_questions) >= 3:
                            st.session_state.habit_questions = valid_questions[:5]
                            st.rerun()
                        else:
                            st.error(f"Could not parse enough valid questions. Found {len(valid_questions)} questions.")
                            st.text_area("Model Response:", response.text, height=200)
                
            except Exception as e:
                st.error(f"Failed to generate questions: {str(e)}")
                st.info("""
                **Steps to resolve:**
                1. **Update library**: `pip install --upgrade google-generativeai`
                2. **Check API key**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
                3. **Ensure API is enabled**: You may need to enable the Gemini API
                4. **Regional restrictions**: Some models may not be available in all regions
                5. **Try Vertex AI**: If Gemini API doesn't work, consider using Vertex AI
                """)

# --- Personal Usage Report ---
elif st.session_state.selected_module == "report":
    st.header("AI Usage Pattern Report")
    st.markdown("View your personalized feedback and usage insights.")
    
    # Journal Summary Section
    with st.container():
        st.subheader("Your Journal Entries Summary")
        if st.session_state.journal_entries:
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
        else:
            st.warning("No journal entries found. Complete the Usage Experience Journal first.")

    # Assessment Summary Section
    if st.session_state.habit_questions:
        st.subheader("Your Assessment Results")
        
        # Initialize scoring
        total_score = 0
        max_possible_score = 0
        answered_questions = 0
        
        # Display questions and answers
        for idx, question in enumerate(st.session_state.habit_questions):
            answer_key = f"q{idx}"
            if answer_key in st.session_state.user_answers and st.session_state.user_answers[answer_key]:
                answer_text = st.session_state.user_answers[answer_key]
                option_letter = answer_text[0] if answer_text else ""
                
                # Context-aware scoring
                if "how often" in question['text'].lower() or "frequency" in question['text'].lower():
                    # Frequency questions: A=0, B=1, C=2, D=3
                    score = ord(option_letter.upper()) - ord('A') if option_letter in ['A','B','C','D'] else 0
                elif "feel" in question['text'].lower() or "ethical" in question['text'].lower():
                    # Ethical questions: Reverse score (A=3, B=2, C=1, D=0)
                    score = 3 - (ord(option_letter.upper()) - ord('A')) if option_letter in ['A','B','C','D'] else 0
                elif "task" in question['text'].lower() or "use" in question['text'].lower():
                    # Usage type questions: All options score 1 (neutral)
                    score = 1
                else:
                    # Default scoring: Middle options score more (A=1, B=2, C=2, D=1)
                    score_map = {'A':1, 'B':2, 'C':2, 'D':1}
                    score = score_map.get(option_letter.upper(), 0)
                
                total_score += score
                max_possible_score += 3  # max score per question
                answered_questions += 1
                
                st.markdown(f"""
                <p><strong>{idx+1}. {question['text']}</strong><br>
                <em>Your answer:</em> {answer_text} (Score: {score}/3)</p>
                """, unsafe_allow_html=True)
        
        if answered_questions > 0:
            percentage = (total_score / max_possible_score) * 100
            
            st.markdown("---")
            st.metric("Your AI Usage Score", 
                     f"{total_score}/{max_possible_score}",
                     f"{percentage:.1f}%")
            
            # Contextual interpretation
            if percentage >= 80:
                st.success("Highly strategic AI user - You leverage AI effectively while maintaining academic integrity")
            elif percentage >= 60:
                st.success("Balanced AI usage - Good mix of practical use and ethical consideration")
            elif percentage >= 40:
                st.info("Developing AI skills - Growing comfort with AI tools, room for more strategic use")
            elif percentage >= 20:
                st.warning("Limited AI engagement - Could benefit from exploring more applications")
            else:
                st.warning("Novice AI user - Significant opportunity to learn about AI's educational potential")
        else:
            st.warning("No answers submitted for assessment")
    
    # Generate Feedback Section
    if st.button("Generate Comprehensive Feedback", type="primary"):
        if st.session_state.journal_entries or st.session_state.habit_questions:
            try:
                genai.configure(api_key=st.secrets["google"]["api_key"])
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                journal_context = "\n".join(
                    f"Entry {idx+1} ({entry['date']}): Task: {entry['task']}, Tool: {entry['tool']}, Usage: {entry['usage']}"
                    for idx, entry in enumerate(st.session_state.journal_entries)
                ) if st.session_state.journal_entries else "No journal entries available"
                
                assessment_context = "\n".join(
                    f"Q: {q['text']}\nA: {st.session_state.user_answers.get(f'q{i}', 'Not answered')}"
                    for i, q in enumerate(st.session_state.habit_questions)
                ) if st.session_state.habit_questions else "No assessment answers available"
                
                prompt = f"""
                Based on the following user data, provide a comprehensive AI usage analysis:
                
                JOURNAL ENTRIES:
                {journal_context}
                
                ASSESSMENT ANSWERS:
                {assessment_context}
                
                Please structure your response with these sections:
                1. Usage Patterns Analysis
                2. Strengths in AI Utilization
                3. Areas for Improvement
                4. Recommended Strategies
                5. Suggested Tools and Resources
                
                Keep the tone professional yet accessible, and provide specific, actionable recommendations.
                """
                
                with st.spinner("Analyzing your usage patterns..."):
                    response = model.generate_content(prompt)
                    if response.text:
                        st.subheader("Personalized Feedback Report")
                        st.markdown(response.text)
                    else:
                        st.error("Could not generate feedback. Please try again.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please complete at least one module (Journal or Assessment) before generating feedback.")

else:
    st.info("Please select a module from the options above to begin your reflection.")
