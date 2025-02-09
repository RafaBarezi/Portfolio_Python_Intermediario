# Iniciar o pacote

import findspark
findspark.init()

# PySpark  - Instanciar o SparkContext

from pyspark import SparkContext
spark_contexto = SparkContext() # Instantiate SparkContext

print(spark_contexto)

import numpy as np

vetor = np.array([10, 20, 30, 40, 50])

# transformando o python em RDD do spark
paralelo = spark_contexto.parallelize(vetor)
print(paralelo)

mapa = paralelo.map(lambda x : x**2+x) # x²+x

mapa.collect()

paralelo = spark_contexto.parallelize(["distribuida", "distribuida", "spark", "rdd", "spark", "spark"])

funcao_lambda = lambda x:(x,1) # Definindo um par ordenado

from operator import add
mapa = paralelo.map(funcao_lambda).reduceByKey(add).collect()
# Feita a redução por chave

for(w, c) in mapa:
  print("{}:{}".format(w,c))

spark_contexto.stop()