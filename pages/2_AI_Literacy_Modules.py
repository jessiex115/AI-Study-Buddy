import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Literacy Modules",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .module-btn {
        transition: all 0.3s ease;
        margin: 0.25rem 0;
    }
    .module-btn:hover {
        transform: scale(1.02);
    }
    .checklist-item {
        margin-bottom: 0.5rem;
    }
    .resource-card {
        padding: 1rem;
        border-radius: 8px;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
    }
    .active-module {
        border-left: 4px solid #1e88e5;
        padding-left: 1rem;
    }
    .button-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = {
        "module1": [False, False, False],
        "module2": [False, False, False],
        "module3": [False, False, False],
        "module4": [False, False, False]
    }

# Main Content Area
st.title("AI Literacy Learning Modules")
st.markdown("Develop essential skills for interacting with artificial intelligence technologies.")
st.markdown("---")

# Module buttons in main content
st.markdown("### Select a Learning Module")
button_cols = st.columns(4)
module_names = [
    "Conceptual Understanding",
    "AI Ethics",
    "Critical Thinking",
    "Using AI for Learning"
]

for i, col in enumerate(button_cols):
    with col:
        if st.button(
            module_names[i],
            key=f"module{i+1}",
            help=f"Click to view {module_names[i]} module",
            use_container_width=True
        ):
            st.session_state.selected_module = f"module{i+1}"

st.markdown("---")

# Module content display
def render_module(title, content, resources, checklist, module_key):
    st.header(title)
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(content)
        
        with st.expander("Learning Resources", expanded=True):
            for resource in resources:
                st.markdown(f"""
                <div class="resource-card">
                    <h4>{resource['title']}</h4>
                    <p>{resource['description']}</p>
                    {f"<a href='{resource['link']}' target='_blank'>Resource will be here!</a>" if 'link' in resource else ""}
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Your Progress")
        for i, item in enumerate(checklist):
            key = f"{module_key}_task_{i}"
            st.session_state.completed_tasks[module_key][i] = st.checkbox(
                item, 
                value=st.session_state.completed_tasks[module_key][i],
                key=key,
                label_visibility="visible"
            )
        
        completion = sum(st.session_state.completed_tasks[module_key])/len(checklist)
        st.metric("Completion", f"{int(completion*100)}%")

if st.session_state.selected_module == "module1":
    render_module(
        "Module 1: Conceptual Understanding",
        """
        Build foundational knowledge about artificial intelligence:
        - **What is AI?** Explore definitions, recognition, and applications
        - **Machine Learning** How systems learn from data
        - **NLP Fundamentals** How computers process human language
        - **Algorithmic Decision Making** Understanding AI choices
        """,
        [
            {"title": "Introductory Video", "description": "5 min overview of key concepts", "link": "#"},
            {"title": "Interactive Concept Map", "description": "Visualize AI relationships", "link": "#"},
            {"title": "Knowledge Check", "description": "Test your understanding", "link": "#"}
        ],
        [
            "Watch introductory video",
            "Review concept map",
            "Complete knowledge check"
        ],
        "module1"
    )

elif st.session_state.selected_module == "module2":
    render_module(
        "Module 2: AI Ethics",
        """
        Examine the ethical dimensions of AI systems:
        - **Privacy Concerns** Data collection and surveillance
        - **Misinformation** AI exacerbates misinformation and fake news
        - **Bias in Algorithms** How prejudice enters systems
        - **Educational Ethics** Using AI responsibly in education
        """,
        [
            {"title": "Ethical Framework Video", "description": "Approaches to AI ethics", "link": "#"},
            {"title": "Case Studies", "description": "Real-world ethical dilemmas", "link": "#"},
            {"title": "Discussion Forum", "description": "Share your perspectives", "link": "#"}
        ],
        [
            "Watch ethics video",
            "Analyze 3 case studies",
            "Participate in forum"
        ],
        "module2"
    )

elif st.session_state.selected_module == "module3":
    render_module(
        "Module 3: Critical Thinking",
        """
        Develop skills to evaluate AI outputs critically:
        - **Verifying Accuracy** Fact-checking AI responses
        - **Identifying Bias** Recognizing skewed perspectives
        - **Prompt Engineering** Crafting effective queries
        """,
        [
            {"title": "Critical Analysis Video", "description": "Techniques for evaluation", "link": "#"},
            {"title": "Bias Detection Exercise", "description": "Practice identifying issues", "link": "#"},
            {"title": "Prompt Workshop", "description": "Improve your queries", "link": "#"}
        ],
        [
            "Watch analysis video",
            "Complete bias exercise",
            "Participate in prompt workshop"
        ],
        "module3"
    )

elif st.session_state.selected_module == "module4":
    render_module(
        "Module 4: Using AI for Learning",
        """
        Strategically integrate AI into your learning process:
        - **Goal Setting** Defining clear learning objectives
        - **Independent Practice** Building skills before using AI
        - **Reflective Practice** Evaluating AI's impact on learning
        
        **Featured Tools:**
        - **ChatGPT** for n
        - **Google Gemini** for problem-solving
        - **Claude** for coding
        """,
        [
            {"title": "Tool Tutorials", "description": "Guides for popular AI tools", "link": "#"},
            {"title": "Learning Plan Template", "description": "Structure your AI use", "link": "#"},
            {"title": "Have a try on the AI Challenges & Activities section!", "description": "Hands-on activities", "link": "#"}
        ],
        [
            "Complete tool tutorials",
            "Create learning plan",
            "AI Challenges & Activities"
        ],
        "module4"
    )

else:
    st.info("Select a module from the options above to begin learning.")
    st.markdown("### Module Overview")
    st.markdown("""
    - **Conceptual Understanding**: Build foundational knowledge
    - **AI Ethics**: Examine responsible use
    - **Critical Thinking**: Evaluate AI outputs
    - **Using AI for Learning**: Strategic integration
    """)
