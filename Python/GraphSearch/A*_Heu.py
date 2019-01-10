'''
ICSI435 - Introduction to Artificial Intelligence: Homework 2, Informed Search

This program will impolement a heuristic and A* graph search on a 
graph provided in the word document "hw2.docx" found in the documentation folder
of this program. 
The graph will be represented using an adjacency list to represent the graph and the
final output will be the Expanded Search State and Path With Lowest Cost

This program uses Python 3.7.0

Bryan Guzman
Student ID: 001265918
ICSI435-Intro To AI
October 26th, 2018
'''

import collections 
from queue import PriorityQueue

# dictionary value tuple will follow this format: ('Next Node', Weight, Heuristic Value)
g1_adj_list = {'A':{('B', 2, 7), ('C', 2, 4)},
			   'B':{('A', 2, 5), ('D', 1, 7)},
			   'C':{('A', 2, 5), ('D', 8, 7), ('F', 3, 2)},
			   'D':{('B', 1, 7), ('C', 8, 4), ('E', 2, 5), ('S', 3, 6)},
			   'E':{('D', 2, 7), ('H', 8, 11), ('R', 2, 3), ('S', 9, 6)},
			   'F':{('C', 3, 4), ('G', 2, 0), ('R', 2, 3)},
			   'G':{('F', 2, 2)},
			   'H':{('E', 8, 5), ('P', 4, 14), ('Q', 4, 12)},
			   'P':{('H', 4, 11), ('Q', 15, 12), ('S', 1, 6)},
			   'Q':{('H', 4, 11), ('P', 15, 14)},
			   'R':{('E', 2, 5), ('F', 2, 2)},
			   'S':{('D', 3, 7), ('E', 9, 5), ('P', 1, 14)},
			   }


def greedy_search(graph, start, goal):
	pq = PriorityQueue()
	pq.put((start,6)) 
	visited = []
	came_from = {}
	came_from[start] = None

	while not pq.empty():
		current_node,heu = pq.get()

		if current_node not in visited:
			visited.append(current_node)

		if current_node == goal:
			break

		for next_node, weight, heuristic in graph[current_node]:
			if next_node not in visited and heuristic < heu:
				pq.put((next_node,heuristic))
				came_from[next_node] = current_node
	return came_from


def a_search(graph, start, goal):
	pq = PriorityQueue()
	pq.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not pq.empty():
		current_node = pq.get()

		if current_node == goal:
			break

		for next_node, weight, heuristic in graph[current_node]:
			new_cost = cost_so_far[current_node] + weight + heuristic

			if next_node not in came_from or new_cost < cost_so_far[next_node]:
				cost_so_far[next_node] = new_cost
				pq.put(next_node, new_cost)
				came_from[next_node] = current_node

	return came_from

# Used to recover the path using states returned from search
def reconstruct_path(came_from, start, goal):
	current_node = goal
	path = []

	while current_node != start:
		path.append(current_node)
		current_node = came_from[current_node]

	path.append(start)
	path.reverse()
	return path


def main():
	# Results from Greedy Search
	greedy_states = greedy_search(g1_adj_list,'S','G')
	greedy_path = reconstruct_path(greedy_states,'S','G')
	print("\nGreedy Search (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,greedy_states)),"-".join(map(str,greedy_path))))

	# Results from A* Search
	a_states = a_search(g1_adj_list,'S','G')
	a_path = reconstruct_path(a_states,'S','G')
	print("\nA* Search (Graph 1)\nState Expanded:\n%s\nPath Returned:\n%s\n" % (",".join(map(str,a_states)),"-".join(map(str,a_path))))


if __name__ == '__main__':
	main()
	