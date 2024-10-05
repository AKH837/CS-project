import streamlit as st
import mysql.connector
import os
import json
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(page_title="Student SignUp", page_icon="📖")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


logo = load_lottiefile("log.json")

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="askuha2659",
    database="test"
)

# Create a cursor object
cursor = mydb.cursor()

# Custom CSS for styling
css = """
<style>
div.stApp {
    text-align: center;
    font-weight: bold;
}

.pw, .us {
    color: white;
    margin-bottom: 0.2rem;
}

.stButton > button {
    background: linear-gradient(to right, #009eff, #0078fa , #0032fa );
    color: white;
    font-weight: bold;
    border-radius: 20px;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
    border: 0;
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

.box {
    background-color: #f1f1f1;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 25px;
    text-align: center;
}

</style>
"""
st.markdown(css, unsafe_allow_html=True)


# Function for page navigation
def navigate_to_hp9():
    os.system("streamlit run Home9.py")

def navigate_to_hp10():
    os.system("streamlit run Home10.py")

def navigate_to_hp11():
    os.system("streamlit run Home11.py")


def navigate_to_hp12():
    os.system("streamlit run Home12.py")


# Main content in a styled box
with st.container():

    st.markdown("<h1 class='welcome-text'>Sign up as Student</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st_lottie(
            logo,
            height=200,
            width=200,
            key="lottie_animation09",
            loop=False
        )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    name = st.text_input("Name")

    classes = [9, 10, 11, 12]
    grade = st.selectbox("Select your class:", classes)

    st.markdown('</div>', unsafe_allow_html=True)  # End of the box

# Submit button and form handling
if st.button("Submit", use_container_width=True):
    if username == "" or password == "" or email == "" or name == "":
        st.warning("Enter credentials!")

    else:
        sql = "INSERT INTO test1 (username, password, email, name, grade) VALUES (%s, %s, %s, %s, %s)"
        values = (username, password, email, name, grade)
        cursor.execute(sql, values)
        mydb.commit()

        st.write("<br>", unsafe_allow_html=True)
        st.success("User created successfully!")
        st.write("Welcome to LearnVid")
        st.write("<br>", unsafe_allow_html=True)

        # Redirect to different pages based on grade
        if grade == 9:
            st.button("Continue to Dashboard", use_container_width=False, on_click=navigate_to_hp9)
        elif grade == 10:
            st.button("Continue to Dashboard", use_container_width=False, on_click=navigate_to_hp10)
        elif grade == 11:
            st.button("Continue to Dashboard", use_container_width=False, on_click=navigate_to_hp11)
        elif grade == 12:
            st.button("Continue to Dashboard", use_container_width=False, on_click=navigate_to_hp12)
