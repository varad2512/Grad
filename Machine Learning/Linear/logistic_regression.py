import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
#learning rate
le = 0.3
input = open("classification.txt","r")
input_data = []
for lines in input.readlines():
    input_data.append(map(float,lines.strip().split(",")))
input_data = np.array(input_data)[:,[0,1,2,4]]
X_train = input_data[:,:3]
Y_train = input_data[:,3]
data_points, features = input_data.shape[0],X_train.shape[1]
weights = np.random.uniform(0.0,1.0,features+1)
X_train = np.c_[np.ones(data_points), X_train]

for step in xrange(7000):
    scores = np.dot(X_train, weights)
    probability = np.exp(scores) / (1 + np.exp(scores))
    loss = np.sum(np.log(1 + np.exp(-(np.dot(Y_train, scores))))) / Y_train.shape[0]
    gradient = -(np.sum(np.dot(Y_train, X_train) / (1 + np.exp(np.dot(Y_train, scores)))))/Y_train.shape[0]
    weights = weights - le*(gradient)
    print step,":",loss

print weights
scores_prediction = np.dot(X_train, weights)
probability_prediction = np.exp(scores_prediction) / (1 + np.exp(scores_prediction))
probability_prediction[probability_prediction >= 0.5] =  1
probability_prediction[probability_prediction <  0.5] = -1


with open("Logistic_Regression_Output.txt","w") as fout:
    for i in range(data_points):
        fout.write(str(X_train[i,1:]) + "\t" + str(Y_train[i]) + "\t" + str(probability_prediction[i]))
        fout.write("\n")


test = probability_prediction == Y_train.all()
count = 0
for x in test:
    if x == True:
        count+=1
print (count*1.0/len(test)) * 100

