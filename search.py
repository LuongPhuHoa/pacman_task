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
    frontier = util.Stack()
    #previously explored states (for path checking), holds states
    exploredNodes = []
    #define start node
    startState = problem.getStartState()
    startNode = (startState, [])
    
    frontier.push(startNode)
    
    while not frontier.isEmpty():
        #begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()
        
        if currentState not in exploredNodes:
            #mark current node as explored
            exploredNodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions
            else:
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)
    return actions 

def breadthFirstSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 18
    frontier = util.Queue()
    #previously explored states (for path checking), holds states
    exploredNodes = []
    #define start node
    startState = problem.getStartState()
    startNode = (startState, [])
     
    frontier.push(startNode)
    
    while not frontier.isEmpty():
        #begin exploring last (most-recently-pushed) node on frontier
        currentState, actions = frontier.pop()
        
        if currentState not in exploredNodes:
            #mark current node as explored
            exploredNodes.append(currentState)
            
            if problem.isGoalState(currentState):
                return actions
            else:
                #get list of possible successor nodes in 
                #form (successor, action, stepCost)
                successors = problem.getSuccessors(currentState)
                
                #push each successor to frontier
                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newNode = (succState, newAction)
                    frontier.push(newNode)
    return actions

def uniformCostSearch(problem):
    '''
    return a path to the goal
    '''
    # TODO 19


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
    pass


def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    return a path to the goal
    '''
    # TODO 22


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
