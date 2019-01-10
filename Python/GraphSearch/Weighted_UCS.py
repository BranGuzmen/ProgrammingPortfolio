'''
HW1- Depth first search, breadth first search and uniform cost search
	Seperate documentation labeled HW1_Documentatoin.pdf was used to record any answers to questions, 
	results and any Python modules and functions used

This program will deal with questions regarding Graph 3 (G3). G3 is an undirected, weighted graph. 
	Representing G3 as a vertex-list and adjacency matrix, UCS will be carried out using a priority queue. 

The program will print out both the search state expanded (from start S to goal G) amd the search path returned
(also from S to G)

Bryan Guzman
Student ID: 001265918
ICSI435-Intro To AI
September 18th, 2018
'''
import collections
from queue import Queue, PriorityQueue


#Undirected, weighted Graph 3
g3_vertex_list = {'A':{('B', 2),('C', 2)},
	 			  'B':{('A', 2),('D', 1)},
	 			  'C':{('A', 2),('D', 8),('F', 3)},
	 			  'D':{('S', 3),('B', 1),('C', 8),('E', 2)},
	 			  'E':{('D', 2),('H', 8),('R', 2),('S', 9)},
	 			  'F':{('C', 3),('G', 2),('R', 2)},
	 			  'G':{('F', 2)},
	 			  'H':{('E', 8),('P', 4),('Q', 4)},
	 			  'P':{('H', 4),('Q', 15),('S', 1)},
	 			  'Q':{('H', 4),('P', 15)},
				  'R':{('E', 2),('F', 2)},
	 			  'S':{('D', 3),('E',9),('P', 1)}}


				 #A B C D E F G H P Q R S 
g3_adj_matrix = [[0,2,2,0,0,0,0,0,0,0,0,0],#A
				 [2,0,0,1,0,0,0,0,0,0,0,0],#B
				 [2,0,0,8,0,3,0,0,0,0,0,0],#C
				 [0,1,8,0,2,0,0,0,0,0,0,3],#D
				 [0,0,0,2,0,0,0,8,0,0,2,9],#E
				 [0,0,3,0,0,0,2,0,0,0,2,0],#F
				 [0,0,0,0,0,2,0,0,0,0,0,0],#G
				 [0,0,0,0,8,0,0,0,4,4,0,0],#H
				 [0,0,0,0,0,0,0,4,0,15,0,1],#P
				 [0,0,0,0,0,0,0,4,15,0,0,0],#Q
				 [0,0,0,0,2,2,0,0,0,0,0,0],#R
				 [0,0,0,3,9,0,0,0,1,0,0,0]]#S

#Directed, weighted Graph 4
g4_vertex_list = {'A':[],
				  'B':[('A', 2)],
				  'C':[('A', 2)],
				  'D':[('B', 1),('C', 8),('E',2)],
				  'E':[('H', 8),('R', 2)],
				  'F':[('C', 3),('G', 2)],
				  'G':[],
				  'H':[('P', 4),('Q', 4)],
				  'P':[('Q', 15)],
				  'Q':[],
				  'R':[('F', 2)],
				  'S':[('P', 1),('D', 3),('E', 9)]}

				 #A B C D E F G H P Q R S 
g4_adj_matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],#A
				 [2,0,0,0,0,0,0,0,0,0,0,0],#B
				 [2,0,0,0,0,0,0,0,0,0,0,0],#C
				 [0,1,8,0,2,0,0,0,0,0,0,0],#D
				 [0,0,0,0,0,0,0,8,0,0,2,0],#E
				 [0,0,3,0,0,0,2,0,0,0,0,0],#F
				 [0,0,0,0,0,0,0,0,0,0,0,0],#G
				 [0,0,0,0,0,0,0,0,4,4,0,0],#H
				 [0,0,0,0,0,0,0,0,0,15,0,0],#P
				 [0,0,0,0,0,0,0,0,0,0,0,0],#Q
				 [0,0,0,0,0,2,0,0,0,0,0,0],#R
				 [0,0,0,3,9,0,0,0,1,0,0,0]]#S



#UCS using Priority Queue on Vertex List
#Used to return the weight between nodes

def ucs_vertex_list(graph, start, goal):
	q = PriorityQueue()
	q.put((start,0)) #priority, node
	visited = []
	state=[start]

	while q:
		curr_node,ucs_weight = q.get()
		# print(curr_node)

		if curr_node not in visited:
			visited.append(curr_node)

		if curr_node == goal:
			# print(path)
			return visited,state

		# print(curr_node)
		for node,weight in graph[curr_node]:
			if node not in visited:
				# print(node,weight)
				state.append(node)
				q.put((node,weight))

	return visited,state

#UCS using Priority Queue on Adjacency Matrix
letter_list = ['A','B','C','D','E','F','G','H','P','Q','R','S']
def ucs_adjacency_list(graph, start, goal):
	q = PriorityQueue()
	visited=[start]
	state=[letter_list[start]]
	q.put((start,[start]))

	while q:
		curr_node,ucs_weight = q.get()

		if curr_node not in visited:
			visited.append(curr_node)

		if curr_node == goal:
			path = [letter_list[x] for x in visited]
			return path,state

		for edge in range(len(graph[0])):
			if graph[curr_node][edge]!=0 and edge not in visited:
				state.append(letter_list[edge])
				q.put((edge,[edge]))


def main():
	print("####################################################################################################################################")

	#Vertex list
	####################################################################################################################################
	#Graph 3
	ucs_vert_path,ucs_vert_states = ucs_vertex_list(g3_vertex_list,'S','G')
	# print(ucs_vert_path,ucs_vert_states)
	print("\nPriority Queue UCS Vertex List (Graph 3)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,ucs_vert_states)),"-".join(map(str,ucs_vert_path))))

	#Graph 4
	ucs_vert_path,ucs_vert_states = ucs_vertex_list(g4_vertex_list,'S','G')
	print("\nPriority Queue UCS Vertex List (Graph 4)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,ucs_vert_states)),"-".join(map(str,ucs_vert_path))))

	####################################################################################################################################

	#Graph 3
	ucs_adjacency_path,ucs_adjacency_states = ucs_adjacency_list(g3_adj_matrix,11,6)
	print("\nPriority Queue UCS Adjacency Matrix (Graph 3)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,ucs_adjacency_states)),"-".join(map(str,ucs_adjacency_path))))

	#Graph 4
	ucs_adjacency_path,ucs_adjacency_states = ucs_adjacency_list(g4_adj_matrix,11,6)
	print("\nPriority Queue UCS Adjacency Matrix (Graph 4)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,ucs_adjacency_states)),"-".join(map(str,ucs_adjacency_path))))	
	print("####################################################################################################################################")


if __name__ == '__main__':
	main()

