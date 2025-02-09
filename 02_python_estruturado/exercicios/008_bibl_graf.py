# Implementar uma solução para visualizar dados de vendas em um gráfico de barras

# Use: x = ["A", "B", "C", "D"] y = [3, 8, 1, 10]

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.xlabel("Produto")
plt.ylabel("valores")
plt.title("Relaçao de vendas")
plt.show()