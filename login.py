import os
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
st.set_page_config(page_title="Login", page_icon="📖",)

# import mysql.connector
# mydb = mysql.connector.connect(
#     host="Localhost",
#     user="root",
#     password="askuha2659",
#     database="db1"
# )

# def check_credentials(username, password):
#     mycursor = mydb.cursor()
#     sql = "SELECT * FROM sgn1 WHERE username = %s AND password = %s"
#     val = (username, password)
#     mycursor.execute(sql, val)
#     result = mycursor.fetchone()
#     return result is not None
def navigate_to_login():
    os.system("streamlit run hp.py")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
logo = load_lottiefile("log.json")

css = """
<style>
div.stApp {
    text-align: center;
    font-weight: bold;
}



.pw {
    color: white;
    margin-bottom: 0.2rem;
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

.us {
    color: white;
    margin-bottom: 0.2rem;
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
    st.markdown("<h1 class='welcome-text'>Log-in to LearnVid</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st_lottie(
            logo,
            height=200,
            width=200,
            key="lottie_animation09",
            loop=False,


        )



# Add CSS styles to center components
    username = st.text_input(
     "Username",
     value="",
     placeholder="Enter your username",
     help="Your username for the application",
     disabled=False,
     )
    password = st.text_input(
     "Password",
     value="",
     type="password",
     placeholder="Enter your password",
     help="Your password for the application",
     disabled=False,
    )
    st.write("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
     if st.button("Log-in",use_container_width=True):
        # if check_credentials(username, password):
       #     st.success("Login successful!")
       #     if st.success:
       #          st.button("Continue", on_click=navigate_to_login)
       # else:
        st.error("Invalid username or password")

