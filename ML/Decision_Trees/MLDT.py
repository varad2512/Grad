'''
Names:
Priyambada Jain(priyambj@usc.edu)
Sai Sree Kamineni (skaminen@usc.edu)
Varad Kulkarni (vdkulkar@usc.edu)
'''
import pandas as pd
import numpy as np
import math
from pprint import pprint
import sys
def initialEntropy(attribute):
    return_value = 0
    count = []
    unique_elements = np.unique(attribute)
    for x in unique_elements:
        count.append((attribute == x).sum())
    count = np.asarray(count)
    count = [float(item)/len(attribute) for item in count]  # Instead of 3 should it not be the len of the attribute array
    for x in count:
        if x!=0 : return_value+= x*(math.log((1/x),2))
    return return_value

def informationGain(target, attribute):
    occurence = []
    res = initialEntropy(target)
    values = np.unique(attribute)
    for element in values:
        occurence.append(float((attribute==element).sum()))
    frequency = [count/len(attribute) for count in occurence]
    for prob,val in zip(frequency,values):
        res -= prob * initialEntropy(target[attribute == val])
    return res


#divide the rows based on value of attribute a
def partition(a):
    splits = {}
    for i in set(a):
        splits[i] = []
        for j in range(len(a)):
            if i==a[j]:
                splits[i].append(j)
    return splits


def recursive_split(x, y):
    # check if its a pure class
    if len(set(y)) == 1 or len(y) == 0:
        return cat_dict[pred][y[0]]
    
    # calculate iformation gain for all the attributes in x
    all_gains = []
    for i in range(len(x.T)):
        all_gains.append(informationGain(y, x.T[i]))
    
    # check if there is a tie
    if max(all_gains)<=0:
        return "Tie"
    
    # extract attribute with highest IG
    attr_select = all_gains.index(max(all_gains))
    
    # split the data based on the attribute values
    new_splits = partition(x[:, attr_select])
    res = {}
    for key in new_splits.keys():
        new_x = x[new_splits[key]]
        new_y = y[new_splits[key]]
        # recursive call on new data set
        #res["%d = %d" % (attr_select, key)] = recursive_split(new_x, new_y)
        res["%s = %s" % (attr_names[attr_select], cat_dict[attr_names[attr_select]][key])] = recursive_split(new_x, new_y)
    return res

def predict(tree, lis):
    if type(tree) is str or len(tree.keys()) == 0:
        print "Prediction:",tree
        return 
    for i in lis:
        if i in tree.keys():
            lis.remove(i)
            break
    return predict(tree[i], lis)


pred = sys.argv[1]#'Enjoy'
filename ='dt-data.txt'
mode ='r'
input_data = open(filename, mode)
lines = input_data.readlines()
feature_names = []
for ele in lines[0].strip().strip('(').strip(')').split(','):
    feature_names.append(ele.strip())
lines = lines[2:]
data = []
for x in lines:
    new = []
    for ele in (x.split(':')[1].strip().strip(';')).split(','):
        new.append(ele.strip())
    data.append(new)
df = pd.DataFrame(data,columns=feature_names)
df1 = pd.DataFrame(data,columns=feature_names)
for x in feature_names:
    df[x] = df[x].astype('category').cat.codes
cat_dict = {}
for col in df.columns:
    cat_dict[col] = {}
for i in range(len(df)):
    for col in df.columns:
        cat_dict[col][df.loc[i, col]] = df1.loc[i,col]
target = np.array(df[pred])
feature_names.remove(pred)
df = df.drop(labels=pred, axis=1)
feature_list = {}
for x in df:
    feature_list[x]=list(df[x])
inputs = []
attr_names = {}
# to make sure attributes are in the same order as given in data
i = 0
for key in feature_names:
    inputs.append(feature_list[key])
    attr_names[i]=key
    i = i + 1
X = np.array(inputs).T
pprint(recursive_split(X, target))
testing = recursive_split(X, target)
predict_str = sys.argv[2] #'(occupied = Moderate; price = Cheap; music = Loud; location = City-Center; VIP = No; favorite beer = No)'
predict_eles = predict_str.lstrip('(').rstrip(')').split('; ')
new_eles = []
for ele in predict_eles:
    new_eles.append(ele[0].upper()+ele[1:])
predict(testing, new_eles)
