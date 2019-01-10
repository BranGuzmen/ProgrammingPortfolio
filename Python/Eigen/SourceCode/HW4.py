'''
Bryan Guzman
ICSI431 - Data Mining: Homework 4
Student ID: 001265918

Part C:

Encode Ls and L (you obtained above) into a python
program and perform eigen decomposition to obtain the eigenvectors corresponding to the smallest
non-zero eigenvalue of both L and Ls. (Hint: Use numpy:linalg:eig(X) to compute the eigen decom-
position of L and Ls.) Let u be the aforementioned eigenvector for L and us for LS. Report the values
corresponding to each nodes in u and us. Plot these values, where on the x axis you have the node id (1
to 6) and on the y axis you have the corresponding value of u and us.
'''

import numpy as np
from math import sqrt
import matplotlib.pyplot as plot



lap = np.array([
		[2,-1,-1,0,0,0],
	   	[-1,2,-1,0,0,0],
	    [-1,-1,3,-1,0,0],
	    [0,0,-1,21,-10,-10],
	    [0,0,0,-10,110,-100],
        [0,0,0,-10,-100,110]])

lap_sym = np.array([
		[1,-(1/sqrt(2*2)),-(1/sqrt(3*2)),0,0,0],
	   	[(-1/sqrt(2*2)),1,-(1/sqrt(3*2)),0,0,0],
	   	[-(1/sqrt(2*3)),-(1/sqrt(3*2)),1,-(1/sqrt(3*21)),0,0],
	   	[0,0,-(1/sqrt(21*3)),1,-(10/sqrt(21*110)),-(10/sqrt(21*110))],
	   	[0,0,0,-(10/sqrt(110*21)),1,-(100/sqrt(110*110))],
       	[0,0,0,-(10/sqrt(21*110)),-(100/sqrt(110*110)),1]
       	])

nodes = [1,2,3,4,5,6]

def score_plotter(graph,scores):
	'''
	Helper method to plot the scores for SVM, Gini, IG, and LDA on a bar graph.

	param:
	graph:
		The graph the data will be plotted to 
	scores:
		Values to be plotted on graph 
	'''
	for score,name in zip(scores,nodes):
		
		graph.plot(str(name),score,'-bs')


def min_index(eigen):
	x = 1
	for index,val in enumerate(eigen):
		if val > (10**-14):
			if val < x:
				x = val
				i = index
	return i



eig_lap_val,eig_lap_vec = np.linalg.eig(lap.T)
eig_sym_val,eig_sym_vec = np.linalg.eig(lap_sym.T)

print("Lapacian eigenvalues: \n{}\n\nSymetric Lapacian eigenvalues: \n{}\n".format(eig_lap_val,eig_sym_val))
eig_lap_min_index, eig_sym_min_index = min_index(eig_lap_val), min_index(eig_sym_val)
# print(eig_lap_min_index,eig_sym_min_index)

fig = plot.figure()
lap_graph = fig.add_subplot(121)
lap_graph.set_title('Lapacian Vector')
sym_graph = fig.add_subplot(122)
sym_graph.set_title('Symmetric Lapacian Vector')

print(eig_lap_vec[eig_lap_min_index],eig_sym_vec[eig_sym_min_index])
score_plotter(lap_graph,eig_lap_vec[eig_lap_min_index])
score_plotter(sym_graph,eig_sym_vec[eig_sym_min_index])


plot.tight_layout(w_pad=1.5,h_pad=2.0)
plot.show()
