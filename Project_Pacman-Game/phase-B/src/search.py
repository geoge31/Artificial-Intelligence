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

    "*** YOUR CODE HERE ***"
    """
       - An empty list is diclared named isVisited to store the nodes that will be visited 
       - the stack is used for managing the nodes and the paths
       - We push to the stack the initial state of the problem and an empty list for the paths
       - We trace the stack while it is not empty
       - We pop the top item from the  stack 
       - If the node matches goal state we return the node as a solution
       - If not, we mark the node as visited and it's successors as new paths and pushing to stack 
    """
    
    isVisited = [] 

    stack = util.Stack()
    stack.push((problem.getStartState(), []))

    while(not stack.isEmpty()):

        node = stack.pop()

        if problem.isGoalState(node[0]):

            return node[1]

        if(node[0] not in isVisited):

            isVisited.append(node[0])
            successors = problem.getSuccessors(node[0])
            
            for next_nodes in successors:
                
                newPath = node[1] + [next_nodes[1]]
                stack.push((next_nodes[0], newPath))

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    """
       - An empty list is diclared named isVisited to store the nodes that will be visited 
       - The queue is used for managing the nodes and the paths
       - We push to the queue the initial state of the problem and an empty list for the paths
       - We trace the queue while it is not empty
       - We pop the lowest item from the queue
       - If the node matches goal state we return the node as a solution
       - If not, we mark the node as visited and it's successors as new paths and pushing to queue 
    """

    isVisited = []

    queue = util.Queue()
    queue.push((problem.getStartState(), []))

    while(not queue.isEmpty()):
        
        node = queue.pop()

        if(problem.isGoalState(node[0])):
            
            return node[1]
        
        if(node[0] not in isVisited):
            
            isVisited.append(node[0])
            successors = problem.getSuccessors(node[0])

            for nextNode in successors:
                
                newPath = node[1] + [nextNode[1]]
                queue.push((nextNode[0],newPath))

    util.raiseNotDefined()
    

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
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
    """
       - An empty list is diclared named isVisited to store the nodes that will be visited 
       - the priority queue  is used for managing the nodes and the paths
       - We push to the priority queue the initial state of the problem , an empty list for the paths and the cost
       - We trace the priority queue while it is not empty
       - We pop the item with the highest cost each time 
       - If the node matches goal state we return the node as a solution
       - If not, we mark the node as visited and it's successors as new paths plus we calculate the new cost which is to sum of cost of the current node + the heuristic cost of the next node
       to the goal node.
    """

    isVisited = []

    priorityQueue = util.PriorityQueue()
    priorityQueue.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))

    while(not priorityQueue.isEmpty()):

        node = priorityQueue.pop()

        if(problem.isGoalState(node[0])):
            
            return node[1]
        
        if(node[0] not in isVisited): 
            
            isVisited.append(node[0])
            successors = problem.getSuccessors(node[0])

            for nextNode in successors:
                
                newPath = node[1] + [nextNode[1]]
                cost = problem.getCostOfActions(newPath) + heuristic(nextNode[0],problem)
                priorityQueue.push((nextNode[0],newPath), cost)

    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
