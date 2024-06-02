"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visited = set()  # To keep track of visited nodes
    stack = util.Stack()  # last in first out
    stack.push((problem.get_start_state(), []))  # Initialize the stack with the starting node and an empty path

    while not stack.isEmpty():
        node, path = stack.pop()
        if problem.is_goal_state(node):
            return path

        if node not in visited:
            visited.add(node)
            for successor, action, step_cost in problem.get_successors(node):
                if successor not in visited:
                    stack.push((successor, path + [action]))

    return []


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    visited = set()
    queue = util.Queue()  # first in first out
    queue.push((problem.get_start_state(), []))
    while not queue.isEmpty():
        node, path = queue.pop()

        if problem.is_goal_state(node):
            return path

        if node not in visited:
            visited.add(node)
            for successor, action, step_cost in problem.get_successors(node):
                if successor not in visited:
                    queue.push((successor, path + [action]))

    return []


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    priority_queue = util.PriorityQueue()
    start_state = problem.get_start_state()
    state_cost_dict = {}  # To keep track of the least cost to reach each state from the start state
    priority_queue.push((start_state, []), 0)  # Initialize the priority queue with the starting node
    state_cost_dict[start_state] = 0  # Initialize the cost to reach the start state

    while not priority_queue.isEmpty():
        node, path = priority_queue.pop()  # Get the node with the least cost

        if problem.is_goal_state(node):
            return path

        if node not in visited:
            visited.add(node)
            for successor, action, step_cost in problem.get_successors(node):
                updated_cost = state_cost_dict[node] + step_cost
                if successor not in state_cost_dict or updated_cost < state_cost_dict[successor]:
                    state_cost_dict[successor] = updated_cost
                    updated_path = path + [action]
                    priority_queue.push((successor, updated_path), updated_cost)
    return []


def uniform_cost_search(problem):
    visited = set()
    priority_queue = util.PriorityQueue()
    start_state = problem.get_start_state()
    priority_queue.push((start_state, []), 0)  # Initialize the priority queue with the starting node

    while not priority_queue.isEmpty():
        node, path = priority_queue.pop()  # Get the node with the least cost

        if problem.is_goal_state(node):
            return path

        if node not in visited:
            visited.add(node)
            for successor, action, step_cost in problem.get_successors(node):
                new_path = path + [action]
                new_cost = problem.get_cost_of_actions(new_path)
                priority_queue.push((successor, new_path), new_cost)

    return []


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    visited = set()
    priority_queue = util.PriorityQueueWithFunction(heuristic)
    start_state = problem.get_start_state()
    state_cost_dict = {}  # To keep track of the least cost to reach each state from the start state
    priority_queue.push((start_state, []))  # Initialize the priority queue with the starting node
    state_cost_dict[start_state] = 0  # Initialize the cost to reach the start state

    while not priority_queue.isEmpty():
        node, path = priority_queue.pop()  # Get the node with the least cost

        if problem.is_goal_state(node):
            return path

        if node not in visited:
            visited.add(node)
            for successor, action, step_cost in problem.get_successors(node):
                updated_cost = state_cost_dict[node] + step_cost
                if successor not in state_cost_dict or updated_cost < state_cost_dict[successor]:
                    state_cost_dict[successor] = updated_cost
                    updated_path = path + [action]
                    priority_queue.push((successor, updated_path))

    return []


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
