import pandas as pd
import math
from collections import defaultdict
import numpy as np
import random
import matplotlib.pyplot as plt
from pprint import pprint
# number of clusters

def L2_distance(centroids, current_tuple):
    '''

    :param centroids: Dictionary
    :param current_tuple: Tuple of X and Y coordinate
    :return: Centroid assigned to X and Y with minimum distance (L2 Distance)
    '''
    min = float("inf")
    for key,items in centroids.iteritems():
        if (math.sqrt(((items[0] - current_tuple[0])^2) + ((items[1] - current_tuple[1])^2))) < min:
            match = [items[0],items[1]]
            min   = math.sqrt(((items[0] - current_tuple[0])^2) + ((items[1] - current_tuple[1])^2))
    return match

k = 3
data = []
file_name = "clusters.txt"
mode = "r"
input_file = open(file_name, mode)
for line in input_file.readlines():
    data.append(tuple(map(float, line.strip().split(","))))
#plot initial points
x_max,x_min,y_max,y_min = max(zip(*data)[0]),min(zip(*data)[0]),max(zip(*data)[1]),min(zip(*data)[1])
plt.scatter(*zip(*data))


#randomly initialise centroids for the first iterations
centroids = {i : [np.random.randint(x_min,x_max), np.random.randint(y_min,y_max)] for i in range(k)}
print centroids
for i in centroids.keys():
    plt.scatter(*centroids[i],color = 'r')
plt.show()

while(True):
    #TODO : base case
    assignments = defaultdict(list)
    for i in data:
        assigned_centroid = L2_distance(centroids,i)
        assignments[assigned_centroid].append(i)

    #TODO recomputation of centroids

