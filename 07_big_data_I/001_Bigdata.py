# Programadora: Rafaela Barezi
# Data:18/06/2023
# Confirmação da importação dos pacotes e exibição de versão

import seaborn as sb
import plotly as plt
import pandas as pd
import yfinance as yf

print("\nversão yfinance:")
print(yf.__version__)
print("versão pandas:")
print(pd.__version__)
print("versão plotly:")
print(plt.__version__)
print("versão seaborn:")
print(sb.__version__, "\n")

# DF = Data frame é como se fosse uma tabela, neste caso importaremos uma tabela da bolsa de valores com dados da Petrobras:

df = yf.download("PETR3.SA", start="2019-11-01",
                 end="2020-06-01", group_by="ticker")

# O head serve para visualização dos dados
print(df.head())

# Definindo características do gráfico:
sb.set_theme(style="darkgrid")
sb.displot(df["Close"].dropna(),kde=True)

import plotly.offline as plof
import plotly.graph_objs as plgo

dados = [plgo.Scatter(x=df.index, y=df['Close'])]
layout = plgo.Layout(title='Histórico dos Preços da Ação',
yaxis={'title':'Preços'}, xaxis={'title': 'Período'})
fig = plgo.Figure(data=dados, layout=layout)
plof.iplot(fig)


