# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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
        util.raiseNotDefined()

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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    frontier = util.Stack()
    initialState = problem.getStartState()
    frontier.push( (initialState, [], []) )

    while not frontier.isEmpty():
        state, actions, explored = frontier.pop()

        goalState = problem.isGoalState(state)
        if goalState:
            return path

        successor = problem.getSuccessors(state)

        for neighbour, direction, steps in successor:
            if neighbour not in explored:
                actionsTemp = actions + [direction]
                exploredTemp = explored + [state]
                frontier.push((neighbour, actionsTemp , exploredTemp))
                path = actions + [direction]
                
    return []

def DFS(problem):

    """			 ******** Challenge 01: ********

    maxIteration = 20:
                    The pacman run and at one point it start moving in to and fro motion 
    and then stops. But it is still caught and dies.

    maxIteration = 30:
                    Similarly the pacman run and at one point it start moving in to and fro 
    motion and then stops. This time the count of its to and fro motion is more than that 
    with 20 iterations. But it is still caught and dies.

    maxIteration = 40:
                    The pacman run and at one point it start moving in to and fro motion 
    and then stops. But it is still caught and dies.


    It stucks because at one point we have to head towards west but it is moving towards east.
    So we also have to consider other chances of child.
    
			 ******** Challenge 02: ********
"""

    currentState = problem.getStartState()
    actions = []
    maxIteration = 0
    lastState = None
    
    while (maxIteration <= 40):
        children = problem.getSuccessors(currentState)
        for chances in children:
            if chances[0] != lastState:
                action = getActionFromTriplet(chances)
                lastState = currentState
                currentState = chances[0]
                break
        
        actions.append(action)
        maxIteration = maxIteration + 1
    return actions;

    
def getActionFromTriplet(triple):
    return triple[1];

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontier = util.Queue()
    initialState = problem.getStartState()
    child = []
    frontier.push( (initialState, [], []) )

    while not frontier.isEmpty():
        state, actions, explored = frontier.pop()

        if state not in child:
            child.append(state)

            goalState = problem.isGoalState(state)
            if goalState:
                return actions

            successor = problem.getSuccessors(state)

            for neighbour, direction, steps in successor:
                actionsTemp = actions + [direction]
                exploredTemp = explored + [state]
                frontier.push((neighbour, actionsTemp , exploredTemp))
                                    
    return []
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()
    initialState = problem.getStartState()
    child = []
    frontier.push( (initialState, [], 0), 0)

    while not frontier.isEmpty():
        state, actions, explored = frontier.pop()

        if state not in child:
            child.append(state)

            goalState = problem.isGoalState(state)
            if goalState:
                return actions

            successor = problem.getSuccessors(state)

            for neighbour, direction, steps in successor:
                actionsTemp = actions + [direction]
                costTemp = explored + steps
                frontier.push((neighbour, actionsTemp , costTemp), costTemp)
                
    return []
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    initialState = problem.getStartState()
    child = []
    frontier.push((initialState, [], 0), heuristic(initialState, problem))

    while not frontier.isEmpty():
        state, actions, explored = frontier.pop()

        if state not in child:
            child.append(state)

            goalState = problem.isGoalState(state)
            if goalState:
                return actions

            successor = problem.getSuccessors(state)

            for neighbour, direction, steps in successor:
                actionsTemp = actions + [direction]
                costTemp = explored + steps
                frontier.push((neighbour, actionsTemp , costTemp), costTemp + heuristic(neighbour, problem))

    return []

"****************** QUESTION 1 ***********************"
def mediumClassicSearch(problem):
    """
    Returns a sequence of moves that pacman eats one food.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    return  [e]

"****************** QUESTION 2 ***********************"
def mediumMazeSearch(problem):
    """
    Returns a sequence of moves that pacman eats food and completes the maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    return  [s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w, s, s, e, e, e, e, s, s, w, w, w, w, s, s, e, e, e, e, s, s, s, w, w, w, w, w, w, w, n, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, s, w, w, w, w, w, w, w, w, w]

"****************** QUESTION 3 ***********************"
def bigMazeSearch(problem):
    """
    Returns a sequence of moves that pacman eats food and completes the maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    return [n, n, w, w, w, w, n, n, w, w, s, s, w, w, w, w, w, w, w, w, w, w, w, w, w, w, n, n, e, e, n, n, w, w, n, n, n, n, n, n, e, e, e, e, e, e, s, s, e, e, n, n, e, e, e, e, n, n, e, e, s, s, e, e, n, n, n, n, n, n, e, e, e, e, n, n, n, n, n, n, n, n, n, n, w, w, s, s, w, w, w, w, s, s, s, s, s, s, w, w, s, s, s, s, w, w, n, n, w, w, w, w, w, w, w, w, w, w, w, w, n, n, e, e, n, n, n, n, n, n, e, e, e, e, e, e, n, n, n, n, n, n, n, n, w, w, w, w, w, w, s, s, w, w, w, w, s, s, s, s, e, e, s, s, w, w, w, w, w, w, w, w, w, w, s, s, s, s, s, s, s, s, s, s, e, e, s, s, s, s, w, w, s, s, s, s, e, e, s, s, w, w, s, s, s, s, w, w, s, s]

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
