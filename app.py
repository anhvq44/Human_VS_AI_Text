import streamlit as st

from home_page import home
from predict_page import predict

st.set_page_config(
    page_title="Human VS AI Generated Text",
    layout="centered",
    initial_sidebar_state="expanded"
)

pg = st.navigation([home, predict])

