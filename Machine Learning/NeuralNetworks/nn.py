import re
import numpy as np
from pprint import pprint
import time
from sklearn.neural_network import MLPClassifier
start_time = time.time()
np.seterr(divide='ignore', invalid='ignore')
train = 'downgesture_train.list'
test  = 'downgesture_test.list'
#Binary prediction 1 for down gesture | 0 for any other gesture
classes = 2
learning_rate = 0.1

def activation(s, derivative = False):
	#Using sigmoid function
	
	if derivative:
		return activation(s)*(1.0 - activation(s))
	else:
		return (1.0/ (1.0 + np.exp(-s)))

def read_pgm(filename, byteorder='>'):
    """
    Return image data from a raw PGM file as np array.

    Format specification: http://netpbm.sourceforge.net/doc/pgm.html

    """
    with open(filename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return np.frombuffer(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height),
                            offset=len(header)
                            ).reshape((int(height), int(width)))

def train_function(train_data, train_label):

	#initialization of hyperparameters
	input_layer_weights  = np.random.uniform(-1000,1000,(train_data.shape[1], 100))
	hidden_layer_weights = np.random.uniform(-1000,1000,(100, 1))
	epochs = 1000
	size_of_input  = train_data.shape[1]
	size_of_hidden = 100
	size_of_output = 1

	while(epochs):
		epochs-= 1
		print "Epoch:\t",epochs
		for iterations in xrange(train_data.shape[0]): 
			# Forward Propagation
			X1 = train_data[iterations]
			
			S1 = np.dot(X1, input_layer_weights)
			X2 = activation(S1)
			
			S2 = np.dot(X2, hidden_layer_weights)
			X3 = activation(S2)
			
			# Prediction using sigmoid function
			if X3 >= 0.5:
				prediction = 1.0
			else:
				prediction = 0.0
			
			#Error : Least Square Error
			error = (prediction - train_label[iterations])**2

			#Backpropagation for final layer of weights
			final_delta_term1 = 2*(X3 - train_label[iterations])
			final_delta_term2 = X3*(1 - X3)
			final_delta       = final_delta_term1 * final_delta_term2
			gradient_final    = (learning_rate * final_delta) * X2
			#Gradient Descent for hidden layer weights
			for x in xrange(100):
				hidden_layer_weights[x]-= gradient_final[x]	 

			#Backpropagation for first layer of weights
			hidden_delta_term = sum(final_delta * hidden_layer_weights) * (X2 * (1-X2))
			#Gradient Descent for first layer of weights
			input_layer_weights -= learning_rate * X1.reshape([960,1]) * (hidden_delta_term.reshape([100,1]).T)

	np.savetxt('Weights_layer1', input_layer_weights)
	np.savetxt('Weights_layer2', hidden_layer_weights)



def test_function(test_data, test_label):
	input_layer_weights  = np.loadtxt('Weights_Layer1')
	hidden_layer_weights = np.loadtxt('Weights_Layer2')
	prediction = []
	for iterations in xrange(test_data.shape[0]):
			X1 = test_data[iterations]
			S1 = np.dot(X1, input_layer_weights)
			X2 = activation(S1)
			S2 = np.dot(X2, hidden_layer_weights)
			X3 = activation(S2)
			
			# Prediction using sigmoid function
			if X3 >= 0.5:
				prediction.append(1.0)
			else:
				prediction.append(0.0)
	prediction = np.asarray(prediction)
	accuracy = (prediction == test_label).sum()/float(prediction.size)
	print (accuracy * 100)


#Importing data for training
input_data = []
train_label = []
for lines in open(train,"r").readlines():
	input_data.append(read_pgm(lines.strip()))
	if 'down' in lines:
		train_label.append(1.0)
	else:
		train_label.append(0.0)
train_data = np.array(input_data, dtype = "float").reshape([len(input_data),32*30])
train_label = np.array(train_label)

#Importing data for Inference
input_test = []
test_label = []
for lines in open(test,"r").readlines():
	input_test.append(read_pgm(lines.strip()))
	if 'down' in lines:
		test_label.append(1.0)
	else:
		test_label.append(0.0)
test_data  = np.array(input_test, dtype = "float").reshape([len(input_test),32*30])
test_label = np.array(test_label)

#Uncomment the next line to start training the network
#train_function(train_data, train_label)

#Uncomment the next line to start the inference on the test data based on the weights saved in files "Weights_Layer1" 
#and "Weights_Layer2 which were learnt in the latest training pass"
test_function(test_data, test_label)









