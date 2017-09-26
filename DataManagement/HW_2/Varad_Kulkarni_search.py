import json
import sys
from pprint import pprint
from collections import OrderedDict
input_file = sys.argv[1]
search_string = sys.argv[2].strip()
with open(input_file) as data_file:
    data = json.load(data_file)
len1 = len(data['data'])
result = []
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            if search_string.lower() in q['question'].lower() :
                result.append(OrderedDict([("id",str((q['id'].encode("utf-8")))),
                                           ("question",str((q['question'].encode("utf-8")))),
                                           ("answer",str((q['answers'][0]["text"].encode("utf-8"))))]))

#pprint(result)
with open("result_search.json","w") as data:
    json.dump(result,data, indent = 4)