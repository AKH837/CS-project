import streamlit as st
import pandas as pd
import numpy as np
import venv
import matplotlib.pyplot as plt
import altair as alt
import time
data = {
    "num" :[x for x in range(1,11)],
    "sqr": [x**2 for x in range(1,11)],
}
rad= st.sidebar.radio("Navigation",["Home","About us"])
if rad == "Home":
    df = pd.DataFrame(data=data)

    col= st.sidebar.multiselect("Select",df.columns)

    plt.plot(df['num'],df[col])

    st.pyplot()
if rad== "About us":
    st.write("#about us")
    img = st.file_uploader("file")
    progress= st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    st.video(img)