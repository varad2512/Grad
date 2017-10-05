import numpy as np
from collections import defaultdict
from pprint import pprint
import sys
strings = open(sys.argv[2],"r")
strings = [x.strip() for x in strings.readlines()]
distance = open(sys.argv[1],"r")
distance_matrix = np.ones([10,10], dtype = "int8")
for x in range(10):
    for y in range(10):
        if x==y:
            distance_matrix[x,y] = 0
for lines in distance.readlines():
    temp = map(int,lines.strip().split())
    distance_matrix[temp[0]-1,temp[1]-1] = temp[2]
    distance_matrix[temp[1]-1,temp[0]-1] = temp[2]

def farthest_objects():
    global distance_matrix

