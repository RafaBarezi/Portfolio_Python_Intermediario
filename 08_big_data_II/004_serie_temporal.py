import pandas as pd
import yfinance as yf
import plotly.offline as py
import plotly.graph_objs as go

df = yf.download("JNJ", start="2022-06-01", end="2022-12-31", group_by="ticker")

dados = [go.Scatter(x=df.index, y=df["Close"])]
layout = go.Layout(title="Fechamento das ações Jhonson & Jhonson em 2022", yaxis={"title":"Valores"}, xaxis={"title":"Período"})
fig=go.Figure(data=dados, layout=layout)
py.iplot(fig)

# Para exibir o valor mínimo da  ação: 
minimo=df['Close'].min()
print(f'mínimo: {minimo}')