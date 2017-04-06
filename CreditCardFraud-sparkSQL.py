from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.mllib.stat import Statistics

spark = SparkSession.builder.appName("example-spark").config("spark.sql.crossJoin.enabled","true").getOrCreate()

# Load data through SparkSQL
dataset = spark.read.csv("/home/kate/Documents/creditcard.csv", header="true", inferSchema="true")

# Overview of the dataset
fraud = dataset.filter("Class = '1'") # count() = 492
valid = dataset.filter("Class = '0'") # count() = 284315
summary = Statistics.colStats(dataset)

# Set up training and testing dataset
fraud_train = 
valid_train = 

# Model building and training
