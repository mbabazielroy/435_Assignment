from collections import deque
from pymaze import maze
from queue import PriorityQueue
def BFS(maze, start, goal):
    """
    This function implements a breadth first search algorithm to find the shortest path
    between start and goal cells in a maze. The algorithm works by exploring the
    maze layer by layer, starting from the start cell. The algorithm keeps track of the
    cells it has explored and the cells it has not explored yet. The algorithm
    terminates when it finds the goal cell.

    Parameters
    ----------
    maze : object
        The maze object to search in.
    start : tuple
        The coordinates of the start cell.
    goal : tuple
        The coordinates of the goal cell.

    Returns
    -------
    path : list
        A list of the coordinates of the cells in the shortest path from the start
        cell to the goal cell.

    """

    fringe = []
    explored = set()
    fringe.append(start)
    explored.add(start)
    parent = {}
    path = []
    while fringe:
        currCell = fringe.pop(0)
        if currCell == goal:
            while currCell != start:
                path.append(currCell)
                currCell = parent[currCell]
            path.append(start)
            path.reverse()
            return path
        for d in 'ESNW':
            if maze.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                if childCell in explored:
                    continue
                explored.add(childCell)
                fringe.append(childCell)
                parent[childCell] = currCell
    return path

# DFS --we need to check for cycles
def DFS(maze,start,goal):
    """
    This function implements a depth first search algorithm to find the shortest path
    between start and goal cells in a maze. The algorithm works by exploring the
    maze depth first, starting from the start cell. The algorithm keeps track of the
    cells it has explored and the cells it has not explored yet. The algorithm
    terminates when it finds the goal cell.

    Parameters
    ----------
    maze : object
        The maze object to search in.
    start : tuple
        The coordinates of the start cell.
    goal : tuple
        The coordinates of the goal cell.

    Returns
    -------
    path : list
        A list of the coordinates of the cells in the shortest path from the start
        cell to the goal cell.

    """
    stack = []
    explored = set()
    stack.append(start)
    explored.add(start)
    parent = {}
    path = []
    while stack:
        currCell = stack.pop()
        if currCell == goal:
            while currCell != start:
                path.append(currCell)
                currCell = parent[currCell]
            path.append(start)
            path.reverse()
            return path
        for d in 'ESNW':
            if maze.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                if childCell in explored:
                    continue
                explored.add(childCell)
                stack.append(childCell)
                parent[childCell] = currCell
    return path


# A*Search
# Heuristics
def heuristic(cell1, cell2):
    """
    This is a heuristic function which estimates the cost from cell1 to cell2
    as the Manhattan distance between cell1 and cell2.

    :param cell1: the start cell
    :param cell2: the goal cell
    :return: The estimated cost from cell1 to cell2
    """
    x1,y1 = cell1
    x2,y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def AStar(maze, start , goal):
    """
    This function implements the A* search algorithm to find the shortest path
    between start and goal cells in a maze.

    Parameters
    ----------
    maze : object
        The maze object to search in.
    start : tuple
        The coordinates of the start cell.
    goal : tuple
        The coordinates of the goal cell.

    Returns
    -------
    path : list
        A list of the coordinates of the cells in the shortest path from the start
        cell to the goal cell.

    """
    g_score = {cell:float('inf')for cell in maze.grid} # cost  of a movement from one cell to another
    g_score[start] = 0
    f_score = {cell:float('inf')for cell in maze.grid}
    f_score[start] = heuristic(start, goal)

    open = PriorityQueue()
    open.put((heuristic(start, goal),heuristic(start,goal),start))

    parent = {}

    while open:
        currCell = open.get()[2] # gets the third element inside the tuple e.g the returns start from line 161
        if currCell == goal:
            path = []
            while currCell != start:
                path.append(currCell)
                currCell = parent[currCell]
            path.append(start)
            path.reverse()
            return path
        for d in 'ESNW':
            if maze.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + heuristic(childCell, goal)

                if temp_f_score < f_score[childCell]:
                    f_score[childCell] = temp_f_score
                    g_score[childCell] = temp_g_score
                    parent[childCell] = currCell
                    open.put((temp_f_score,heuristic(childCell, goal),childCell))


def GS(maze,start, goal):
    """
    This function implements a Greedy Search algorithm to find the shortest path
    between start and goal cells in a maze. The algorithm works by exploring the
    maze, starting from the start cell. The algorithm keeps track of the cells it
    has explored and the cells it has not explored yet. The algorithm terminates
    when it finds the goal cell.

    Parameters
    ----------
    maze : object
        The maze object to search in.
    start : tuple
        The coordinates of the start cell.
    goal : tuple
        The coordinates of the goal cell.

    Returns
    -------
    path : list
        A list of the coordinates of the cells in the shortest path from the start
        cell to the goal cell.

    """

    f_score = {cell:float('inf')for cell in maze.grid}
    f_score[start] = heuristic(start, goal)

    open = PriorityQueue()
    open.put((heuristic(start,goal),start))

    parent = {}

    while open:
        currCell = open.get()[1] # gets the second element inside the tuple e.g the returns start from line 200
        if currCell == goal:
            path = []
            while currCell != start:
                path.append(currCell)
                currCell = parent[currCell]
            path.append(start)
            path.reverse()
            return path
        for d in 'ESNW':
            if maze.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                temp_f_score = heuristic(childCell, goal)

                if temp_f_score < f_score[childCell]:
                    f_score[childCell] = temp_f_score
                    parent[childCell] = currCell
                    open.put((temp_f_score,childCell))
