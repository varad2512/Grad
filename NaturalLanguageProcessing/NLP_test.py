import pickle
from pprint import pprint
from collections import defaultdict
import math
#Global Declarations

a = pickle.load(open('model.txt','rb'))
transition = a[0]
emission   = a[1]
testFile = open('random.txt','rb')

for lines in testFile.readlines():
	words = lines.split()
	length = len(words)
	bestScore = defaultdict()
	backEdge   = defaultdict()
	bestScore = defaultdict()
	bestScore['0 start'] = 0
	backEdge['0 start'] = None
	for i in range(length):
		for prev in list(transition.keys()):
			for nexts in list(transition.keys()):
				if prev in transition.keys() and nexts in transition[prev].keys() and ((str(i)+" "+str(prev)) in bestScore.keys()):
					if words[i] in emission[nexts].keys():
						score = bestScore[str(i)+" "+str(prev)] + (-math.log(transition[prev][nexts])) + (-math.log(emission[nexts][words[i]]))
					else:
						''' Smoothning required for emission of unknown or unseen words'''
						score = bestScore[str(i)+" "+str(prev)] + (-math.log(transition[prev][nexts])) + -math.log(0.00001)

					if (str(i+1)+" "+str(nexts)) not in bestScore.keys() or  bestScore[str(i+1)+" "+str(nexts)] > score:
						
						bestScore[str(i+1)+" "+str(nexts)] = score 
						backEdge[str(i+1)+" "+str(nexts)]  = str(i)+" "+str(prev)
	#Fidning mininmum score for last state
	finalState = defaultdict(dict)
	minScore   = 100000000.0
	minKey     = ''
	for key,value in bestScore.iteritems():
		finalState[key.split()[0]][key.split()[1]] = float(value)
	for key,value in finalState[str(i+1)].iteritems():
		if float(minScore) > float(value):
			minScore = float(value)
			minKey   = key
	backEdge[str(i+2)+" "+'End'] = str(i+1)+" "+str(minKey)
	bestScore[str(i+2)+" "+'End'] = minScore

	''' BACKTRACKING FOR PATH '''
	path = []
	tag = str(i+2)+" "+'End'
	while('start' not in tag):
		path.append(tag.split()[1])
		tag = backEdge[tag]
	pprint(list(reversed(path)))
