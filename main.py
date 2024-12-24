import streamlit as st
import pandas as pd
import investpy as inv
import numpy as np
import yfinance as yf


def carregar_dados(empresas):
    #texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(empresas)
    df = dados_acao.history(period='1d', start='2024-01-01', end='2024-12-31')
    df = df["Close"]
    return df


#acoes = ['ITUB4.SA', 'PETR4.SA', 'VALE3.SA', 'BBDC4.SA', 'ABEV3.SA', 'B3SA3.SA', 'ITSA4.SA', 'PETR3.SA', 'BBAS3.SA', 'BBDC3.SA']

#dados = carregar_dados(acoes)

st.title('Histórico de cotação na Bolsa de Valores')
st.write('Aqui você pode visualizar o histórico de cotação de ações da bolsa de valores')
st.write('Para isso, você precisa informar o código da ação e a data de início e fim do período desejado')
st.write('O código da ação pode ser encontrado no site da bolsa de valores')
st.write('A data de início e fim do período deve ser informada no formato "aaaa-mm-dd"')
st.write('Exemplo: 2020-01-01 para 2020-12-31')

#st.text_input('Código da ação')
st.text_input('Data de início')
st.text_input('Data de fim')

st.button('Visualizar histórico')
st.write('Aqui está o histórico de cotação da ação selecionada')


'''
lista_acao = st.multiselect('Selecione a ação', dados.columns)
print(lista_acao)

if lista_acao:
    dados = dados[lista_acao]
    if len(lista_acao) == 1:
        acao_unica = lista_acao[0]
        dados = dados.rename(columns={acao_unica: "Close"})
    
        

#dados = carregar_dados(lista_acao)
#print(dados)

st.bar_chart(dados)

'''

data_inicial = "2024-01-01"
data_final = "2024-12-30"

nomes_acoes = inv.stocks.get_stocks(country='brazil')
nomes_acoes = sorted(nomes_acoes["symbol"])

print(nomes_acoes)


lista_acao = st.multiselect('Selecione as ações', nomes_acoes["symbol"])


#print(lista_acao)

nova_lista = ""
if len(lista_acao) > 0:
    for item in lista_acao:
        nova_lista = nova_lista + item+".SA "        
    dados = carregar_dados(nova_lista)
    st.write(dados)
    st.line_chart(dados)
    print(nova_lista)
else:
    print("Você não selecionou uma ou mais ações")





