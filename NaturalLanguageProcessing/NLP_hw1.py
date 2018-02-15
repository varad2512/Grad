from collections import defaultdict
import sys
import math
from pprint import pprint
import pickle
#Global Declarations
transitionModel = defaultdict(dict)
emissionModel   = defaultdict(dict)
context = {}
transitionMatrix  = {}
emissionMatrix    = {}
context           = defaultdict(lambda : 0, context)
transitionMatrix  = defaultdict(lambda : 0, transitionMatrix)
emissionMatrix    = defaultdict(lambda : 0, emissionMatrix)
def findParams():
	#TODO : Do not include the count for context if the tag is found at the end of the sentence. 
	#Right now it is being included.
	trainFile = open('en_train_tagged.txt','r')
	for x in trainFile.readlines():
		wordsTags = x.split()
		previous  = 'start'
		context[previous] += 1 
		for y in wordsTags:
			word = y.rsplit('/',1)[0]
			tag  = y.rsplit('/',1)[1]
			transitionMatrix[previous+" "+tag] += 1
			context[tag] += 1
			emissionMatrix[tag+" "+word] += 1
			previous = tag
findParams()
for key,value in transitionMatrix.iteritems():
	transitionModel[key.split()[0]][key.split()[1]] = float(value)/context[key.split()[0]]
for key,value in emissionMatrix.iteritems():
	emissionModel[key.split()[0]][key.split()[1]] = float(value)/context[key.split()[0]]
writef = open('model.txt','wb')
dumped = [transitionModel, emissionModel]
pickle.dump(dumped, writef)


