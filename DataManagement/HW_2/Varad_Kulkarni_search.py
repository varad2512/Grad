import json
import sys
from pprint import pprint
input_file = sys.argv[1]
search_string = sys.argv[2].strip()
with open(input_file) as data_file:
    data = json.load(data_file)
len1 = len(data['data'])
print data['data'][0]['paragraphs'][0]['context']
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            if search_string.lower() in q['question'].lower() :
                print q['question'],q['id'],q['answers'][0]["text"]
