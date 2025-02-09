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

print(spark)

# Carregar os dados do arquivo no Spark Dataframe

dataset = spark.read.csv('/content/sample_data/california_housing_test.csv',inferSchema=True, header =True)
# dataframe do google já configurado

# Imprimir o Esquema

dataset.printSchema()

# Visualizar um subconjunto dos Dados

dataset.show(3)

dataset.head()

dataset.count()

# Criar Tabela SQL Temporária

dataset.createOrReplaceTempView("tabela_temporaria")

print(spark.catalog.listTables())

# Criar consultas SQL

query = "FROM tabela_temporaria SELECT longitude, latitude LIMIT 3"  # Don't change this query

# Executar a Query

saida = spark.sql(query)  # Get the first 10 rows of flights

# Exibir o resultado da Query

saida = spark.sql(query)  # Get the first 10 rows of flights

# Parar o Spark

spark.stop()