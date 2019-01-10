import numpy as np
import math
np.set_printoptions(threshold=np.nan)
def IG(D, index, value):
	"""Compute the Information Gain of a split on attribute index at value
	for dataset D.
	
	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the Information Gain for the given split
	"""
	X,y = D[0],D[1]
	pre_prob_y,pre_prob_n = [],[]
	# print(y.T.size, y.size)
	#Calculate entropy before split
	pre_prob_y = np.count_nonzero(y == 0)/y.size
	pre_prob_n = np.count_nonzero(y)/y.size
	pre_split_entropy = (-(pre_prob_y * math.log(pre_prob_y,2)) - (pre_prob_n * math.log(pre_prob_n,2)))

	# Split the data
	split_y, split_n = [],[]
	for val,tag in zip(X[:,index],y): # tag == class
		if val <= value:
			split_y.append(tag[0])
		else:
			split_n.append(tag[0])

	#Calculate H(Dy,Dn)
	# print(np.count_nonzero(np.asarray(split_y)==0),np.count_nonzero(split_y),np.count_nonzero(np.asarray(split_n) == 0),np.count_nonzero(split_n))
	# if len(split_y) == 0 or len(split_n) == 0:
	# 	return -1
	prob_y0 = np.count_nonzero(np.asarray(split_y) == 0)/y.size
	prob_y1 = np.count_nonzero(split_y)/y.size
	# print(len(split_n))
	prob_n0 = np.count_nonzero(np.asarray(split_y) == 0)/y.size
	prob_n1 = np.count_nonzero(split_n)/y.size

	if prob_y0 == 0 or prob_y1 == 0 or prob_n0 == 0 or prob_n1 == 0:
		return -1

	dy = (-(prob_y0 * math.log(prob_y0,2)) - (prob_y1 * math.log(prob_y1,2))) 
	dn = (-(prob_n0 * math.log(prob_n0,2)) - (prob_n1 * math.log(prob_n1,2)))

	h_dy_dn = ((len(split_y)/y.size) * dy) + ((len(split_n)/y.size) * dn)

	return (pre_split_entropy - h_dy_dn) #Directly return the Information gain


def G(D, index, value):
	"""Compute the Gini index of a split on attribute index at value
	for dataset D.

	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the Gini index for the given split
	"""
	X,y = D[0],D[1]
	split_y,split_n = [],[]

	#Perform the split
	for val,tag in zip(X[:,index],y): # tag == class
		if val <= value:
			split_y.append(tag[0])
		else:
			split_n.append(tag[0])

	#Count the number of 0 and 1 classes in splits	
	# print(np.count_nonzero(np.asarray(split_y)==0),np.count_nonzero(split_y),np.count_nonzero(np.asarray(split_n) == 0),np.count_nonzero(split_n))	
	prob_y0 = np.count_nonzero(np.asarray(split_y) == 0) / y.size
	prob_y1 = np.count_nonzero(split_y) / y.size
	prob_n0 = np.count_nonzero(np.asarray(split_n) == 0) / y.size
	prob_n1 = np.count_nonzero(split_n) / y.size

	#Calculate dy and dn
	dy = 1 - ((prob_y0*prob_y0) + (prob_y1*prob_y1))
	dn = 1 - ((prob_n0*prob_n0) + (prob_n1*prob_n1))

	GINI = (((len(split_y)/y.size) * dy) + ((len(split_n)/y.size) * dn)) 
	return GINI

def CART(D, index, value):
	"""Compute the CART measure of a split on attribute index at value
	for dataset D.

	Args:
		D: a dataset, tuple (X, y) where X is the data, y the classes
		index: the index of the attribute (column of X) to split on
		value: value of the attribute at index to split at

	Returns:
		The value of the CART measure for the given split
	"""
	X,y = D[0],D[1]
	split_y,split_n = [], []

	#Perform split
	for val, tag in zip(X[:,index],y): # tag == class
		if val <= value:
			split_y.append(tag[0])
		else:
			split_n.append(tag[0])

	#Count the number of 0 and 1 in split_y and split_n to calculate the probability
	# print(np.count_nonzero(np.asarray(split_y)==0),np.count_nonzero(split_y),np.count_nonzero(np.asarray(split_n) == 0),np.count_nonzero(split_n))
	if len(split_y) == 0 or len(split_n) == 0:
		return -1
	prob_y0 = np.count_nonzero(np.asarray(split_y) == 0) / len(split_y)
	prob_y1 = np.count_nonzero(split_y) / len(split_y)
	prob_n0 = np.count_nonzero(np.asarray(split_n) == 0) / len(split_n)
	prob_n1 = np.count_nonzero(split_n) / len(split_n)

	CART = (2 * ((len(split_y)/y.size) * (len(split_n)/y.size))) * (abs(prob_y0 - prob_n0) + abs(prob_y1 - prob_n1))
	return CART

#Use values already present in data
def bestSplit(D, criterion):
	"""Computes the best split for dataset D using the specified criterion

	Args:
		D: A dataset, tuple (X, y) where X is the data, y the classes
		criterion: one of "IG", "GINI", "CART"

	Returns:
		A tuple (i, value) where i is the index of the attribute to split at value
	"""

	#functions are first class objects in python, so let's refer to our desired criterion by a single name
	# X,y = D
	best_output,index,best_index,best_value = 0.0,0,0,0.0
	split_y,split_n = [],[]

	X,y=D[0],D[1]
	# print(X,y)

	if criterion == 'IG':
		for column in X.T:
			# print(column)
			for value in column:
				output = IG(D,index,value)
				
				if output > best_output:
					best_output = output
					best_value = value
					best_index = index
			index += 1
		# print(best_index,best_value)
		return best_index,best_value


	elif criterion == 'GINI':
		best_output = 1
		for column in X.T:
			for value in column:
				output = G(D,index,value)
	
				if output < best_output:	
					best_output = output
					best_value = value
					best_index = index
			index += 1
		# print(best_index,best_value)
		return best_index,best_value

	elif criterion == 'CART':
		for column in X.T:
			for value in column:
				output = CART(D,index,value)
				
				if output > best_output:					
					best_output = output
					best_value = value
					best_index = index
			index += 1
		# print(best_index,best_value)
		return best_index,best_value

	else:
		return ('Classiefiers present in this module are Information Gain (IG), Gini Index (GINI) and Cart (CART). Use one of the following.')



def load(filename):
	"""Loads filename as a dataset. Assumes the last column is classes, and 
	observations are organized as rows.

	Args:
		filename: file to read

	Returns:
		A tuple D=(X,y), where X is a list or numpy ndarray of observation attributes
		where X[i] comes from the i-th row in filename; y is a list or ndarray of 
		the classes of the observations, in the same order
	"""
	load_txt = np.loadtxt(filename,delimiter=',')
	return load_txt[:,0:9],load_txt[:,[10]]


def classifyIG(train, test):
	"""Builds a single-split decision tree using the Information Gain criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	split = []
	best_index,best_value = bestSplit(train,'IG')
	# print("Best Index:%s\nBest Value:%s\n"% (best_index,best_value))
	X,y = test[0],test[1]
	for val,tag in zip(X[:,best_index],y):
		if val <= best_value:
			split.append(0)
		else:
			split.append(1)
	return split


def classifyG(train, test):
	"""Builds a single-split decision tree using the GINI criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	split = []
	best_index,best_value = bestSplit(train,'GINI')
	# print("Best Index:%s\nBest Value:%s\n"% (best_index,best_value))
	X,y = test[0],test[1]
	for val,tag in zip(X[:,best_index],y):
		if val <= best_value:
			split.append(0)
		else:
			split.append(1)
	return split


def classifyCART(train, test):
	"""Builds a single-split decision tree using the CART criterion
	and dataset train, and returns a list of predicted classes for dataset test

	Args:
		train: a tuple (X, y), where X is the data, y the classes
		test: the test set, same format as train

	Returns:
		A list of predicted classes for observations in test (in order)
	"""
	split = []
	best_index,best_value = bestSplit(train,'CART')
	# print("Best Index:%s\nBest Value:%s\n"% (best_index,best_value))
	X,y = test[0],test[1]
	for val,tag in zip(X[:,best_index],y):
		if val <= best_value:
			split.append(0)
		else:
			split.append(1)
	return split


def main():
	"""This portion of the program will run when run only when main() is called.
	This is good practice in python, which doesn't have a general entry point 
	unlike C, Java, etc. 
	This way, when you <import HW2>, no code is run - only the functions you
	explicitly call.
	"""
	train,test = load('train.txt'),load('test.txt')
	ig,gini,cart = classifyIG(train,test),classifyG(train,test),classifyCART(train,test)
	X,y = test[0],test[1]
	print('Information Gain:\n%s\nTest:\n%s\nGini Index:\n%s\nTest:\n%s\nCart:\n%s\nTest:\n%s\n' % (ig,y.T[0],gini,y.T[0],cart,y.T[0]))
	# ig,gini,cart = IG(train,6,1.18),G(train,5,7.0),CART(train,2,0.0)


if __name__=="__main__": 
	"""__name__=="__main__" when the python script is run directly, not when it 
	is imported. When this program is run from the command line (or an IDE), the 
	following will happen; if you <import HW2>, nothing happens unless you call
	a function.
	"""
	main()