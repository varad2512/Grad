import numpy as np
from pprint import pprint
#learning rate
le = 0.1
input = open("classification.txt","r")
input_data = []
for lines in input.readlines():
    input_data.append(map(float,lines.strip().split(",")[:4]))
input_data = np.array(input_data)
X_train = input_data[:,:3]
Y_train = input_data[:,3]
data_points, features = input_data.shape[0],X_train.shape[1]
weights = np.random.uniform(0.0,1.0,features)
epochs = 0
while True:
    epochs+=1
    w_updated = False
    for data_points_iterator in range(data_points):
        prediction = np.dot(weights.T,X_train[data_points_iterator])
        if prediction  > 0 and int(Y_train[data_points_iterator]) == -1:
            weights-= le * X_train[data_points_iterator]
            w_updated = True
        elif prediction < 0 and int(Y_train[data_points_iterator]) == 1:
            weights+= le * X_train[data_points_iterator]
            w_updated = True
    if w_updated == False:
        break
#Prediction using the learnt weights
predictions = []
for x in range(data_points):
    if np.dot(weights, X_train[x]) > 0:
        predictions.append(1.0)
    else:
        predictions.append(-1.0)
np.savetxt(r'Perceptron_Result.txt', np.c_[X_train, Y_train, predictions], header='\t\t\t\t\t\t\t\t\t\t\tData\t\t\t\t\t\t\t\t\tLabel\t\t\t\tPrediction')
