import mysql.connector
import streamlit as st
db= mysql.connector.connect(
    host='Localhost',
    user='root',
    password='askuha2659',
    database='db1'
)

mycursor = db.cursor()
mycursor.execute("CREATE TABLE sgn1(username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,Name VARCHAR(255),id INT AUTO_INCREMENT PRIMARY KEY);")




mycursor.execute("Select * from sgn1")

for x in mycursor:
    print(x)