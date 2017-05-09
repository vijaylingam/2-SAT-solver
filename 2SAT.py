# 2SAT Problem
# Author: Vijay Lingam
# Date: April 24, 2017

import networkx as nx
from networkx.algorithms.components.strongly_connected import kosaraju_strongly_connected_components
import matplotlib.pyplot as plt
import graphviz as gv
from networkx.drawing.nx_agraph import graphviz_layout
import pycosat

graph = nx.DiGraph()
f = open('test.txt')
n = int(f.readline())
clauses = [[int(x) for x in line.split()] for line in f]

print("Number of Clauses: ", n)
print("Clauses: ", clauses)

for clause in clauses:
	graph.add_edge(-int(clause[0]), int(clause[1])) # (-x to y)
	graph.add_edge(-int(clause[1]), int(clause[0])) # (-y to x)

# Test case for SCC: should return [[0,1,2],[3],[4]]
# graph.add_edge(1, 0)
# graph.add_edge(0, 2)
# graph.add_edge(2, 1)
# graph.add_edge(0, 3)
# graph.add_edge(3, 4)

SCC = []
for element in nx.kosaraju_strongly_connected_components(graph):
	SCC.append(list(element))
print("Graph edges: ", graph.edges())
print("Strongly Connected Components: ", SCC)
for components in SCC:
	for element in components:
		if (element in components) and (-element in components):
			print("Not satisfiable because nodes", element, " and ", -element, " are in the same strongly connected component.")
			nx.draw(graph,pos=graphviz_layout(graph),node_size=1600, cmap=plt.cm.Blues,prog='dot', with_labels = True)
			plt.show()
			exit(1)
print("Satisfiable for the below values:")
solution = pycosat.solve(clauses)
for x in range(len(solution)):
	if solution[x] > 0:
		print("x",x+1,": True")
	else:
		print("x",x+1,": False")			
nx.draw(graph,pos=graphviz_layout(graph),node_size=1600, cmap=plt.cm.Blues,prog='dot', with_labels = True)
plt.show()

