# IMPORTANDO MODULOS 

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import locale


# DEFININDO TAMANHO DA PÁGINA

st.markdown(
    """ 
    <style>
        .block-container { 
            max-width: 90%
            }
        
        </style>
    """, unsafe_allow_html=True
)

# IMPORTANDO A TABELA CSV COM OS DADOS

df = pd.read_csv(r'vendas_python/vendas_2023.csv')

# TITULO DA PÁGINA
st.title('Vendas 2023')

# SUBTITULO DA PÁGINA 
st.write('Uma analise de vendas de 2023')

# DEFININDO VÁRIAVEIS
faturamento_total = (sum(df['Valor da Venda']))

quant_vendas = df['Quantidade Vendida'].sum()

ticket_medio = str(round(faturamento_total/quant_vendas, 2)).replace('.',',')

faturamento_total = str(faturamento_total).replace('.',',')

# CALCULANDO O TOP5
df_group = df.groupby("Nome do Produto", as_index=False).sum() #AGRUPA POR NOME DE PRODUTO
top_5 = df_group.sort_values(by='Valor da Venda', ascending=False).head(5) # ORDENA POR VALOR DA VENDA, COLOCA EM ORDEM DECRESCENTE, E CERCA NOS TOP5

# GERANDO GRAFICOS 

# GRAFICO DE BARRAS, FATURAMENTO POR CIDADE
fig_faturamento = px.bar(df, x="Cidade da Venda", y="Valor da Venda", title="Faturamento por cidade", color_discrete_sequence=px.colors.qualitative.Alphabet)

# GRAFICO DE BARRAS, Quantidade vendida por Produto
fig_quant = px.bar(df, y="Nome do Produto", x="Quantidade Vendida", title="Quantidade vendida por Produto", color_discrete_sequence=px.colors.qualitative.Alphabet, orientation="h", height=500, labels=None)

# GRAFICO DE ROSCA, Faturamento por Categoria
fig_categoria = px.pie(df, names="Categoria do Produto", values="Valor da Venda", hole=0.3, title="Faturamento por Categoria", color_discrete_sequence=px.colors.qualitative.Alphabet)

# GRAFICO DE BARRAS, TOP 5 PRODUTOS MAIS VENDIDOS
top5_fig = px.bar(top_5, x='Nome do Produto', y='Valor da Venda', text="Nome do Produto", title='Top 5 Produtos', color_discrete_sequence=px.colors.qualitative.Alphabet)

# CRIAÇÃO DE CARTÕES COM INFORMAÇÕES

# CARTÃO TICKET MEDIO

# CARTÃO FATURAMENTO TOTAL

# DEFININDO NUMERO DE COLUNAS NA PÁGINA

col1, col2 = st.columns(2)

# DEFININDO POSIÇÃO DOS GRAFICOS NAS COLUNAS
with col1:
    st.metric(label="Ticket Médio", value=f'R$ {ticket_medio}')
    st.plotly_chart(top5_fig, use_container_width=True)
    st.plotly_chart(fig_faturamento,use_container_width=True)
    

with col2:
    st.metric(label="Faturamento Total", value=f'R$ {faturamento_total}')
    st.plotly_chart(fig_quant)
    st.plotly_chart(fig_categoria)

