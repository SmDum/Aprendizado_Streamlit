import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Primeira Coluna': [1, 2, 3, 4],
    'Segunda Coluna': [10, 20, 30, 40]
})

df 

'''
    Qualquer variável sozinha em que tenha um DataFrame,
    será exibida como uma tabela no Streamlit.
'''

