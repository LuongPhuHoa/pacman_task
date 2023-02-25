import util
import re
import sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class SingleFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 1
        self.expanded_states = []
        lines = startingGameState.split('\n')
        r = re.match('start_state:(.*)', lines[0])
        if r == None:
            print("Broken graph:")
            print('"""%s"""' % startingGameState)
            raise Exception("GraphSearch graph specification start_state not found or incorrect on line 0")
        self.start_state = r.group(1).strip()
        r = re.match('goal_states:(.*)', lines[1])
        if r == None:
            print("Broken graph:")
            print('"""%s"""' % startingGameState)
            raise Exception("GraphSearch graph specification goal_states not found or incorrect on line 1")
        goals = r.group(1).split()
        self.goals = [str.strip(g) for g in goals]
        self.successors = {}
        all_states = set()
        self.orderedSuccessorTuples = []
        for l in lines[2:]:
            if len(l.split()) == 3:
                start, action, next_state = l.split()
                cost = 1
            elif len(l.split()) == 4:
                start, action, next_state, cost = l.split()
            else:
                print("Broken graph:")
                print('"""%s"""' % startingGameState)
                raise Exception("Invalid line in GraphSearch graph specification on line:" + l)
            cost = float(cost)
            self.orderedSuccessorTuples.append((start, action, next_state, cost))
            all_states.add(start)
            all_states.add(next_state)
            if start not in self.successors:
                self.successors[start] = []
            self.successors[start].append((next_state, action, cost))
        for s in all_states:
            if s not in self.successors:
                self.successors[s] = []
        

    def getStartState(self):
        # TODO 1
        return self.start_state

    def isGoalState(self, state):
        # TODO 3
        return state in self.goals

    def getSuccessors(self, state):
        # TODO 4
        self.expanded_states.append(state)
        return list(self.successors[state])

    def getCostOfActions(self, actions):
        # TODO 5
        total_cost = 0
        state = self.start_state
        for a in actions:
            successors = self.successors[state]
            match = False
            for (next_state, action, cost) in successors:
                if a == action:
                    state = next_state
                    total_cost += cost
                    match = True
            if not match:
                print('invalid action sequence')
                sys.exit(1)
        return total_cost


class MultiFoodSearchProblem(SearchProblem):
    def __init__(self, startingGameState):
        # TODO 6
        pass
        

    def getStartState(self):
        # TODO 7
        pass

    def isGoalState(self, state):
        # TODO 8
        pass

    def getSuccessors(self, state):
        # TODO 9
        pass

    def getCostOfActions(self, actions):
        # TODO 10
        pass
