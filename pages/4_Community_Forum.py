import streamlit as st
from datetime import datetime

def community_forum():
    st.title("Community Forum")
    st.markdown("""
    Connect with peers to share experiences, ask questions, and discover AI resources.
    """)
    
    # Initialize session state for posts
    if 'forum_posts' not in st.session_state:
        st.session_state.forum_posts = []
        st.session_state.current_post = None
    
    # Create tabs for forum modules
    tab1, tab2, tab3 = st.tabs([
        "Share Insight & Experience", 
        "Ask & Answer Questions", 
        "AI Resources & Trends"
    ])
    
    with tab1:
        st.header("Share Insight & Experience")
        st.markdown("""
        **Share your AI learning experiences and strategies with the community**
        - Reflect on your AI usage
        - Share successful strategies
        - Discuss challenges and solutions
        """)
        
        with st.expander("Create New Post", expanded=False):
            with st.form("insight_form"):
                title = st.text_input("Post Title")
                content = st.text_area("Your Experience/Insight", height=200)
                categories = st.multiselect("Tags", 
                                          ["Writing", "Research", "Coding", 
                                           "Ethics", "Productivity", "Other"])
                submit = st.form_submit_button("Share Post")
                
                if submit:
                    if title and content:
                        new_post = {
                            "type": "insight",
                            "title": title,
                            "content": content,
                            "categories": categories,
                            "author": "Current User",
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "comments": []
                        }
                        st.session_state.forum_posts.append(new_post)
                        st.success("Post shared successfully!")
                    else:
                        st.warning("Please add a title and content")
        
        st.subheader("Recent Posts")
        for post in [p for p in st.session_state.forum_posts if p["type"] == "insight"]:
            with st.container():
                st.markdown(f"### {post['title']}")
                st.caption(f"Posted by {post['author']} on {post['date']} | Tags: {', '.join(post['categories'])}")
                st.markdown(post['content'])
                with st.expander(f"Comments ({len(post['comments'])} replies)"):
                    for comment in post['comments']:
                        st.markdown(f"{comment['author']}: {comment['content']}")
                    
                    with st.form(key=f"comment_form_{post['title']}"):
                        new_comment = st.text_input("Add a comment")
                        if st.form_submit_button("Post Comment") and new_comment:
                            post['comments'].append({
                                "author": "Current User",
                                "content": new_comment,
                                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                            })
                            st.rerun()
                st.markdown("---")
    
    with tab2:
        st.header("Ask & Answer Questions")
        st.markdown("""
        **Collaborate with peers to solve AI-related challenges**
        - Ask questions about AI tools
        - Share your knowledge by answering
        - Upvote helpful responses
        """)
        
        with st.expander("Ask New Question", expanded=False):
            with st.form("question_form"):
                title = st.text_input("Question Title")
                content = st.text_area("Detailed Question", height=200)
                tags = st.multiselect("Tags", 
                                    ["ChatGPT", "Grammarly", "Research", 
                                     "Coding", "Troubleshooting", "Other"])
                submit = st.form_submit_button("Post Question")
                
                if submit:
                    if title and content:
                        new_post = {
                            "type": "question",
                            "title": title,
                            "content": content,
                            "tags": tags,
                            "author": "Current User",
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "answers": [],
                            "votes": 0
                        }
                        st.session_state.forum_posts.append(new_post)
                        st.success("Question posted successfully!")
                    else:
                        st.warning("Please add a title and question details")
        
        st.subheader("Recent Questions")
        for post in [p for p in st.session_state.forum_posts if p["type"] == "question"]:
            with st.container():
                col1, col2 = st.columns([1, 10])
                with col1:
                    st.markdown(f"### {post['votes']}")
                    st.markdown("votes")
                    if st.button("Upvote", key=f"upvote_{post['title']}"):
                        post['votes'] += 1
                        st.rerun()
                
                with col2:
                    st.markdown(f"### {post['title']}")
                    st.caption(f"Asked by {post['author']} on {post['date']} | Tags: {', '.join(post['tags'])}")
                    st.markdown(post['content'])
                    
                    with st.expander(f"Answers ({len(post['answers'])})"):
                        for answer in post['answers']:
                            st.markdown(f"{answer['author']}: {answer['content']}")
                            st.caption(f"Posted on {answer['date']}")
                        
                        with st.form(key=f"answer_form_{post['title']}"):
                            new_answer = st.text_area("Your Answer", height=100)
                            if st.form_submit_button("Post Answer") and new_answer:
                                post['answers'].append({
                                    "author": "Current User",
                                    "content": new_answer,
                                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                                })
                                st.rerun()
                    st.markdown("---")
    
    with tab3:
        st.header("AI Resources & Trends")
        st.markdown("""
        **Discover and share valuable AI resources**
        - Share useful tools and tutorials
        - Discuss latest AI developments
        - Post about upcoming events
        """)
        
        with st.expander("Share New Resource", expanded=False):
            with st.form("resource_form"):
                resource_type = st.selectbox("Resource Type", 
                                           ["Article", "Tool", "Research Paper", 
                                            "Tutorial", "Event", "News", "Other"])
                title = st.text_input("Title")
                url = st.text_input("URL (optional)")
                description = st.text_area("Description", height=150)
                submit = st.form_submit_button("Share Resource")
                
                if submit:
                    if title and description:
                        new_post = {
                            "type": "resource",
                            "resource_type": resource_type,
                            "title": title,
                            "url": url,
                            "description": description,
                            "author": "Current User",
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "saves": 0
                        }
                        st.session_state.forum_posts.append(new_post)
                        st.success("Resource shared successfully!")
                    else:
                        st.warning("Please add a title and description")
        
        st.subheader("Recent Resources")
        for post in [p for p in st.session_state.forum_posts if p["type"] == "resource"]:
            with st.container():
                st.markdown(f"##### {post['resource_type'].upper()}")
                st.markdown(f"### {post['title']}")
                if post['url']:
                    st.markdown(f"[Visit Resource]({post['url']})")
                st.caption(f"Shared by {post['author']} on {post['date']} | {post['saves']} saves")
                st.markdown(post['description'])
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Save", key=f"save_{post['title']}"):
                        post['saves'] += 1
                        st.rerun()
                with col2:
                    if st.button("Discuss", key=f"discuss_{post['title']}"):
                        st.session_state.current_post = post
                        st.rerun()
                
                st.markdown("---")

def main():
    st.set_page_config(page_title="Community Forum", layout="wide")
    community_forum()

if __name__ == "__main__":
    main()