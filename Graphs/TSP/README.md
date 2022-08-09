The Traveling Salesman Problem (TSP) is one of the most well-known NP-Complete problems. It has been intriguing scientists for more than a century. In simple language, the problem is: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"

Input: The input Graph is provided in the form of a 2-D matrix (adjacency matrix).
Consider the first node as the starting point.

Sample input:
```
G = [
[0, 2, 3, 20, 1],
[2, 0, 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0],
]
```
Output: A list of indices indicating the path taken. You must return the sequence of
nodes, the path taken starting from node 0. In this example, G is 5x5, indicating
there are 5 nodes in this graph: 0-4. You will always begin with node 0, and your
path should include every node exactly once, and only go between nodes with a
nonzero edge between them. You path will end at the starting node.

Sample output (For above graph G):
[0, 4, 3, 1, 2, 0]

Note: Not all graphs are fully connected. Some rows in G may have more than one 0.
These indicate absence of an edge.
