import sys
import time
import warnings
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

# Scoring for classifiers
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score

# Importing SVM, Decision Tree classifiers, LDA and Random Forest Classifier
from sklearn.svm import SVC as svm
from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as lda
from sklearn.ensemble import RandomForestClassifier as rfc

# Display all values present in numpy array
np.set_printoptions(threshold=np.nan)

# Set the window size for graph
fig_size = plot.rcParams['figure.figsize']
fig_size[0],fig_size[1] = 12,9
plot.rcParams['figure.figsize'] = fig_size

# Supress warnings from sklearn. Comment out if you want warnings
warnings.filterwarnings('ignore')

# Classifier names used for graph plotting and printing predictions
class_names = ['SVM','Gini','IG','LDA','Rand Forest']


# Method for plotting scores
def score_plotter(graph,scores):
	'''
	Helper method to plot the scores for SVM, Gini, IG, and LDA on a bar graph.

	param:
	graph:
		The graph the data will be plotted to 
	scores:
		Values to be plotted on graph 
	'''
	for score,name in zip(scores,class_names):
		graph.bar(name,score, width=0.8)


def load(filename):
	'''
	Loads a file based on the file name parameter. Assumes that the last column is classes and the 
	rest are data.

	Param: 
	filename:
		Name of file to be opened

	Return: 
	A tuple D=(X,y) where X is a numpy nxd array of observations attributes where X[i] comes from
	the it-th row in filename; y is 1 column of observations in the same order.
	'''
	classes = list()
	load_txt = np.loadtxt(filename,dtype=np.object,delimiter=',')

	for index in load_txt[:,-1]:
		if index == 'M':
			classes.append(0)
		else:
			classes.append(1)
	return load_txt[:,0:29],classes


def print_predictions(predictions,print_pred):
	'''
	Prints out the predictions of the classes for the dataset. Method also converts the classes from 0 and 1 to 
	M and B.

	Params:
	predictions:
		A list of lists containing the predictions for each classifier

	Return:
	Prints a list of classes converted from 0 and 1 to M and B
	'''
	letter_class = list()
	if print_pred:
		print('\n\nPrinting Predictions\n')
		for pred,clf in zip(predictions,class_names):
			for num in pred:
				if num == 0:
					letter_class.append('M')
				else:
					letter_class.append('B')
			print('\n{}:\n{d}'.format(clf,d=letter_class))
			del letter_class[:]
		print('\n')

	else:
		print('\n\nIf you want to see predictions, run program again with argument pred_print\n')


def print_scores(scores):
	'''
	Prints out the scores for Average precision, average recall and average F-measure. 

	Params:
	scores:
		A list of lists containing the scores for each score calculated. 

	Return:
		Prints the average precision, average recall and average F-measure for all the classifiers present in the program.
	'''
	score_names = ['Average Precsion Scores','Average Recall Score','Average F-Measure']

	for score,name in zip(scores,score_names):
		print('\n{}:\n'.format(name))
		for clf_score,clf in zip(score,class_names):
			print('{}: {:.4f}%'.format(clf,clf_score*100))

	
def classifier_plotter(X_train, y_train):
	'''
	Takes the training data and runs through SVM, DT-Gini and DT-IG with multiple C values and max_leaf_nodes to try.
	The method then creates a graph by taking the average of cross validation scores for that C value or max_leaf_node.

	Params:
	X_train: 
		List/s of features already standardized from the initial dataset
	y_train: 
		List of classifiers for X_train taken from the original dataset

	Return:
	Outputs a graph of the average cross validation scores.
	'''
	i,d = 1,0

	# Values to test 
	c_values = [0.01,0.1,1,10,100]
	k_values = [2,5,10,20]
	classifiers = ["SVM","DT-Gini & DT-IG"]

	for clf in classifiers:
		count = 1
		if clf == "SVM":
			if d == 0:
					ax = plot.subplot(231)
					ax.set_title(clf)
					plot.ylabel('F-measure')
					plot.xlabel('C values')
					d += 1
			print('SVM')
			for c in c_values:
				classi = svm(kernel='linear', C=c).fit(X_train,y_train)
				scores = cross_val_score(classi, X_train, y_train, cv=10)
				ax.plot(str(c),scores.mean(),'bs')
				print('%d.) %.4f%%' %(count,scores.mean()*100))
				count += 1
			plot.axis([None,None,0.90,1])
			print('\n')
			i += 1
			d = 0


		elif clf == "DT-Gini & DT-IG":
			count = 1
			if d == 0:
				ax = plot.subplot(232)
				plot.ylabel('F-measure')
				plot.xlabel('Max Leaf Nodes')
			print('    Gini\tIG')
			for k in k_values:
				gini_class,ig_class = dt(criterion='gini', max_leaf_nodes=k), dt(criterion='entropy', max_leaf_nodes=k)
				score_gini,score_ig = cross_val_score(gini_class, X_train, y_train, cv=10), cross_val_score(ig_class, X_train, y_train, cv=10)
				ax.plot(str(k), score_gini.mean(), 'r.', str(k), score_ig.mean(), 'g.')
				print('%d.) %.4f%%\t%.4f%%'%(count,score_gini.mean()*100,score_ig.mean()*100))
				count += 1
			plot.axis([None,None,0.889,0.96])	
			ax.legend(('Gini','IG'),loc=2)
			print('\n')	
			i += 1
			d = 0

		else:
			return "Should not get here."


def arguments(argv,train,test):
	'''
	Arguments will take any parameters passed along with the program and do one of five things:

	1.) Will use the raw dataset without any standardization in all classifier methods and graphs.
	2.) Will use a standardized dataset in all classifier methods and graphs.
	3.) Will print out predictions for the standardized data set or the raw dataset depending on if 
	    the arguement follows the first argument raw.
	4.) Return a message to console notifying the user that they did not pass a valid argument.
	5.) Use the standardized test set by default if no argument is provided. 

	For each case that the data is standardized, the test data will also be standardized.

	Params:
	argv:
		Any arguments passed from the console 
	train:
		Training data that will be standardized if asked 
	test:
		Test data that will be standardized if train is standardized

	Return:
	train:
		Either standardized data will be returned or the same dataset untouched will be returned depending on arguements
	test:
		If train has been returned standardized the so will test, otherwise it will be returned untouched
	print_pred:
		boolean returned True if predictions are to be printed, otherwise will be returned False
	'''
	if len(argv) >= 4:
		print('Too many arguemnts provided. Using standardized data and will not print out classifiers predictions')
		time.sleep(3)
		train,test = StandardScaler().fit_transform(train),StandardScaler().fit_transform(test)
		return train,test,False

	if len(argv) >= 2 and len(argv) < 3:

		if argv[1].lower() == 'raw':
			print('\n\nUsing un-standardized data for classification.\nThis will take a bit.\n\n')
			time.sleep(3)
			return train,test,False

		elif argv[1].lower() == 'standardized':
			print('\n\nUsing standardized data for classification.\n\n')
			time.sleep(3)
			train,test = StandardScaler().fit_transform(train),StandardScaler().fit_transform(test)
			return train,test,False

		elif argv[1].lower() == 'print_pred':
			print('\n\nWill print predictions for the classifiers on standardized dataset. Input print_pred after raw to print out its predictions\n\n')
			time.sleep(3)
			train,test = StandardScaler().fit_transform(train),StandardScaler().fit_transform(test)
			return train,test,True

		elif argv[1].lower() != 'standardized' or 'print_pred' or 'raw':
			print('\n\nYou are using an unrecognized command.\nPlease use one of the following:\nstandardized: Does classification on a standardized'
					'dataset.\nraw: Does classification on the raw dataset\nprint_pred: Prints predictions for all of the classifiers. (Can be used'
					' after standardized and raw to print their classifiers)')
			time.sleep(3)
			sys.exit('\n\nTerminating Program.\n\n')

	if len(argv) >= 3 and len(argv) < 4:
		if argv[1].lower() == 'raw' and argv[2].lower() == 'print_pred':
			print('\n\nUsing un-standardized data for classification and the predictions for all classifiers will be printed.\nThis will take a bit.\n\n')
			time.sleep(3)
			return train,test,True
		elif argv[1].lower() == 'standardized' and argv[2].lower() == 'print_pred':
			print('\n\nUsing standardized data for classification and the predictions for all classifiers wil be printed.\n\nNext time you can just input print_pred.\n\n')
			time.sleep(3)
			train,test = StandardScaler().fit_transform(train),StandardScaler().fit_transform(test)
			return train,test,True
		else:
			print('\n\nYou are using an unrecognized command.\nPlease use one of the following:\nstandardized: Does classification on a standardized'
					'dataset.\nraw: Does classification on the raw dataset\nprint_pred: Prints predictions for all of the classifiers. (Can be used'
					'after standardized and raw to print their classifiers)')
			time.sleep(3)
			sys.exit('\n\nTerminating Program.\n\n')

	if len(argv) <= 1:	
		print('\n\nUsing standardized data for classification by default since no aruguement was provided.\n\nEnter print_pred to print out predictions for classifiers using standardized data.' 
			  '\nEnter raw to use raw data for classification.\nEnter raw print_pred to print out predictions for classifiers using raw data\n\n')
		time.sleep(3)
		train,test = StandardScaler().fit_transform(train),StandardScaler().fit_transform(test)
		return train,test,False
	

def main():
	train,test = load("cancer-data-train.csv"),load("cancer-data-test.csv")
	X_train,y_train = train
	X_test,y_test = test
	X_train,X_test,print_pred = arguments(sys.argv,X_train,X_test)
	fig = plot.figure()

	# Passing training data and classes to find best C and number of leaf nodes to use. Also creating graphs to display this info		
	classifier_plotter(X_train, y_train)

	# Setting up graphs for each plot
	ax1 = fig.add_subplot(234)
	ax1.set_title('Average Precsion Scores')
	ax1.set_ylabel('Precsion Score')
	ax1.set_xlabel('Classifier')
	ax2 = fig.add_subplot(235)
	ax2.set_title('Average Recall Scores')
	ax2.set_ylabel('Recall Score')
	ax2.set_xlabel('Classifier')
	ax3 = fig.add_subplot(236)
	ax3.set_title('Average F-measures')
	ax3.set_ylabel('F-measure')
	ax3.set_xlabel('Classifier')

	# Create and train the classifiers
	classifier_svm,classifier_gini,classifier_ig,classifier_lda = svm(kernel='linear', C=0.1),dt(criterion='gini',max_leaf_nodes=10),dt(criterion='entropy',max_leaf_nodes=5),lda()
	classifier_svm.fit(X_train,y_train),classifier_gini.fit(X_train,y_train),classifier_ig.fit(X_train,y_train),classifier_lda.fit(X_train,y_train)

	# Make the predictions
	pred_svm,pred_gini,pred_ig,pred_lda = classifier_svm.predict(X_test),classifier_gini.predict(X_test),classifier_ig.predict(X_test),classifier_lda.predict(X_test) 
	
	# Calculate the precision, recall, f-measure
	avg_precision_svm,avg_precision_gini,avg_precision_ig,avg_precision_lda = average_precision_score(y_test,pred_svm),average_precision_score(y_test,pred_gini),average_precision_score(y_test,pred_ig),average_precision_score(y_test,pred_lda)
	recall_svm,recall_gini,recall_ig,recall_lda = recall_score(y_test,pred_svm, average='weighted'),recall_score(y_test,pred_gini, average='weighted'),recall_score(y_test,pred_ig, average='weighted'),recall_score(y_test,pred_lda, average='weighted')
	f_svm,f_gini,f_ig,f_lda = f1_score(y_test,pred_svm,average='weighted'),f1_score(y_test,pred_gini,average='weighted'),f1_score(y_test,pred_ig,average='weighted'),f1_score(y_test,pred_lda,average='weighted')


	################## Extra Credit #########################
	# Train classifier and make predictions on test set
	classifier_rfc = rfc(n_estimators=100,max_depth=2)
	classifier_rfc.fit(X_train,y_train)
	pred_rfc = classifier_rfc.predict(X_test)

	#Calculate precision, recall and f-measure for Random Forest Classifier
	avg_precision_rfc = average_precision_score(y_test,pred_rfc)
	recall_rfc = recall_score(y_test,pred_rfc,average='weighted')
	f_rfc = f1_score(y_test,pred_rfc,average='weighted')
	#########################################################

	# Printing scores and predictions
	print_scores([[avg_precision_svm,avg_precision_gini,avg_precision_ig,avg_precision_lda,avg_precision_rfc],[recall_svm,recall_gini,recall_ig,recall_lda,recall_rfc],[f_svm,f_gini,f_ig,f_lda,f_rfc]])
	print_predictions([pred_svm,pred_gini,pred_ig,pred_lda,pred_rfc],print_pred)

	# Create the graphs for the scores
	score_plotter(ax1,[avg_precision_svm,avg_precision_gini,avg_precision_ig,avg_precision_lda,avg_precision_rfc])
	score_plotter(ax2,[recall_svm,recall_gini,recall_ig,recall_lda,recall_rfc])
	score_plotter(ax3,[f_svm,f_gini,f_ig,f_lda,f_rfc])

	plot.tight_layout(w_pad=1.5,h_pad=2.0)
	plot.show()


if __name__ == '__main__':
	main()