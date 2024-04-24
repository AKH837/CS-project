import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
import requests
import json
import os

from streamlit_lottie import st_lottie

st.set_page_config(page_title="LearnVid", page_icon="📖", layout="wide")


def navigate_to_teacher():
    os.system("streamlit run slogin.py")


def navigate_to_student():
    os.system("streamlit run signup.py")

col1, col2 = st.columns(2)
with col1:
        login_button = st.button("Teacher sign-in", use_container_width=True, on_click=navigate_to_teacher)
with col2:
        signup_button = st.button("Student sign-up", use_container_width=True, on_click=navigate_to_student)