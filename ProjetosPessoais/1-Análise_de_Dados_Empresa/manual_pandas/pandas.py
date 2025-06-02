# Importar Bibliotecas

import pandas as pd
import streamlit as st
import plotly.express as px

# Setar a págna para prencher completa.
st.set_page_config(layout="wide")

# Ler o arquivo da empresa.
df = pd.read_csv('assets/company_transactions.csv')

# Descartar a coluna inútil "Id de Transações"
df = df.drop(columns="Transaction_ID")

# Transformar a coluna da planilha 'df' em datas.
df["Date"] = pd.to_datetime(df["Date"])

# Filtrar colunas por ordem de data
df = df.sort_values("Date")

# Função para criar nova coluna [Month] em que conterá somente o ano e o mês.
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma caixa de seleção na lateral para poder escolher qual mês visualizar.
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Criar uma nova variável para filtrar com base no mês, de acordo com o selectbox selecionada.
df_filtered = df[df["Month"] == month]

# Criar colunas para armazenar novas informações no layout.
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Nova variável para armazenar um gráfico de barras do Faturamento por dia.
fig_cat = px.bar(df, x="Transaction_Amount", y="Category", title = "Faturamento por Categoria", orientation="h")
col1.plotly_chart(fig_cat)

fig_date = px.bar(df, x="Month", y="Transaction_Amount", title = "Faturamento por Mês")
col2.plotly_chart(fig_date)

