from flask import Flask, jsonify, request
from flask_cors import CORS

from elasticsearch_helper import searchNews, addNews
from fakeNewsDetection import predict

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('query')
	result = searchNews(query)
	
	return jsonify(result)

@app.route('/predict', methods=['GET'])
def prediction():
	values = ['false', 'true']
	text = request.args.get('query')
	result = predict(text)
	
	addNews(text, values[int(result)])

	return jsonify(values[int(result)])

if __name__ == '__main__':
	app.run()