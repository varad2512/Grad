import pandas as pd
import numpy as np
from collections import defaultdict as d
import math
#TODO Define a preprocessing function as :"preprocessing():"

filename ='dt-data.txt'
mode ='r'
input_data = open(filename, mode)
lines = input_data.readlines()
feature_names = (lines[0].strip().strip('(').strip(')').split(','))
lines = lines[2:]
data = []
for x in lines:
     data.append((x.split(':')[1].strip().strip(';')).split(','))
df = pd.DataFrame(data,columns=feature_names)
for x in feature_names:
    df[x] = df[x].astype('category')
for x in feature_names:
    df[x] = df[x].cat.codes
target = np.array(df[' Enjoy'])
df = df.drop(labels=' Enjoy', axis=1)
feature_list = d(np.array)
for x in df:
    feature_list[x]=np.array(df[x])

def initialEntropy(attribute):

    return_value = 0
    count = []
    unique_elements = np.unique(attribute)
    for x in unique_elements:
        count.append((attribute == x).sum())
    count = np.asarray(count)
    count = float(count/3)
    for x in count:
       if x!=0 : return_value+= x*(math.log((1/x),2))
    return return_value


def informationGain(target, attribute):

    #TODO
    E1 = initialEntropy(target)



def decisionTrees(input_features, target):
    '''
    :param input_features: features np array
    :param target: Labels np array
    :return: Decision Tree
    '''
    #TODO recursion and return value
    selected_attribute = min(informationGain(target, attribute) for attribute in input_features)





