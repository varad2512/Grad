import re
import numpy as np

train = 'downgesture_train.list'
test  = 'downgesture_test.list'
#Binary prediction 1 for down gesture | 0 for any other gesture
classes = 2
learning_rate = 0.1

def activation(S, derivative = False):
	#Using sigmoid function
	
	if derivative:
		return ((np.exp(s) / (1 + np.exp(s))) - ((np.exp(s) / (1 + np.exp(s)))**2))
	
	return (np.exp(s) / (1 + np.exp(s)))

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

#initialization of weights for the input layer and the middle hidden layer
input_layer_weights  = np.random.uniform(-1000,1000,(train_data.shape[1], 100))
hidden_layer_weights = np.random.uniform(-1000,1000,(100, 1))
print input_layer_weights.shape
print hidden_layer_weights
epochs = 1000


while(epochs):
	epochs-= 1
	for iterations in xrange(train_data.shape[0]):
		# Forward Propagation
		X = train_data[iterations]
		S1 = activation(np.dot(X , input_layer_weights  ))
		S2 = activation(np.dot(S1, hidden_layer_weights ))
		# Prediction using sigmoid function
		if S2 >= 0.5:
			prediction = 1
		else:
			prediction = 0

		#Error : Least Square Error
		error = (prediction - train_label[iterations])**2

		#Backpropagation Algorithm for obtaining the gradients
		
		#Gradient for final layer
		delta_final  = S2
		delta_final_GD = np.dot(delta_final, S1)

		#Gradient for hidden layer
		delta_hidden = np.dot(np.dot(delta_final, hidden_layer_weights), activation(derivative = True))







