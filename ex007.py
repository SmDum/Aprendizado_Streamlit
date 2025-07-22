import streamlit as st

x = st.slider('X')
st.write(x, ' ao quadrado é', x * x)

st.text_input("Digite seu nome", key="name")
st.session_state.name