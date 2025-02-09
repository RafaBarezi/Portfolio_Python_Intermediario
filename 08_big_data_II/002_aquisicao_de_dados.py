import pandas as pd
import yfinance as yf

df = yf.download("TSLA", start="2022-06-01", end="2022-12-31", group_by="ticker")
print(df.head())