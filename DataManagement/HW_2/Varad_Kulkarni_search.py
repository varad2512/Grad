import json
import re
import sys
from pprint import pprint
from collections import OrderedDict
input_file = sys.argv[1]
search_string = sys.argv[2].strip()
search_string_words = search_string.split()
pprint(search_string_words)
pattern = '(?<=\\s){0}(?=\\s)|^{0}(?=\\s)|(?<=\\s){0}$|^{0}$'
with open(input_file) as data_file:
    data = json.load(data_file)
len1 = len(data['data'])
result = []
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            if all(re.search(pattern.format(x), q['question'].lower(), flags=re.I) for x in search_string_words):
                    result.append(OrderedDict([("id",str((q['id'].encode("utf-8")))),
                                               ("question",str((q['question'].encode("utf-8")))),
                                               ("answer",str((q['answers'][0]["text"].encode("utf-8"))))]))
with open("1b.json","w") as data:
    json.dump(result,data, indent = 4)