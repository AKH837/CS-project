import streamlit as st
import pandas as pd
import numpy as np
import venv
import matplotlib.pyplot as plt
import altair as alt
import mysql.connector

db= mysql.connector.connect(
    host='Localhost',
    user='root',
    password='askuha2659',
    database='db1'
)
e=st.text_input("Email")
u=st.text_input("Username")
p=st.text_input("Password")
n=st.text_input("Name")



mycursor = db.cursor()

#mycursor.execute("Create table tab1 (name VARCHAR(50) NOT_NULL, age int, ID int PRIMARY KEY 1)")

mycursor.execute("Insert into tasin(Email,Username,Password,Name) VALUES(%s,%s,%s,%s)", (e,u,p,n))
submitted = st.button("Submit")  # Use a button to trigger actions

if submitted:
    db.commit()
else:
    db.rollback()



mycursor.execute("Select * from tasin")

for x in mycursor:
    print(x)

