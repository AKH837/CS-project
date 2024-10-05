#Absolute main page of the project
import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
import requests
import json
import os

from streamlit_lottie import st_lottie

# Set the page configuration
st.set_page_config(page_title="LearnVid", page_icon="📖", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding11 = load_lottiefile("11.json")
lottie_coding12 = load_lottiefile("12.json")
lottie_coding10 = load_lottiefile("10.json")
lottie_coding9 = load_lottiefile("9.json")
lottie_coding = load_lottiefile("cmg sn.json")
logo = load_lottiefile("log.json")

# Hide the hamburger menu and footer
st.markdown(
    """
    <style>
    .st-emotion-cache-iiif1v.ef3psqc4 { visibility:hidden; }
    .st-emotion-cache-ztfqz8.ef3psqc5 { visibility:hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define custom CSS styles
css = """
<style>
body {


    text-align: center;
    font-weight: bold;
}
.stButton > button {
    background: linear-gradient(to right, #6366f1, #a855f7, #ec4899);
    color: white;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
    border: 0;
}
.stButton > button:hover {
    background-color: #388e3c;
}
.logo-container {
    display: flex;
    justify-content: center;
    margin-top: -12px;
}
.logo {
    max-width: 200px;
    animation: spin 5s linear infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.welcome-text {
    animation: text-flicker 2s linear infinite;
    color: white;
}
@keyframes text-flicker {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
}
.fc {
    color: white;
}
.cln {
    color: white;
}
.clt {
    color: white;
}
.cle {
    color: white;
}
.cmg {
    color: white;
}
.cltw {
    color: white;
}
.typewriter {
    overflow: hidden;
    white-space: nowrap;
    margin: 0 auto;
    width: 0;
    animation: typing 3s steps(30, end) forwards, blink 0.5s infinite alternate;
    color: grey;
}
@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink {
    50% { border-color: transparent; }
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


def navigate_to_login():
    os.system("streamlit run student-login.py")


def navigate_to_signup():
    os.system("streamlit run gen-signup.py")


with st.container():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col3:
        st_lottie(
            logo,
            height=200,
            width=200,
            key="lottie_animation09",
            loop=False
        )
    st.markdown("<h1 class='welcome-text'>Welcome to LearnVid</h1>", unsafe_allow_html=True)

    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 class='typewriter'>Get access to all your missed lectures from anywhere, anytime.</h3>",
                unsafe_allow_html=True)

    # Sign-in and log-in buttons
    col1, col2 = st.columns(2)
    with col1:
        login_button = st.button("Log-in", use_container_width=True, on_click=navigate_to_login)
    with col2:
        signup_button = st.button("Sign-up", use_container_width=True, on_click=navigate_to_signup)

    # Dummy content for showcasing the layout
    st.write("<br><br>", unsafe_allow_html=True)
    st.write("<h2 class='fc'>Featured Classes</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st_lottie(
            lottie_coding9,
            height=200,
            width=200,
            key="lottie_animation",
        )
        st.write("<h5 class='cln'>Class 9</h2>", unsafe_allow_html=True)
    with col2:
        st_lottie(
            lottie_coding10,
            height=200,
            width=200,
            key="lottie_animation1",
        )
        st.write("<h5 class='clt'>Class 10</h2>", unsafe_allow_html=True)

    with col3:
        st_lottie(
            lottie_coding11,
            height=200,
            width=200,
            key="lottie_animation2",
        )
        st.write("<h5 class='cle'>Class 11</h2>", unsafe_allow_html=True)
    with col4:
        st_lottie(
            lottie_coding12,
            height=200,
            width=200,
            key="lottie_animation3",
        )
        st.write("<h5 class='cltw'>Class 12</h2>", unsafe_allow_html=True)
    with col5:
        st_lottie(
            lottie_coding,
            height=200,
            width=200,
            key="lottie_animation4",
        )
        st.write("<h5 class='cmg'>Coming Soon</h2>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
