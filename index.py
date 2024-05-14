import streamlit as st
import pandas as pd
from services import call_get_api
from api import products_url, carts_url, users_url

st.set_page_config(page_title="Dummy API", page_icon=None, layout='wide', initial_sidebar_state='auto')

selected_page = st.sidebar.radio("Navigation", ["Products", "Carts", "Users"])
if selected_page == "Products":
    st.title('Products')
    st.write(products_url)
    data = call_get_api(products_url)
    df = pd.DataFrame(data['products'])
    st.dataframe(df, height=800)
elif selected_page == "Carts":
    st.title('Carts')
    data = call_get_api(carts_url)
    df = pd.DataFrame(data['carts'])
    st.dataframe(df, height=800)
elif selected_page == "Users":
    st.title('Users')
    data = call_get_api(users_url)
    df = pd.DataFrame(data['users'])
    st.dataframe(df, height=800)