import json
import re
from collections import OrderedDict
from collections import defaultdict as dict
import sys
input_file = sys.argv[1]
question_tags = OrderedDict()
questions = dict(list)
pattern = r'^{0}(?=(\s)+)|^{0}(?=,)|^{0}\?$'
list_of_tags = ["how","how many","how much","what","when","where","which","whom","who"]
for x in list_of_tags:
    question_tags[x] = 0
with open(input_file) as data_file:
    data = json.load(data_file)
len1 = len(data['data'])
questions_list = []
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            questions_list.append(q['question'])
            for y in list_of_tags:
                if re.match(pattern.format(y.lower()), q['question'].strip().lower()):
                    question_tags[y]+=1
                    questions[y].append(q['question'])
with open('1a.json', 'w') as fp:
    json.dump(question_tags, fp)

