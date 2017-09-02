import os
from sklearn.preprocessing import LabelEncoder as lb
import pandas as pd
from pprint import pprint as pp
filename='dt-data.txt'
mode='r'
input_data = open(filename, mode)
lines = input_data.readlines()
feature_names=(lines[0].strip().strip('(').strip(')').split(','))
lines=lines[2:]
data=[]
for x in lines:
     data.append((x.split(':')[1].strip().strip(';')).split(','))
df = pd.DataFrame(data,columns=feature_names)
for x in feature_names:
    df[x]=df[x].astype('category')
for x in feature_names:
    df[x]=df[x].cat.codes
print df