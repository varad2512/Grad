import numpy as np
import math
from collections import defaultdict
from pprint import pprint
import sys
#global arrays
k = 2
N = 10
X = np.ones([N,k])
pivot_array = np.ones([2,k])
#ID of the pivot objects for each recursive call --global
column = 0
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
pprint(distance_matrix)
def farthestObjects():
    global distance_matrix
    #TODO complete the function

def fastMap(k):

    global column
    global X
    global pivot_array

    if k<=0:
        return

    #Find the indices of the farthest objects in the space
    OA,OB = farthestObjects()
    pivot_array[0,column] = OA
    pivot_array[1,column] = OB

    if distance_matrix[OA,OB] == 0:
       X[:,column] = 0
    #Finding Coordinates using cosine function

    X[OA,column] = 0
    X[OB,column] = distance_matrix[OA,OB]

    for i in range(len(strings)):
         #Formula for calculating coordinate for every object
         if i!=OA and i!=OB:
            X[i,column] = ((distance_matrix[OA,i])**2 + (distance_matrix[OA,OB])**2 - (distance_matrix[OB,i])**2)/(2*(distance_matrix[OA,OB]))

    #Updating Distance Matrix for next recursive call
    for i in range(10):
        for j in range(10):
            distance_matrix[i,j] = math.sqrt((distance_matrix[i,j]**2) - (X[i,column] - X[j,column])**2)

    column+=1
    fastMap(k-1)






