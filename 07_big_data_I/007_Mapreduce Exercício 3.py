import findspark
findspark.init()

# PySpark  - Instanciar o SparkContext

from pyspark import SparkContext
spark_contexto = SparkContext() # Instantiate SparkContext

lista = ([1, 2, 3, 4, 5, 3])
lista_rdd = spark_contexto.parallelize(lista)

lista_rdd.count() # Contando a quantidade de ítens da lista

par_ordenado = lambda numero: (numero, numero*10)

lista_rdd.flatMap(par_ordenado).collect() # Flat vetoriza a lista

lista_rdd.map(par_ordenado).collect()