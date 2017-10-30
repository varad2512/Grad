import re
import numpy as np
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
    """Return image data from a raw PGM file as np array.

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
	epochs = 1 #TODO 1000
	size_of_input  = train_data.shape[1]
	size_of_hidden = 100
	size_of_output = 1

	while(epochs):
		epochs-= 1
		for iterations in xrange(1): #TODO train_data.shape[0]):
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

			#Backpropagation for hidden layer
			final_delta_term1 = 2*(X3 - train_label[iterations])
			final_delta_term2 = X3*(1 - X3)
			final_delta       = final_delta_term1 * final_delta_term2c
			gradient_final    = (learning_rate * final_delta) * X2

			#Gradient Descent for hidden layer weights

			for x in xrange(100):
				hidden_layer_weights[x]-= gradient_final[x]	 

			


			'''
			#Backpropagation Algorithm for obtaining the gradients
			
			#Gradient for final layer
			delta_final     = S2
			delta_final_GD  = delta_final * S1

			#Gradient for hidden layerc
			delta_hidden    = np.dot((delta_final * hidden_layer_weights).T, activation(S1, derivative = True))
			delta_hidden_GD = delta_hidden * X
			print delta_hidden_GD.shape

			#Gradient Descent for hidden layer and final layer weights
			hidden_layer_weights -=  learning_rate * delta_final_GD.reshape([100,1])
			input_layer_weights  -=  learning_rate * delta_hidden_GD

			'''


	#pprint(hidden_layer_weights)





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


train_function(train_data, train_label)









