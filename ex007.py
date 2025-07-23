import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('X')
st.write(x, ' ao quadrado é', x * x)

st.text_input("Digite seu nome", key="name")
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data