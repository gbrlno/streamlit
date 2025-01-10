import streamlit as st
import pandas as pd
import numpy as np

st.write("My charts")

nNumOfDatapoints = 20
strNumOfDatapoints = st.text_input("Number of datapoints")

if strNumOfDatapoints:
    nNumOfDatapoints = int(strNumOfDatapoints)

chart_data = pd.DataFrame(
    np.random.randn(nNumOfDatapoints, 4),
    columns = ["A","B","C","D"]
)

st.line_chart(chart_data)
st.bar_chart(chart_data)