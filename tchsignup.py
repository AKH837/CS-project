import streamlit as st
# import mysql.connector
import os
import json

from streamlit_lottie import st_lottie

st.set_page_config(page_title="Teacher SignUp", page_icon="📖")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
logo = load_lottiefile("log.json")


# Connect to MySQL database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="askuha2659",
#     database="db1"
# )

# Create a cursor object
# cursor = mydb.cursor()


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
    margin-top: 0.01rem;
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


def navigate_to_hp():
    os.system("streamlit run hp.py")

with st.container():
    st.markdown("<h1 class='welcome-text'>Sign up as Teacher</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st_lottie(
            logo,
            height=200,
            width=200,
            key="lottie_animation09",
            loop=False,

        )
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
    email = st.text_input(
        "email",
        value="",
        placeholder="Enter your email id",
        help="Your email for the application",
        disabled=False,
    )
    #if username != "" and password != "" and email != "":
        #sql = "INSERT INTO sgn1 (username, password, email) VALUES (%s,%s,%s,%s)"
        #values = (username, password, email )
        #cursor.execute(sql, values)
    st.write("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Submit", use_container_width=True):
            st.success("User created successfully!")
            st.write("Welcome to LearnVid")
            #mydb.commit()
            if st.success:
                st.write("<br>", unsafe_allow_html=True)
                st.button("Continue", use_container_width=True, on_click=navigate_to_hp)
