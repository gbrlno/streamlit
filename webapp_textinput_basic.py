import streamlit as st

favfood = st.text_input("What is your favorite food?")

st.write(f"You said your favorite food is {favfood}")