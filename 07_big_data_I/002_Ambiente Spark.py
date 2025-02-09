
# Iniciar o pacote
 
import findspark
findspark.init()
 
# PySpark  - Instanciar o SparkContext
 
from pyspark import SparkContext
spark_contexto = SparkContext() # Instantiate SparkContext
print(spark_contexto)
 
# Criar uma instância do Spark
 
from pyspark.sql import SparkSession
# Criando a sessão do Spark na maquina local
spark = SparkSession.builder.master("local[*]").getOrCreate()
print(spark_contexto.version)