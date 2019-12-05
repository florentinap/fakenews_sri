import pandas as pd
import os
import pyspark
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import RegexTokenizer, OneHotEncoder, StringIndexer, VectorAssembler, StopWordsRemover, CountVectorizer
from pyspark.ml.classification import NaiveBayesModel

def predict(news_text):
	spark = SparkSession.builder.master("local[*]").getOrCreate()
	model = NaiveBayesModel.load("./naiveBayes")
	mySchema = StructType([StructField("text", StringType()),\
                       StructField("label", IntegerType())])

	sc = spark.sparkContext
	news = sc.parallelize([(news_text,1)])
	dataTest = spark.createDataFrame(news,mySchema)
	# print(dataTest)
	# dataTest.show()

	regexTokenizer = RegexTokenizer(inputCol="text", outputCol="words", pattern="\\W")
	stopwordsRemover = StopWordsRemover(inputCol="words", outputCol="filtered")
	countVectors = CountVectorizer(inputCol="filtered", outputCol="features", vocabSize=10000)

	pipelineFit = PipelineModel.load("./pipeline")
	dataset = pipelineFit.transform(dataTest)
	# dataset.show(1)

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

news_text = 'Says the Annies List political group supports third-trimester abortions on demand.'
predict(news_text)