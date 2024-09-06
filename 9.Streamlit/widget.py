import streamlit as st
import pandas as pd

st.title("Streamlit GUI APP")

name=st.text_input("Please Enter you Name Here:")


age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")

options = ["LSTM", "RNN", "CNN", "YOLO"]
models = st.selectbox("Choose your models:", options)
st.write(f"You selected {models}.")

if name:
    st.write(f"Hello, {name}")



uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
