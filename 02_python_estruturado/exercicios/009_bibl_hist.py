# Implementar uma soluçãopara gerar 1000 pontos seguindo a distribuição normal com média e desvio-padrão 2. Exiba os dados em um histograma

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1) # gera a randomização
dados = np.random.normal(loc=20, scale=2, size=1000)

plt.hist(dados, color='black', edgecolor='blue')
plt.show()