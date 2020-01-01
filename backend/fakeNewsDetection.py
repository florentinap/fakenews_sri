import pandas as pd
import os
import pyspark
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import RegexTokenizer, OneHotEncoder, StringIndexer, VectorAssembler, StopWordsRemover, CountVectorizer
from pyspark.ml.classification import NaiveBayes, NaiveBayesModel

spark = SparkSession.builder.master("local[*]").getOrCreate()
nb = NaiveBayes.load("./ml/nbModel")
model = NaiveBayesModel.load("./ml/naiveBayes")
mySchema = StructType([StructField("text", StringType()),\
                       StructField("label", IntegerType())])
	
regexTokenizer = RegexTokenizer(inputCol="text", outputCol="words", pattern="\\W")
stopwordsRemover = StopWordsRemover(inputCol="words", outputCol="filtered")
countVectors = CountVectorizer(inputCol="filtered", outputCol="features", vocabSize=10000)

sc = spark.sparkContext
# pipelineFit = PipelineModel.load("./ml/pipeline")

def predict(news_text):
	news = sc.parallelize([(news_text, 1)])
	dataTest = spark.createDataFrame(news, mySchema)

	pipelineFit = PipelineModel.load("./ml/pipeline")
	dataset = pipelineFit.transform(dataTest)

	predictions = model.transform(dataset)
	predictions.filter(predictions['prediction'] == 0) \
		.select("text","label","prediction") \
		.orderBy("probability", ascending=False) \
		.show(n = 10, truncate = 30)
	predictions.filter(predictions['prediction'] == 1) \
		.select("text","label","prediction") \
		.orderBy("probability", ascending=False) \
		.show(n = 10, truncate = 30)

	return predictions.select("prediction").collect()[0].__getitem__("prediction")

# news_text = 'Says the Annies List political group supports third-trimester abortions on demand.'
# predict(news_text)