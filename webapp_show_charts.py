import streamlit as st
import pandas as pd
import numpy as np

st.write("My charts")

chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns = ["A","B","C","D"]
)

st.line_chart(chart_data)
st.bar_chart(chart_data)