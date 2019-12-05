import sys
sys.path.append('../dataset')

from flask import Flask, jsonify, request
from flask_cors import CORS

from elasticsearch_helper import searchNews

import random

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
	text = request.args.get('query')
	result = random.choice(['true', 'barely-true', 'false', 'half', 'mostly-true', 'pants-fire']) #predict(query)
	return jsonify(result)

if __name__ == '__main__':
	app.run()