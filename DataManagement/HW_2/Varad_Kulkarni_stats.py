import json
from collections import defaultdict as dict
from pprint import pprint
import sys
input_file = sys.argv[1]
question_tags = dict(int)
questions = dict(list)
list_of_tags = ["how many","how much","how","what","when","where","which","whom","who"]
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
                    questions[y].append(q['question'])
                    break
with open('result_stats.json', 'w') as fp:
    json.dump(question_tags, fp)
#print{key:value for key,value in question_tags.iteritems()},
