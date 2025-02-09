import pandas as pd
from sklearn.datasets import load_iris # Conjunto íris - pré-definido
data = load_iris() # associamos o conjunto a uma variável chamamos o método load íris
iris_df = pd.DataFrame(data.data, columns = data.feature_names)
iris_df["encoded_target"] = data.target # convertendo dicionário em dataframe
iris_df