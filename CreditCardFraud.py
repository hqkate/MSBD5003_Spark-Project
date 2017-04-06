from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("example-spark").config("spark.sql.crossJoin.enabled","true").getOrCreate()

# Load data through Spark dataFrame
lines = spark.read.text("/home/kate/Documents/creditcard.csv")

# Overview of the dataset

# Set up training and testing dataset

# Model building and training
