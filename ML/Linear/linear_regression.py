import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint
le = 0.01
input_data = open("linear-regression.txt","r")
data = []
for x in input_data.readlines():
    data.append(map(float,x.strip().split(",")))
X_train = np.array(data)[:,[0,1]]
Y_train = np.array(data)[:,[2]]
data_points = X_train.shape[0]
X_train = np.c_[np.ones(data_points),X_train]
weights = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T,X_train)), X_train.T), Y_train)
pprint(weights)
result = np.c_[X_train[:,1],X_train[:,2],Y_train,np.dot(X_train,weights)]
np.savetxt('Regression_Output.txt',result, header='X1\t\t\t\t\t\tX2\t\t\t\t\t\tLabel\t\t\t\t\t\t\tPrediction')

