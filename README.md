# AI Study Buddy

> **Note:** This is currently a **prototype**, and platform development is in progress. Features and content may change as the project evolves.  
> **Prototype Link:** [https://ai-studybuddy.streamlit.app](https://ai-studybuddy.streamlit.app)

## Overview  
AI Study Buddy is a **web-based learning platform** that empowers students to develop **AI literacy** and **use AI responsibly in their learning process**. By combining **foundational AI knowledge** with **guided reflection on personal usage habits**, the platform helps students harness AI’s benefits strategically while supporting cognitive growth and fostering independent learning skills.

The platform is grounded in:  
- **Motivation Theories**  
- **AI Literacy Framework (Long & Magerko, 2020)**  
- **Piaget’s Cognitive Constructivism**  

Together, these theoretical foundations support students in balancing AI’s benefits with their own cognitive development.  

Reference: Long, D., & Magerko, B. (2020). What is AI literacy? competencies and design considerations. In Proceedings of the 2020 CHI conference on human factors in computing systems. https://doi.org/10.1145/3313831.3376727

---

## Features  
- 📖 **AI Literacy Modules** – Learn essential AI concepts and responsible usage strategies.  
- ✍️ **AI Usage Reflection** – Reflect on your personal AI usage and receive personalized feedback.  
- 🎯 **AI Challenges & Activities** – Engage in practical exercises to strengthen AI literacy.  
- 💬 **AI Community Forum** – Share insights, ask questions, and learn from peers.  
- ⚡ **Dynamic AI Support** – Integrates **Google Gemini 1.5 Flash API** to generate AI usage assessment questions and personalized advice.  

---

## Tech Stack  
- **Python**  
- **Streamlit** – for building a clean and interactive web interface  
- **Google Gemini 1.5 Flash API** – for dynamic question generation & personalized recommendations  

---

## Installation & Setup  

1. Clone this repository:  
   ```bash
   git clone https://github.com/jessiex115/AI-Study-Buddy.git
   cd AI-Study-Buddy
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   ```bash
   streamlit run Home.py
5. Open your browser and go to the local URL provided by Streamlit (usually http://localhost:8501).

---

Author
Developed by Jiaxin (Jessie) Xu
Email: jessie02115@gmail.com
