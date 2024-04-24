import streamlit as st


my_file = “https://drive.google.com/file/d/1KC7NdwwmH6-Puit1MYxPoONxjkDejw1R/view?usp=sharing”
video_file = open(my_file, “rb”).read()
show_topics.video(video_file