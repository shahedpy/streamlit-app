import streamlit as st
import pandas as pd
import requests
from api_urls import api_urls

def call_api_and_display(url, title):
    st.title(title)
    st.write(url)
    with st.spinner(f'Loading {title}...'):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data.get(title.lower(), []))
            st.dataframe(df, height=800, hide_index=True)
        else:
            st.error(f"Failed to fetch {title} data.")


st.set_page_config(page_title="Dummy API", page_icon=None, layout='wide', initial_sidebar_state='auto') # noqa

selected_page = st.sidebar.radio("Navigation", ["Products", "Carts", "Users"])

if selected_page == "Products":
    call_api_and_display(api_urls['products'], "Products")
elif selected_page == "Carts":
    call_api_and_display(api_urls['carts'], "Carts")
elif selected_page == "Users":
    call_api_and_display(api_urls['users'], "Users")
