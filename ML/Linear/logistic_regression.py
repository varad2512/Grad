import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
#learning rate
le = 0.1
input = open("classification.txt","r")
input_data = []
for lines in input.readlines():
    input_data.append(map(float,lines.strip().split(",")))
input_data = np.array(input_data)[:,[0,1,2,4]]
X_train = input_data[:,:3]
Y_train = input_data[:,3]
data_points, features = input_data.shape[0],X_train.shape[1]
weights = np.random.uniform(0.0,1.0,features)

for step in xrange(7000):

    scores = np.dot(X_train, weights)
    probability = np.exp(scores) / (1 + np.exp(scores))
    loss = np.sum(np.log(1 + np.exp(-(np.dot(Y_train, scores))))) / Y_train.shape[0]

    #calculate derivative
    gradient = -(np.sum(np.dot(Y_train, X_train) / (1 + np.exp(np.dot(Y_train, scores)))))/Y_train.shape[0]

    #gradient descent
    weights = weights - le*(gradient)

    print step,":",loss


print weights

