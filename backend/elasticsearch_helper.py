from  elasticsearch import Elasticsearch, helpers
import csv
import json

index = 'news'
es = Elasticsearch([{
	'host': 'localhost', 
	'port': 9200
	}])

def indexData():
	with open('./files/fakenews.json') as json_file:
		data = json.load(json_file)
		for idx, news in enumerate(data['news']):
			 es.index(
			 	index = index, 
			 	doc_type = index,
			 	id = idx,
			 	body = news)

def searchNews(query):
	result = es.search(
		index = index,
		body = {'query': {'match': {'statement': query}}})

	return [hit['_source'] for hit in result['hits']['hits']]

def getIndex(idx):
	result = es.get(
		index = index, 
		doc_type = index,
		id = idx)
	return result

def addNews(news, label):
	es.index(
		index = index,
		doc_type = index,
		body = {'statement': news, 'label': label})
