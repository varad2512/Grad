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
epochs = 7000
constraints = np.zeros(epochs)
for i in range(epochs):
    print i
    violations = 0
    w_updated = False
    for iterator in range(data_points):
        prediction = np.dot(weights.T, X_train[iterator])
        if prediction > 0 and int(Y_train[iterator]) == -1:
            weights -= le * X_train[iterator]
            w_updated = True
            violations+=1
        elif prediction < 0 and int(Y_train[iterator]) == 1:
            weights += le * X_train[iterator]
            w_updated = True
            violations+=1
    constraints[i] = violations
    if w_updated == False:
        print "Converged"
        break

if w_updated == True:
    print "Failed to converge"

#PLOT
pprint(constraints)
iters = np.arange(0,7000,1)
plt.plot(iters, constraints,'g^')
plt.xlabel("Iterations")
plt.ylabel("No of violated constraints")
plt.title("Pocket Algorithm")
plt.show()