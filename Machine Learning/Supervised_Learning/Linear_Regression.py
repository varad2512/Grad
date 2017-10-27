#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 01:07:59 2017

@author: priyambadajain
"""
import numpy as np
import pandas as pd

def gradDesc(X,y,theta,alpha,iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    Z = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        Z[i] = computeCost(X, y, theta)

    return theta, Z
    
def computeCost(X, y, theta):  
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

data_file ="linear-regression.txt"
data_file = open(data_file,"r")
data_points=[]

for line in data_file:
    line = map(float,line.split(","))
    data_points.append(line[:3])
 

df = pd.DataFrame(data_points,columns=['X','Y','Z'])
#normalize the dataset
df = (df-df.mean())/df.std()
#appending x0 = 1 always
df.insert(0,'Xo',1)
cols = df.shape[1]
X = df.iloc[:,0:cols-1]  
y = df.iloc[:,cols-1:cols]
alpha = 0.01  
iters = 1000
# convert to matrices and initialize theta
X = np.matrix(X.values)  
y = np.matrix(y.values)  
theta = np.matrix(np.array([0,0,0]))  

g, Z = gradDesc(X, y, theta, alpha, iters)

# get the cost (error) of the model
print(computeCost(X, y, g))
predicted_value= X*g.T
df['Predicted']= predicted_value
df.to_csv('Linear_Regression_Results.csv')
