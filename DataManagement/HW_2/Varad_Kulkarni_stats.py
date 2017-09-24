import json
from collections import defaultdict as dict
from pprint import pprint
input_file = 'dev-v1.1.json'
question_tags = dict(int)
list_of_tags = ["how","how many","how much","what","when","where","which","who","whom"]
for x in list_of_tags:
    question_tags[x] = 0
with open(input_file) as data_file:
    data = json.load(data_file)
for x in data['data'][0]['paragraphs'][0]['qas']:
    if x['question'].startswith('Which NFL'):
        print x['question']
