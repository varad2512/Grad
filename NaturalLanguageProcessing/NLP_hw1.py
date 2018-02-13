from collections import defaultdict
import sys
import math
from pprint import pprint
#Global Declarations
uniqueTags  = {}
uniqueWords = {}
tagsAtEnd   = {}
uniqueTags  = defaultdict(lambda : 0, uniqueTags)
uniqueWords = defaultdict(lambda : 0, uniqueWords)
tagsAtEnd   = defaultdict(lambda : 0, tagsAtEnd)
uniqueTagsList  = []
uniqueWordsList = []
def findUniqueTags():
	trainFile = open('en_train_tagged.txt','r')
	for x in trainFile.readlines():
		wordsTags = x.split()
		for y in wordsTags:
			uniqueTags[y.rsplit('/',1)[1]] += 1
			uniqueWords[y.rsplit('/',1)[0]] += 1
		lastPair = wordsTags[-1]
		tagsAtEnd[lastPair.rsplit('/',1)[1]] += 1
	print uniqueTags
	for key,value in uniqueTags.iteritems():
		uniqueTags[key] -= tagsAtEnd[key]
	print uniqueTags

findUniqueTags()
uniqueTagsList  = list(uniqueTags.keys())
uniqueWordsList = list(uniqueWords.keys())

