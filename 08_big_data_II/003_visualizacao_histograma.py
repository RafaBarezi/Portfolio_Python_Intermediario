import pandas as pd
import yfinance as yf
import seaborn as sb

df = yf.download("JNJ", start="2022-06-01", end="2022-12-31", group_by="ticker")

sb.set_theme(style="darkgrid")
sb.displot(df["Close"].dropna(), kde=True)

# displot serve para trabalhar com histograma
# Close é o valor de fechamento da ação
# dropna() serve para aliminar sujeiras nos dados, alguns dados que porventura não poderam ser coletados
# kde=True é um parâmetro usado para melhor visualização dos dados no gráfico