import mysql.connector
import os
import streamlit as st

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
centered_style = """
<style>
    .centered {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
"""

# Display the centered style
st.markdown(centered_style, unsafe_allow_html=True)

def navigate_to_login():
    os.system("streamlit run hp.py")

def main():
    # Center the components
    with st.container():
        st.markdown('<div class="centered">', unsafe_allow_html=True)
        st.write('<h1>Login to LEARNVID</h1>', unsafe_allow_html=True)

        username = st.text_input("Enter your Username", key="username")
        password = st.text_input("Enter your Password", type="password", key="password")

        if st.button("Log-in", key="login_button"):
            if check_credentials(username, password):
                st.success("Login successful!")
                if st.success:
                    st.button("Continue", on_click=navigate_to_login)
            else:
                st.error("Invalid username or password")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "_main_":
    main()