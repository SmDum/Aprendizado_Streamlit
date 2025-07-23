import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({
    'Primeira Coluna': [1, 2, 3, 4],
    'Segunda Coluna': [10, 20, 30, 40]
    })


option = st.selectbox(
    'Qual é o número que você mais gosta?',
    df['Primeira Coluna'])

'Você selecionou: ', option


add_selectbox = st.sidebar.selectbox(
    'Como você gostaria de ser contatado?',
    ('Email', 'Telefone', 'WhatsApp'))

add_slider =   st.sidebar.slider(
    'Selecione um intervalo de valores',
    0.0, 100.0, (25.0, 75.0))


coluna_esquerda, coluna_direita = st.columns(2)

coluna_esquerda.button('Clique aqui!')

with coluna_direita:
    chosen = st.radio(
        'Qual é o seu animal favorito?',
        ('Cachorro', 'Gato', 'Pássaro', 'Peixe'))
    st.write(f'Você escolheu: {chosen}')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteração {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)