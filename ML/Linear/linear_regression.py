import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
le = 0.01
input_data = open("classification.txt","r")
data = []
for x in input_data.readlines():
    data.append(map(float,x.strip().split(",")))
X_train = np.array(data)[:,[0,1]]
Y_train = np.array(data)[:,[2]]
Y_train = np.reshape(Y_train, (2000))
data_points = X_train.shape[0]

weights = np.dot(np.dot(np.linalg.inv(np.dot(X_train.T,X_train)), X_train.T), Y_train)
pprint(weights)

with open("Regression_Output.txt","w") as fout:
    for i in range(data_points):
        fout.write(str(X_train[i]) + "\t" + str(Y_train[i]) + "\t" + str(X_train.dot(weights)[i]))
        fout.write("\n")

