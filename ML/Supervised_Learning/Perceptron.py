#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:14:03 2017

@author: priyambadajain
"""
import numpy as np
from decimal import *
import math

#PREDICT THE CLASS FOR THE DATA POINT
def predict_level(data_point,weights,bias):
    return int(np.sign(bias+np.dot(weights,data_point)))
        
data_file = "classification.txt"
data_file = open(data_file,"r")
data_points=[]
level=[]
for line in data_file:
    line = map(float,line.split(","))
    data_points.append(line[0:3])
    level.append(line[3])
    
X = np.array(data_points)
Y = np.array(level)

instances,dimen = X.shape
weights = np.zeros(dimen)
bias=0

#building the model using the perceptron learning algorithm
while True:
    w_updated = False
    for j in range(0,instances):
        a = bias + np.dot(weights,X[j])
        if np.sign(Y[j]*a) != 1:
            w_updated = True
            weights +=Y[j]*X[j]
            bias +=Y[j]
    if not w_updated:
        print("Converged equation found")
        break

#Now check the levels for the data points based on the weights obtained
predicted_level = []         

for i in range(np.shape(X)[0]):
    pred_class = predict_level(X[i],weights,bias)
    predicted_level.append(pred_class)

for line in data_file:
    line = line.split(",")
    data_points.append(line[0:3])
    
res = zip(data_points,Y,predicted_level)



with open ("Perceptron_result.txt","w") as output:
    output.write("Data_Point  ,   Actual_level , Predicted_Level")
    output.write("\n")
    for line in res:
        output.write(str(line))
        output.write("\n")
    

