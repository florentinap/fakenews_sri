import csv
import json


with open('train.tsv', 'r') as tsvfile:
	reader = list(csv.reader(tsvfile, delimiter='\t'))

data = {}
data['news'] = []
for r in reader:
	if len(r) > 4:
		data['news'].append({
			'label': r[1],
			'statement': r[2],
			'subject': r[3],
			'author': r[4]
			})
		print (r[6])
# with open('fakenews.json', 'w') as outfile:
#     json.dump(data, outfile)

# with open('train.tsv', 'rb') as tsvfile:
# 	reader = list(csv.reader(tsvfile, delimiter='\t'))
# 	for r in reader[0:5]:
# 		print(r)

# with open('fakenews.csv', 'rb') as fakenews:
# 	reader = list(csv.reader(fakenews))
# 	for r in reader[0:5]:
# 		print(r)