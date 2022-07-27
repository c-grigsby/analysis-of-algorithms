from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)



def helperFunction(myGraph, currentNode, visited, result):
    # Mark the current node as visited
    visited[currentNode] = True 
    # Recur for all the adjacent vertices of currentNode
    for i in myGraph.graph[currentNode]:
        if visited[i] == False:
            helperFunction(myGraph, i, visited, result)
    # Push current vertex to result
    result.insert(0, currentNode) 


def topologicalSort(myGraph):
    # Mark all the vertices as not visited
    visited = [False] * myGraph.vertices
    # Our stack to store the result/output  
    result = []  
    for currentNode in range(myGraph.vertices):
        if visited[currentNode] == False:
            helperFunction(myGraph, currentNode, visited, result)
    return (result)


# Create a graph given in the above diagram
myGraph = Graph(5)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)

print("Topological Sort")
print(topologicalSort(myGraph))