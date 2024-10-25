import sys
from SearchSolution import BFS, DFS, AStar, GS
import pymaze as maze
import random

def random_cell_position(m):
    """ Returns a random cell position in the given maze m. """
    return (random.randint(0, m.rows - 1), random.randint(0, m.cols - 1))

def gen_goal_agent(m):
    """
    Generates a random goal and agent position in the given maze m.

    The positions are chosen so that the agent and goal are not in the same cell.

    Returns: (goal_position, agent_position)
    """
    goal_position = random_cell_position(m)
    agent_position = random_cell_position(m)
    while agent_position == goal_position:
        agent_position = random_cell_position(m)
    return goal_position, agent_position

def main():
    # Check if the correct number of arguments is provided
    """
    The main function to execute the MazeRunner program.

    This function initializes a maze with specified dimensions and uses a chosen
    search method to find a path from a randomly placed agent to a goal. The
    search methods available are BFS, DFS, GS, and AStar. The function also
    handles command-line arguments, validates input, and traces the path found.

    Command-line arguments:
    M (int): Number of rows in the maze.
    N (int): Number of columns in the maze.
    searchmethod (str): The search algorithm to use ('BFS', 'DFS', 'GS', or 'AStar').

    Raises:
    ValueError: If the input arguments are not valid integers or if the search
    method is not one of the specified options.
    """
    if len(sys.argv) != 5:
        print("Usage: MazeRunner.py [M] [N] [searchmethod] [searchmethod2]")
        sys.exit(1)

    # Parse command line arguments
    try:
        M = int(sys.argv[1])
        N = int(sys.argv[2])
        search_method = sys.argv[3]
        search_method2 = sys.argv[4]
    except ValueError:
        print("M and N must be integers.")
        sys.exit(1)

    if search_method not in {"BFS", "DFS", "GS", "AStar"}:
        print("Search method must be one of: BFS, DFS, GS, AStar.")
        sys.exit(1)

    if search_method2 not in {"BFS", "DFS", "GS", "AStar"}:
        print("Search method must be one of: BFS, DFS, GS, AStar.")
        sys.exit(1)

    # Create the maze
    m = maze.maze(M, N)
    m.CreateMaze(theme=maze.COLOR.light, loopPercent=100, pattern='h')

    # Generate random goal and agent positions
    goal_position, agent_position = gen_goal_agent(m)

    # Create the agent
    a = maze.agent(m, *agent_position, goal=goal_position, footprints=True, color=maze.COLOR.blue, filled=True)

    # Get the start and goal positions
    start = a.position
    goal = a.goal

    millie = maze.agent(m, *a.position, goal=a.goal, footprints=True, color=maze.COLOR.red, filled=True)

    # Run the selected search method
    search_methods = {
        "BFS": BFS,
        "DFS": DFS,
        "GS": GS,
        "AStar": AStar
    }
    path = search_methods[search_method](m, start, goal)
    path2 = search_methods[search_method2](m, start, goal)

    # Trace the path if found
    if path:
        m.tracePath({a: path})
    else:
        print("No path found.")

    if path2:
        m.tracePath({millie: path2})
    else:
        print("No path found.")
    # Run the maze
    m.run()

if __name__ == "__main__":
    main()
