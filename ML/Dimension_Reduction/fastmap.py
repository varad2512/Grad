import numpy as np
import math
from collections import defaultdict
from pprint import pprint
import sys
#global arrays
k = 2
N = 10
X = np.zeros([N,k], dtype = "float")
pivot_array = np.ones([2,k])
#ID of the pivot objects for each recursive call --global
column = 0
strings = open(sys.argv[2],"r")
strings = [x.strip() for x in strings.readlines()]
distance = open(sys.argv[1],"r")
distance_matrix = np.ones([10,10], dtype = "float")
for x in range(10):
    for y in range(10):
        if x==y:
            distance_matrix[x,y] = 0
for lines in distance.readlines():
    temp = map(int,lines.strip().split())
    distance_matrix[temp[0]-1,temp[1]-1] = temp[2]
    distance_matrix[temp[1]-1,temp[0]-1] = temp[2]
pprint(distance_matrix)

print distance_matrix[9,0]

def find(init):
    maxed = 0
    for i in range(10):
        if distance_matrix[init][i] > maxed:
            maxed = distance_matrix[init][i]
            max_index = i
    return max_index

def farthestObjects():
    #TODO complete the function
    a = np.random.randint(0,9)
    while(True):
        b = find(a)
        c = find(b)
        if c == a:
            break
        else:
            del a
            a = b
    if a<b:
        return a,b
    else:
        return b,a

def fastMap(k):

    global distance_matrix
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
    print "yes"
    pprint(distance_matrix)
    column+=1
    fastMap(k-1)


fastMap(2)
pprint(X)


