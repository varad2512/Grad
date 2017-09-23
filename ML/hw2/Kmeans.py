import pandas as pd
import math
from collections import defaultdict
import numpy as np
import random
import matplotlib.pyplot as plt
import copy
from pprint import pprint
def Assignment_Stage(centroids, data):
    '''
    :param centroids: Dictionary
    :param data: Pandas Data Frame
    '''
    for i in centroids.keys():
        data[str(i)] = np.sqrt((data['X'] - centroids[i][0])**2+(data['Y'] - centroids[i][1])**2)
    data['Nearest'] = data[['0', '1', '2']].idxmin(axis=1).map(lambda x:int(x))
    data['Colors'] = data['Nearest'].map(lambda x:colors[x])
    return data
def Compute_Stage(new_centroids):
    for i in centroids.keys():
        centroids[i][0] = np.mean(data[data['Nearest'] == i]['X'])
        centroids[i][1] = np.mean(data[data['Nearest'] == i]['Y'])
    return centroids
def show(centroids, data):
    for i in centroids.keys():
        plt.scatter(*centroids[i], color=colors[i])
    plt.scatter(data['X'], data['Y'], color=data['Colors'], alpha=0.3)
    plt.show()
k = 3
data = []
file_name = "clusters.txt"
mode = "r"
input_file = open(file_name, mode)
for line in input_file.readlines():
    data.append((map(float, line.strip().split(","))))
data = np.array(data)
data = pd.DataFrame({'X':data[:,0],'Y':data[:,1]})
x_max,x_min,y_max,y_min = max(data['X']),min(data['X']),max(data['Y']),min(data['Y'])
colors = {0:'r',1:'g',2:'b'}
centroids = {i : [np.random.randint(x_min,x_max), np.random.randint(y_min,y_max)] for i in range(k)}
for i in centroids.keys():
    plt.scatter(*centroids[i],color = colors[i])
data = Assignment_Stage(centroids,data)
plt.scatter(data['X'], data['Y'], color = data['Colors'], alpha = 0.3)
plt.show()
old_centroids = copy.deepcopy(centroids)
centroids = Compute_Stage(centroids)
data = Assignment_Stage(centroids,data)
while True:
    original = data['Nearest'].copy(deep=True)
    centroids = Compute_Stage(centroids)
    data = Assignment_Stage(centroids, data)
    if original.equals(data['Nearest']):
        break
show(centroids, data)
print centroids
for index,rows in data.iterrows():
    print (rows['X'],rows['Y'])," : ",tuple(centroids[rows['Nearest']])
