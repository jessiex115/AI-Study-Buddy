import streamlit as st

def about_page():
    st.title("About AI Study Buddy")
    st.markdown("---")
    
    # First paragraph
    st.markdown("""
    There is a growing concern about balancing AI's involvement in learning with cognitive development. 
    Some students' limited understanding and irresponsible usage of AI lead to their overreliance on AI. 
    Therefore, students not only need to be equipped with essential knowledge of AI, but also require 
    external guidance on integrating AI into their learning process. These two factors together help 
    maximize AI's benefits in learning while maintaining students' cognitive growth and independent 
    learning ability development.
    """)
    
    st.markdown("---")
    
    # Platform description
    st.markdown("""
    **AI Study Buddy** is a web-based learning platform, it is designed to address AI overreliance in 
    learning and enhance students' AI literacy. Grounded in Motivation theories, the AI Literacy 
    Framework by Long & Magerko (2020), and Piaget's Cognitive Constructivism theory, the platform focuses on teaching 
    students essential AI knowledge and strategic utilization. It aims to help achieve a balance between 
    leveraging AI's benefits for learning and sustaining essential cognitive development. The platform 
    is open to all students, students of any major, grade, or academic level are welcome to use it to 
    learn about AI to meet their individual learning needs.
    """)
    
    st.markdown("---")
    
    # Reference section
    st.markdown("### Reference")
    st.markdown("""
    Long, D., & Magerko, B. (2020). What is AI literacy? competencies and design considerations. 
    In Proceedings of the 2020 CHI conference on human factors in computing systems. 
    https://doi.org/10.1145/3313831.3376727
    """)

def main():
    st.set_page_config(page_title="About AI Study Buddy", layout="wide")
    about_page()

if __name__ == "__main__":
    main()
