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
len1 = len(data['data'])
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            for y in list_of_tags:
                if q['question'].lower().startswith(y.lower()):
                    question_tags[y]+=1
                    print q['question']
print question_tags
