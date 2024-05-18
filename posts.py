import streamlit as st
import requests

posts_url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(posts_url)
if response.status_code != 200:
    st.error("Failed to fetch posts")
    st.stop()

posts_data = response.json()

def display_post_details(post_id):
    post_url = f"{posts_url}/{post_id}"
    post_response = requests.get(post_url)
    if post_response.status_code != 200:
        st.error("Failed to fetch post details")
        st.stop()

    post = post_response.json()
    st.write(f"### {post['title']}")
    st.write(post['body'])
    st.write("---")

post_id = st.query_params.get("post_id", [None])[0]

if post_id:
    display_post_details(post_id)
    st.button("Back to Posts")
else:
    st.title("Posts")
    for post in posts_data:
        post_url = f"/?post_id={post['id']}"
        st.write(f"## [{post['title']}]({post_url})")
        st.write(post['body'])
        st.write('---')
