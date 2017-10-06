import json
import re
import sys
from pprint import pprint
from collections import OrderedDict
import string
input_file = sys.argv[1]
search_string = sys.argv[2].strip()
search_string_words = search_string.split()
util = ''.join(x for x in(set(string.punctuation) - set(["'"])))
with open(input_file) as data_file:
    data = json.load(data_file)
len1 = len(data['data'])
result = []
for x in range(len1):
    for z in range(len(data['data'][x]['paragraphs'])):
        for q in data['data'][x]['paragraphs'][z]['qas']:
            counter = 0
            words_in_question = q['question'].encode('ascii', 'ignore').translate(None, util).split()
            for it in search_string_words:
                for w in words_in_question:
                    if w.lower()==it.lower():
                        counter+=1
                        break
            if counter == len(search_string_words):
                result.append(OrderedDict([("id",str((q['id'].encode("ascii","replace")))),
                                           ("question",str((q['question'].encode("ascii", "replace")))),
                                           ("answer",str((q['answers'][0]["text"].encode("ascii", "replace"))))]))

with open("1b.json","w") as data:
    json.dump(result,data, indent = 4)