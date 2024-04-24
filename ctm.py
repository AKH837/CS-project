import streamlit as st
import mysql.connector

from cts import mycursor

# Create an empty container
placeholder = st.empty()
db= mysql.connector.connect(
    host='Localhost',
    user='root',
    password='askuha2659',
    database='db1'
)

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    name= st.text_input("Name")
    username= st.text_input("username")
    submit = st.form_submit_button("Login")


if submit and email != "" and password != "":
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message

    mycursor.execute("Insert into tasin(Email,Username,Password,Name) VALUES(%s,%s,%s,%s)", (email,password,name,username))
    db.commit()
    st.success("Login successful")
else:
    st.warning("input")
