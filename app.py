import streamlit as st
import pandas as pd
import numpy as np


st.title("최고의 수업, oss 개발에서 배운 Streamlit")
st.slider("-")
df = pd.DataFrame(np.random.randn(500,2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)
