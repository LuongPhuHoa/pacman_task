import util
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from game import Directions

n = Directions.NORTH
s = Directions.SOUTH
e = Directions.EAST
w = Directions.WEST


def depthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 17
    forDFS = util.Stack()

    #Getting starting point
    startLocation = problem.getStartState()

    # Defining Root Node => (location, path)
    rootNode = (startLocation, [])

    #Pushing root to stack
    forDFS.push(rootNode)

    #Defining a set for visited nodes
    visitedLocations = set()

    while not forDFS.isEmpty():
        # node[0] : location, node[1] : path(NEWS)

        #pop latest node as current node
        node = forDFS.pop()

        #adding current node to visited ones
        visitedLocations.add(node[0])

        #check whether current node is goal or not
        if problem.isGoalState(node[0]):
            return node[1]

        #find successors of current node
        successors = problem.getSuccessors(node[0])

        for item in successors:
            #checking whether successor has been visited or not
            if item[0] in visitedLocations:
                continue
            #pushining unvisited ones as nodes to stack
            forDFS.push((item[0], node[1] + [item[1]]))

    return None

def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    forBFS = util.Queue()

    # Getting starting node
    startLocation = problem.getStartState()

    #Setting Root Node
    rootNode = (startLocation, [])

    #adding root node to queue
    forBFS.push(rootNode)

    #Defining a set for visited nodes
    visitedLocations = set()

    #adding starting point to that set
    visitedLocations.add(startLocation)

    while not forBFS.isEmpty():
        # node[0] : location, node[1] : path (NEWS)
        #Setting latest node as current one
        node = forBFS.pop()

        #checking whether current node is goal
        if problem.isGoalState(node[0]):
            return node[1]

        #getting current node successors
        successors = problem.getSuccessors(node[0])

        #adding successors to queue if they are not visited
        for item in successors:
            if item[0] in visitedLocations:
                continue
            visitedLocations.add(item[0])
            forBFS.push((item[0], node[1] + [item[1]]))

    return None

def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19
    forUCS = util.PriorityQueue()

    #Getting starting point
    startLocation = problem.getStartState()

    # (location, path, cost)
    rootNode = (startLocation, [], 0)

    #adding root to priority queue and visited locations
    forUCS.push(rootNode, 0)
    visitedLocations = set()

    while not forUCS.isEmpty():
        # node[0] : location, node[1] : path, node[2] : cost
        #setting latest node as current one
        node = forUCS.pop()

        #checking whether if current node is goal or not
        if problem.isGoalState(node[0]):
            return node[1]

        #adding current node to visited ones and checking for its successors
        if node[0] not in visitedLocations:
            visitedLocations.add(node[0])
            for successor in problem.getSuccessors(node[0]):
                if successor[0] not in visitedLocations:
                    cost = node[2] + successor[2]
                    forUCS.push((successor[0], node[1] + [successor[1]], cost), cost)

    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def singleFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of single food search
    """
    # TODO 20
    pass


def multiFoodSearchHeuristic(state, problem=None):
    """
    A heuristic function for the problem of multi-food search
    """
    # TODO 21
    position, foodGrid = state
    foods = foodGrid.asList()
    #if there is no food then return 0
    if not foods:
        return 0

    farFood = 0
    for food in foods:
        key = position + food
        if key in problem.heuristicInfo:
            distance = problem.heuristicInfo[key]
        else:
            # Use manhattan distance 
            distance = mazeDistance(position, food, problem.startingGameState)
            problem.heuristicInfo[key] = distance

        if distance > farFood:
            farFood = distance

    return farFood


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22
    forAstar = util.PriorityQueue()

    #Getting start location
    startLocation = problem.getStartState()

    #Setting root node
    rootNode = (startLocation, [], 0)
    forAstar.push(rootNode, 0)
    visitedLocations = set()

    while not forAstar.isEmpty():
        # node[0] : location,node[1] : path,node[2] : cumulative cost
        #current node
        node = forAstar.pop()

        #checking whether current node is goal or not
        if problem.isGoalState(node[0]):
            return node[1]

        #adding to visited nodes
        if node[0] not in visitedLocations:
            visitedLocations.add(node[0])
            for successor in problem.getSuccessors(node[0]):
                if successor[0] not in visitedLocations:
                    cost = node[2] + successor[2]
                    #f function
                    totalCost = cost + heuristic(successor[0], problem)
                    forAstar.push((successor[0], node[1] + [successor[1]], cost), totalCost)

    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
