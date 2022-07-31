import queue

def updateCoordinates(move, current_coordinates):
    row = current_coordinates[0]
    column = current_coordinates[1]
    
    if move == "L":
        column -= 1

    elif move == "R":
        column += 1

    elif move == "U":
        row -= 1

    elif move == "D":
        row += 1
        
    return (row, column)
    

def getCoordinates(path, source):
    row = source[0]
    column = source[1]
    
    for move in path:
        if move == "L":
          column -= 1

        elif move == "R":
          column += 1

        elif move == "U":
          row -= 1

        elif move == "D":
          row += 1
    
    return (row, column)

def getNodesVisited(path, source):
    nodesVisited = []
    row = source[0]
    column = source[1]
    nodesVisited.append((row, column))
    
    for move in path:
        if move == "L":
            column -= 1

        elif move == "R":
            column += 1

        elif move == "U":
            row -= 1

        elif move == "D":
            row += 1
        
        nodesVisited.append((row, column))
    
    return nodesVisited


def valid(maze, visited, coordinates):
    row = coordinates[0]
    column = coordinates[1]
    # ensure valid position in the maze
    if not(0 <= column < len(maze[0]) and 0 <= row < len(maze)):
        return False
    # ensure not an obstacle
    elif (maze[row][column] == "#"):
        return False
    # ensure new position has not been previously visited
    if (visited[row][column] == True):
        return False
    # mark the node as visited
    visited[row][column] = True
    return True


def findEnd(destination, coordinates):
    if coordinates[0] == destination[0] and coordinates[1] == destination[1]: return True
    return False


# main algorithm
def solve_puzzle(board, source, destination): 
  visited = [[False for i in board[0]] for i in board]
  visited[source[0]][source[1]] = True
  pathQ = queue.Queue()
  pathQ.put("")
  maze = board

  while pathQ.qsize() > 0:
    path = pathQ.get()
    current_coordinates = getCoordinates(path, source)
    
    if (findEnd(destination, current_coordinates)): 
        return getNodesVisited(path, source), path
    
    for move in ["L", "R", "U", "D"]:
        newPath = path + move
        potential_coordinates = updateCoordinates(move, current_coordinates)
        if valid(maze, visited, potential_coordinates):
            pathQ.put(newPath)
          
  return None

if __name__ == "__main__":   
  puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
  ]  
  source = (0,2)
  destination = (4, 2)
  print(solve_puzzle(puzzle, source, destination))