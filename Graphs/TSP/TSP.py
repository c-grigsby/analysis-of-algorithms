def nearest_neighbor_heuristic(graph, startingNode):
    result = [startingNode]
    infinite = 2147483647
    vertices = len(graph[0])
    visited = [False for i in range(vertices)]
    visited[0] = True
    nextNode = startingNode
    edges = 0
    
    while edges < vertices - 1:
      minimum = infinite
      minRow = 0
      # the current column to explore for the lowest weighted edge
      column = nextNode
      # traverse down the column
      for row in range(len(graph[0])):
        if (not visited[row] and graph[row][column] > 0 and graph[row][column] < minimum):
          minimum = graph[row][column]
          minRow = row
          
      # add the node to the visited list
      visited[minRow] = True
      # next column to traverse 
      nextNode = minRow
      # append the node to the result path
      result.append(minRow)
      edges += 1
      
    return result


def solve_tsp(G):
  root = 0
  path = nearest_neighbor_heuristic(G, 0)
  # complete the cycle
  path.append(root)
  return path

if __name__ == "__main__":
  G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
    ]
  
  result = solve_tsp(G)
  print(result)