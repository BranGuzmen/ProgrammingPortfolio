'''
HW1- Depth first search, breadth first search and uniform cost search
	Seperate documentation labeled HW1_Documentatoin.pdf was used to record any answers to questions, 
	results and any Python modules and functions used

This program will deal with questions regarding Graph 1 (G1) and Graph 2 (G2). G1 is an undirected, unweighted graph. 
	G2 is a directed, unweighted graph. Representing G1 and G2 as a vertex-list and adjacency matrix, DFS using recursion 
	and a stack will be ran; along with a BFS using a queue. 

The program will print out both the search state expanded (from start S to goal G) amd the search path returned
(also from S to G)

Bryan Guzman
Student ID: 001265918
ICSI435-Intro To AI
September 18th, 2018
'''
import collections 

#Undirected, unweighted Graph 1
g1_vertex_list = {'A':set(['B','C']),
				  'B':set(['A','D']),
				  'C':set(['A','D','F']),
				  'D':set(['B','C','E','S']),
				  'E':set(['D','H','R','S']),
				  'F':set(['C','G','R']),
				  'G':set(['F']),
				  'H':set(['E','P','Q']),
				  'P':set(['H','Q','S']),
				  'Q':set(['H','P']),
				  'R':set(['E','F']),
				  'S':set(['D','E','P'])}

				 #A B C D E F G H P Q R S
g1_adj_matrix = [[0,1,1,0,0,0,0,0,0,0,0,0],#A
				 [1,0,0,1,0,0,0,0,0,0,0,0],#B
				 [1,0,0,1,0,1,0,0,0,0,0,0],#C
				 [0,1,1,0,1,0,0,0,0,0,0,1],#D
				 [0,0,0,1,0,0,0,1,0,0,1,1],#E
				 [0,0,1,0,0,0,1,0,0,0,1,0],#F
				 [0,0,0,0,0,1,0,0,0,0,0,0],#G
				 [0,0,0,0,1,0,0,0,1,1,0,0],#H
				 [0,0,0,0,0,0,0,1,0,1,0,1],#P
				 [0,0,0,0,0,0,0,1,1,0,0,0],#Q
				 [0,0,0,0,1,1,0,0,0,0,0,0],#R
				 [0,0,0,1,1,0,0,0,1,0,0,0]]#S

#Directed, unweighthed Graph 2
g2_vertex_list = {'A':set([]),
				  'B':set(['A']),
				  'C':set(['A']),
				  'D':set(['B','C','E']),
				  'E':set(['H','R']),
				  'F':set(['C','G']),
				  'G':set([]),
				  'H':set(['P','Q']),
				  'P':set(['Q']),
				  'Q':set([]),
				  'R':set(['F']),
				  'S':set(['D','E','P'])}

				 #A B C D E F G H P Q R S
g2_adj_matrix = [[0,0,0,0,0,0,0,0,0,0,0,0],#A
				 [1,0,0,0,0,0,0,0,0,0,0,0],#B
				 [1,0,0,0,0,0,0,0,0,0,0,0],#C
				 [0,1,1,0,1,0,0,0,0,0,0,0],#D
				 [0,0,0,0,0,0,0,1,0,0,1,0],#E
				 [0,0,1,0,0,0,1,0,0,0,0,0],#F
				 [0,0,0,0,0,0,0,0,0,0,0,0],#G
				 [0,0,0,0,0,0,0,0,1,1,0,0],#H
				 [0,0,0,0,0,0,0,0,0,1,0,0],#P
				 [0,0,0,0,0,0,0,0,0,0,0,0],#Q
				 [0,0,0,0,0,1,0,0,0,0,0,0],#R
				 [0,0,0,1,1,0,0,0,1,0,0,0]]#S

letter_list = ['A','B','C','D','E','F','G','H','P','Q','R','S']


#Returns the shortest path from list and adds formatting for state expanded and path returned 
#Returns two string variables 
def shortest_path(path_list):
	min_list=[]
	min_length = min(map(len,path_list))
	for inner_list in path_list:
		if len(inner_list) == min_length:
			min_list.append(inner_list)
			# print(min_list)		
	# print(min_list)
	path = ["-".join(map(str,x)) for x in min_list]#deliminates each list entry with a "," and makes a new list of strings
	return path

#Stack DFS vertex list
#Return a list of path and states
def dfs_stack(graph, start, goal):
	visited = []
	states = []
	visited.append(start)
	stack = [start]

	while stack:
		node = stack.pop()
		states.append(node)

		if node not in visited:
			visited.append(node)

		if node == goal:
			return states,visited

		for edge in graph[node]:
			if edge not in visited:
				stack.append(edge)
	return states,visited


#Recursive DFS vertex list
#Return a list of all possible paths
def dfs_recursive_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_recursive_paths(graph, next, goal, path + [next])

def dfs_recursive_states(graph, start, visited=None): #Need a second variable to track actual path 
	if visited is None:
		visited=[]

	visited.append(start)

	for node in graph[start]:
		if node not in visited:
			visited = dfs_recursive_states(graph,node,visited)

	return visited
 
#Queue BFS vertex list
#Expanded States
def bfs_queue_expanded(graph, start, goal, path=[]):
    visited, queue = set([start]), collections.deque([start]) #Have to put start in visited set since it starts there
    while queue: 
        vertex = queue.popleft() 
        path.append(vertex)
        # print(vertex)
        for neighbour in graph[vertex]: #Find all connected nodes to vertex
            if neighbour not in visited: 
                visited.add(neighbour)
                # print(neighbour)
                queue.append(neighbour)
        if vertex == goal:
        	return path 
    return path
#Path returned
def bfs_queue_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next] #use a generator to continue finding paths
            else:
                queue.append((next, path + [next]))

#Stack DFS adjacency matrix 
#DFS path and expanded states returned
def dfs_stack_adj(graph, start, goal, path=None,states=[]): #Starting element is 11
	stack=[start]
	if path == None:
		path=[]
	visited=[False]*len(graph) 
	while len(stack)!=0: 
		node=stack.pop()
		states.append(letter_list[node])

		if node == goal:
			path.append(letter_list[node])
			return path,states

		if visited[node]==False: 
			visited[node]=True
			path.append(letter_list[node]) #letter_list can be found after the adjacency matrices
	
			for edge in range(len(graph[0])): #iterate through column looking for 1's 
				if graph[node][edge]!=0: #
					stack.append(edge) #push index on to the stack

#Recursion DFS adjacency matrix
dfs_recursive_adj_states=[]
def dfs_recursive_adj(graph, curr_node, goal, visited=None,path=None): 
	if visited is None:
		visited=[False]*len(graph)
	if path is None:
		path=[]
	
	if visited[curr_node]==False:
		visited[curr_node]=True
		path.append(letter_list[curr_node])#letter_list can be found after the adjacency matrices

		if curr_node == goal:
			global dfs_recursive_adj_states
			dfs_recursive_adj_states = path.copy()

		#Goes through indexes 0-11 looking for 1's
		for node in range(len(graph[0])):
			if graph[curr_node][node]!=0 and visited[node]==False: 
				dfs_recursive_adj(graph,node,goal,visited,path)			
	return path

#Queue BFS adjacency matrix
#BFS path returned and expanded states
def bfs_queue_adj_states_path(graph, start,goal, visited=None,path=[],states=[]):
	if visited is None:
		visited=[False]*len(graph)

	queue = collections.deque([start])
	if len(states)==0:
		states.append(letter_list[start])
	while queue:
		node = queue.popleft()

		if visited[node]==False:
			visited[node]=True
			path.append(letter_list[node])
			for edge in range(len(graph[0])):
				if graph[node][edge]!=0 and visited[edge]==False:
					queue.append(edge)
					states.append(letter_list[edge])

	return path,states


def main():
	print("####################################################################################################################################")
	#Vertex list
	################################################################## GRAPH 1 ##################################################################
	dfs_st_states,dfs_st_path = dfs_stack(g1_vertex_list, 'S', 'G')#states path returned
	print("\nStack DFS Vertex List (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,dfs_st_states)),"-".join(map(str,dfs_st_path))))
	

	dfs_rec_path = shortest_path(list(dfs_recursive_paths(g1_vertex_list, 'S', 'G')))
	dfs_rec_states = dfs_recursive_states(g1_vertex_list,'S')
	print("\n\nRecursive DFS Vertex List (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,dfs_rec_states)),dfs_rec_path))

	bfs_q_expanded = bfs_queue_expanded(g1_vertex_list,'S','G')
	bfs_q_path = shortest_path(list(bfs_queue_paths(g1_vertex_list,'S','G')))
	print("\nQueue BFS Vertex List (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,bfs_q_expanded)),bfs_q_path))



	################################################################## GRAPH 2 ##################################################################
	dfs_st_states,dfs_st_path = dfs_stack(g2_vertex_list, 'S', 'G')
	print("\nStack DFS Vertex List (Graph 2)\nState Expanded:\n%s\nPath Expanded:\n%s\n" % (",".join(map(str,dfs_st_states)),"-".join(map(str,dfs_st_path))))

	dfs_rec_path = shortest_path(list(dfs_recursive_paths(g2_vertex_list, 'S', 'G')))
	dfs_rec_states = dfs_recursive_states(g2_vertex_list,'S')
	print("\n\nRecursive DFS Vertex List (Graph 2)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,dfs_rec_states)),dfs_rec_path))

	bfs_q_expanded = bfs_queue_expanded(g2_vertex_list,'S','G')
	bfs_q_path = shortest_path(list(bfs_queue_paths(g2_vertex_list,'S','G')))
	print("\nQueue BFS Vertex List (Graph 2)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,bfs_q_expanded)),bfs_q_path))







	#Adjacent Matrix
	################################################################## GRAPH 1 ##################################################################
	dfs_st_path,dfs_st_states = dfs_stack_adj(g1_adj_matrix,11,6)#path state returned
	print("\nStack DFS Adjacency List (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,dfs_st_states)),"-".join(map(str,dfs_st_path))))

	dfs_rec_path = dfs_recursive_adj(g1_adj_matrix,11,6)#path returned 
	print("\nRecursive DFS Adjacency List (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,dfs_rec_path)),"-".join(map(str,dfs_recursive_adj_states))))
		

	bfs_queue_adj_path,bfs_queue_adj_expanded = bfs_queue_adj_states_path(g1_adj_matrix,11,6)#path state returned 
	print("\nQueue BFS Adjacency List (Graph 1)\nState Expanded\n%s\nPath Returned:\n%s\n\n" %(",".join(map(str,bfs_queue_adj_expanded)),"-".join(map(str,bfs_queue_adj_path))))


	################################################################## GRAPH 2 ##################################################################
	dfs_st_path,dfs_st_states = dfs_stack_adj(g2_adj_matrix,11,6)#path state returned
	print("\nStack DFS Adjacency List (Graph 2)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,dfs_st_states)),"-".join(map(str,dfs_st_path))))

	dfs_rec_path = dfs_recursive_adj(g2_adj_matrix,11,6)#path
	print("\nRecursive DFS Adjacency List (Graph 2)\nState Expanded:\n%s\nPath Returned:\n%s\n\n" % (",".join(map(str,dfs_rec_path)),"-".join(map(str,dfs_recursive_adj_states))))

	bfs_queue_adj_path,bfs_queue_adj_expanded = bfs_queue_adj_states_path(g2_adj_matrix,11,6)#path state returned 
	print("\nQueue BFS Adjacency List (Graph 2)\nState Expanded\n%s\nPath Returned:\n%s\n\n" %(",".join(map(str,bfs_queue_adj_expanded)),"-".join(map(str,bfs_queue_adj_path))))
	print("####################################################################################################################################")


if __name__ == '__main__':
	main()














				 