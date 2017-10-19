import numpy as np
from pprint import pprint
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

for i in range(epochs):
    updated_flag = 0
    for iterator in range(data_points):

