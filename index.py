import streamlit as st
import pandas as pd
from services import call_get_api
from api import products_url


st.title('Products')

data = call_get_api(products_url)

df = pd.DataFrame(data['products'])

st.dataframe(df, height=800)
