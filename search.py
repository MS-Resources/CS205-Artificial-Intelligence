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
    return [s, s, w, s, w, w, s, w]


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
    "*** YOUR CODE HERE ***"
    #Note: Visit the Nodes first and then pop the stack

    #initialization
    stack = util.Stack()
    all_moves = {}
    needed_moves = []
    goal_state = -1
    
    visited = set()
    stack.push(problem.getStartState())  

    #Perform DFS traversal and record the moves
    while not stack.isEmpty():
        curr_state = stack.pop()
        visited.add(curr_state)
        
        if problem.isGoalState(curr_state): 
            goal_state = curr_state
            break

        successors = problem.getSuccessors(curr_state)

        #state = (loc, direction, cost)
        for state in successors:
            loc = state[0]

            if loc not in visited: 
                all_moves[loc] = [curr_state, state[1]]
                stack.push(loc)

    #Get the needed moves from source to goal (i.e perform backtracking to get moves)
    if goal_state != -1:
        curr_backtracked_state = goal_state

        while curr_backtracked_state in all_moves.keys():
            parent, direction = all_moves[curr_backtracked_state]
            needed_moves.append(direction)
            curr_backtracked_state = parent 


    #reverse the list to get the actual order
    return needed_moves[::-1] 

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    #Initialization
    queue = util.Queue()
    all_moves = {}
    needed_moves = []
    goal_state = -1

    visited = set()
    queue.push(problem.getStartState())
    visited.add(problem.getStartState())

    #Iterative BFS Traversal
    while not queue.isEmpty():
        curr_state = queue.pop()
        # visited.add(curr_state)
        
        if problem.isGoalState(curr_state): 
            goal_state = curr_state
            break

        successors = problem.getSuccessors(curr_state)

        #state = (loc, direction, cost)
        for state in successors:
            loc = state[0]

            if loc not in visited: 
                visited.add(loc)
                all_moves[loc] = [curr_state, state[1]]
                queue.push(loc)
    

    #Perform Backtracking
    if goal_state != -1:
        curr_backtracked_state = goal_state

        while curr_backtracked_state in all_moves.keys():
            parent, direction = all_moves[curr_backtracked_state]
            needed_moves.append(direction)
            curr_backtracked_state = parent 


    #return the moves
    return needed_moves[::-1]
    
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
