from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.mllib.stat import Statistics

spark = SparkSession.builder.appName("example-spark").config("spark.sql.crossJoin.enabled","true").getOrCreate()

# Load data through SparkSQL
dataset = spark.read.csv("/home/kate/Documents/creditcard.csv", header="true", inferSchema="true")

# Overview of the dataset
fraud = dataset.filter("Class = '1'") # count() = 492
valid = dataset.filter("Class = '0'") # count() = 284315

# deal with the unbalanced dataset
new_data = dataset.select(concat(fraud))
new_data = valid.unionAll(fraud)
new_data = new_data.unionAll(fraud)

# Correlation check
header = dataset.schema.names

for i in range(30):
  feature = header[i]
  print dataset.stat.corr(feature,'Class')

# Set up training and testing dataset
fraud_train = 
valid_train = 

# Model building and training
