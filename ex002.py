import streamlit as st
import pandas as pd

st.write("Criandouma tabela com DataFrame no Streamlit")

st.write(pd.DataFrame({
    "Coluna 1": [1, 2, 3, 4],
    "Coluna 2": [10, 20, 30, 40]
}))
