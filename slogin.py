import streamlit as st
import mysql.connector
st.header("Student Sign-up")

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="askuha2659",
    database="db1"
)

# Create a cursor object


cursor = mydb.cursor()



    # Get user input from Streamlit form
username = st.text_input("Create username")
password = st.text_input("Create password", type="password")
email = st.text_input("Enter Your Email")
name = st.text_input("Name")


    # Insert user data into MySQL database
if username!= "" and password!="" and email!="":
    sql = "INSERT INTO sgn1 (username, password, email, name) VALUES (%s,%s,%s,%s)"
    values = (username, password, email, name)
    cursor.execute(sql, values)
submitted = st.button("Submit")

if submitted:
    st.success("User created successfully!")
    mydb.commit()







