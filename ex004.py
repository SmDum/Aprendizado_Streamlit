import pandas as pd
import numpy as np
import streamlit as st

dataframe = pd.DataFrame(
    np.random.randn(10, 20),  # Cria um DataFrame com 10 linhas e 20 colunas com números aleatórios
    columns=('Coluna %d' % i for i in range(20))  # Define os nomes de cada uma das colunas por Coluna 0, Coluna 1, ..., Coluna 19
)

st.table(dataframe) # Exibe o DataFrame no Streamlit como uma tabela