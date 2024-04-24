import mysql.connector
import os
import streamlit as st
with st.container():
    st.markdown(
        "<div class='logo-container'><img src='https://cdn.pixabay.com/photo/2017/03/16/21/18/logo-2150297_960_720.png' class='logo'></div>",
        unsafe_allow_html=True)
    # st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='welcome-text'>Log-in to LearnVid</h1>", unsafe_allow_html=True)

    st.write("<br><br>", unsafe_allow_html=True)
mydb = mysql.connector.connect(
  host="Localhost",
  user="root",
  password="askuha2659",
  database="db1"
)

def check_credentials(username, password):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM sgn1 WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result is not None


# Add CSS styles to center components




def navigate_to_login():
    os.system("streamlit run hp.py")

def main():


    username = st.text_input("Enter your Username")
    password = st.text_input("Enter your Password", type="password")

    if st.button("Log-in"):
        if check_credentials(username, password):
            st.success("Login successful!")
            if st.success:
                st.button("Continue", on_click=navigate_to_login,)
            # Optionally, you can redirect the user to another page or perform additional actions
        else:
            st.error("Invalid username or password")


if __name__ == "__main__":
    main()




#---------------------------------------------------

import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
import requests
import json
import os

from streamlit_lottie import st_lottie




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

st.markdown(
    """
    <style>
    .st-emotion-cache-iiif1v.ef3psqc4 { visibility:hidden; }
    .st-emotion-cache-ztfqz8.ef3psqc5 { visibility:hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

css = """
<style>
div.stApp {
    background-color: #0f0f0f;
    color: #f0f0f0;
    text-align: center;
    font-weight: bold;
}
body {
    background-color: #0f0f0f;
    color: #f0f0f0;
    text-align: center;
    font-weight: bold;
}
.stButton > button {
    background-color: #4caf50;
    color: #ffffff;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
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
}
@keyframes text-flicker {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
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
    os.system("streamlit run login.py")


def navigate_to_signup():
    os.system("streamlit run signup.py")








    st.write("<br>", unsafe_allow_html=True)
    st.header("Featured Classes")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st_lottie(
            lottie_coding9,
            height=200,
            width=200,
            key="lottie_animation",

        )
        st.write("Class 9")
    with col2:
        st_lottie(
            lottie_coding10,
            height=200,
            width=200,
            key="lottie_animation1",

        )
        st.write("Class 10")
    with col3:
        st_lottie(
            lottie_coding11,
            height=200,
            width=200,
            key="lottie_animation2",

        )
        st.write("Class 11")

    with col4:
        st_lottie(
            lottie_coding12,
            height=200,
            width=200,
            key="lottie_animation3",

        )
        st.write("Class 12")
    with col5:
        st_lottie(
            lottie_coding,
            height=200,
            width=200,
            key="lottie_animation4",

        )
        st.write("Coming soon..")

    st.markdown("</div>", unsafe_allow_html=True)