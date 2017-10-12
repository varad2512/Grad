#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 00:46:24 2017

@author: priyambadajain
"""
import numpy as np
import matplotlib.pyplot as plt

data_file = "classification.txt"
data_file = open(data_file,"r")
data_points=[]
level=[]
for line in data_file:
    line = map(float,line.split(","))
    data_points.append(line[0:3])
    level.append(line[4])
    
X = np.array(data_points)
Y = np.array(level)

instances,dimen = X.shape
weights = np.zeros(dimen)
bias=0

max_iterations = 7000
voilated_constraint = np.zeros(max_iterations)
con=0
for i in range(0,max_iterations):
    w_updated = False
    for j in range(0,instances):
        a = bias + np.dot(weights,X[j])
        if np.sign(Y[j]*a) != 1:
            con+=1
            w_updated = True
            weights +=Y[j]*X[j]
            bias +=Y[j]
    voilated_constraint[i]=con
    con=0
    if not w_updated:
        print("Converged equation found")
        break
if w_updated:
    print("Not converged after max_iterations")
    
print(voilated_constraint[6900])
iters = np.arange(0,7000,1)
plt.plot(iters, voilated_constraint,'g^')
plt.xlabel("Iterations")
plt.ylabel("No of voilated constraints")
plt.title("Pocket Algorithm")
plt.show()