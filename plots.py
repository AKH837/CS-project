import streamlit as st
import pandas as pd
import numpy as np
import venv
import matplotlib.pyplot as plt
import altair as alt
data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)
chart= alt.Chart(data).mark_circle().encode(
    x='a',y='b'
)
st.map()
st.altair_chart(chart)
plt.scatter(data['a'],data['b'])
# st.pyplot()
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.image("A:\project\pythonProject\_117310488_16.jpg")
st.audio("A:\project\pythonProject\do I wanna know ringtone.mp3")
vid= st.video("https://drive.google.com/file/d/1KC7NdwwmH6-Puit1MYxPoONxjkDejw1R/view?usp=sharing")
st.download_button(vid)
st.button("Clickk")
if st.button("Click this"):
    st.write("HIII")
name = st.text_input("Name")
st.write(name)

add= st.text_area("Address")
st.write(add)

st.date_input("Select date")

st.time_input("Select time")

st.checkbox("Select me")
if st.checkbox("T&C",value= False): # False- checkbox wont be selected, true- checkbox will be selected by default
    st.button("Continue")
    st.write("Thank you")

st.radio("colours", ["Period 1","Period 2","Period 3"], index=0) # index shows us which option is selected by default
st.selectbox("colours", ["a","b","c"], index=0)
st.slider("Age", min_value=18,max_value=60,value=20)
st.number_input("number", step=1.0)
# st.file_uploader("file")
img= st.file_uploader("file")
st.video(img)

