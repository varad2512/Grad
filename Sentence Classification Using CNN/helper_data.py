'''
Sentence Classification using Convolutional Neural Networks
References : https://arxiv.org/abs/1408.5882
WildML - Explanation for NLP with Convolutional Neural Networks. Not Word2Vec used. In fact no pre=processing models used to 
model the word vectors.
'''
import tensorflow as tf 
import numpy as np
import sys
import re
from pprint import pprint

class HelperData:
	
	def __init__(self):
		self.input_pos = open(sys.argv[1],"r")
		self.input_neg = open(sys.argv[2],"r")

	'''
	def countVocabulary(self):
		lines = self.input_data.readlines()
		unique = []
		for iter in lines:
			unique.append(iter.strip().split(" "))
		print set(unique)
	'''

	def preProcess(self, positive, negative):
		positives = list(positive.readlines())
		negatives = list(negative.readlines())
		positives = [x.strip() for x in positives]
		negatives = [x.strip() for x in negatives]
		x_train = positives + negatives
		x_train = [self.clean_str(x) for x in x_train]
		print max([len(x.split()) for x in x_train])
		positive_labels = [[0, 1] for _ in positives]
		negative_labels = [[1, 0] for _ in negatives]
		y = np.concatenate([positive_labels, negative_labels], 0)
	



	def clean_str(self,string):
		string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
		string = re.sub(r"\'s", " \'s", string)
		string = re.sub(r"\'ve", " \'ve", string)
		string = re.sub(r"n\'t", " n\'t", string)
		string = re.sub(r"\'re", " \'re", string)
		string = re.sub(r"\'d", " \'d", string)
		string = re.sub(r"\'ll", " \'ll", string)
		string = re.sub(r",", " , ", string)
		string = re.sub(r"!", " ! ", string)
		string = re.sub(r"\(", " \( ", string)
		string = re.sub(r"\)", " \) ", string)
		string = re.sub(r"\?", " \? ", string)
		string = re.sub(r"\s{2,}", " ", string)
		return string.strip().lower()


helper = HelperData()
helper.preProcess(helper.input_pos, helper.input_neg)