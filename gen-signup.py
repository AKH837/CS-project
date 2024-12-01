import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
import requests
import json
import os

from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sign up", page_icon="📖")
def navigate_to_login():
    os.system("streamlit run hp.py")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
logo = load_lottiefile("log.json")
def navigate_to_teacher():
    os.system("streamlit run tchsignup.py")


def navigate_to_student():
    os.system("streamlit run stsignup.py")
css = """
<style>
div.stApp {
    text-align: center;
    font-weight: bold;
}
.stButton > button {
    background: linear-gradient(to right, #1e3a8a, #2563eb, #3b82f6);
    color: white;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
    border: 0;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}
.welcome-text {
    color: white;
    animation: text-flicker 2s linear infinite;
}
@keyframes text-flicker {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
}

</style>
"""
st.markdown(css, unsafe_allow_html=True)


with st.container():
    st.markdown("<h1 class='welcome-text'>Sign up to LearnVid</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st_lottie(
            logo,
            height=200,
            width=200,
            key="lottie_animation09",
            loop=False,

        )

    col1, col2 = st.columns(2)
    with col1:
        login_button = st.button("As Teacher", use_container_width=True, on_click=navigate_to_teacher)
        # Custom button size using CSS

    with col2:
        signup_button = st.button("As student", use_container_width=True, on_click=navigate_to_student)


