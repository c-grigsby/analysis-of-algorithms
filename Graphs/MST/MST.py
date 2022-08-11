def prims(graph):
    result = []
    INF = 9999999
    # number of vertices (columns) in the graph
    V = len(graph[0])
    print(V)
    # create a array to track selected vertex, selected will become true 
    selected = [0 for i in range(V)]
    selected[0] = True
    # set number of edge to 0
    num_edges = 0
    # print for edge and weight
    print("Edge : Weight\n")
    while (num_edges < V - 1):
        # For every vertex in the set, find the all adjacent vertices
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    # not already selected and there is an edge and the edge weight < current min
                    if ((not selected[j]) and graph[i][j] and graph[i][j] < minimum):
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(graph[x][y]))
        result.append((x, y, graph[x][y]))
        selected[y] = True
        num_edges += 1

    return result

if __name__ == "__main__":
    graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
    ]
    result = prims(graph)
    print(result)