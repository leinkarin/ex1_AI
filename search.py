"""
In search.py, you will implement generic search algorithms
"""

import util
import math

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


# def uniform_cost_search(problem):
#     """
#     Search the node of least total cost first.
#     """
#     "*** YOUR CODE HERE ***"
#     visited = set()
#     priority_queue = util.PriorityQueue()
#     start_state = problem.get_start_state()
#     state_cost_dict = {}  # To keep track of the least cost to reach each state from the start state
#     priority_queue.push((start_state, []), 0)  # Initialize the priority queue with the starting node
#     state_cost_dict[start_state] = 0  # Initialize the cost to reach the start state
#
#     while not priority_queue.isEmpty():
#         node, path = priority_queue.pop()  # Get the node with the least cost
#
#         if problem.is_goal_state(node):
#             return path
#
#         if node not in visited:
#             visited.add(node)
#             for successor, action, step_cost in problem.get_successors(node):
#                 updated_cost = state_cost_dict[node] + step_cost
#                 if successor not in state_cost_dict or updated_cost < state_cost_dict[successor]:
#                     state_cost_dict[successor] = updated_cost
#                     updated_path = path + [action]
#                     priority_queue.push((successor, updated_path), updated_cost)
#     return []
#
#
# def uniform_cost_search(problem):
#     visited = set()
#     priority_queue = util.PriorityQueue()
#     start_state = problem.get_start_state()
#     priority_queue.push((start_state, []), 0)  # Initialize the priority queue with the starting node
#
#     while not priority_queue.isEmpty():
#         node, path = priority_queue.pop()  # Get the node with the least cost
#
#         if problem.is_goal_state(node):
#             return path
#
#         if node not in visited:
#             visited.add(node)
#             for successor, action, step_cost in problem.get_successors(node):
#                 new_path = path + [action]
#                 new_cost = problem.get_cost_of_actions(new_path)
#                 priority_queue.push((successor, new_path), new_cost)
#
#     return []

# actual

def uniform_cost_search(problem):

    priorityQueue = util.PriorityQueue()

    priorityQueue.push(problem.get_start_state(), 0)
    visited = dict()
    parents = dict()

    # Initialize the cost dictionary to keep track of the minimum cost to reach each node
    cost = {problem.get_start_state(): 0}
    parents[problem.get_start_state()] = None

    while not priorityQueue.isEmpty():
        # Pop the node with the lowest cost
        currentNode = priorityQueue.pop()
        currentCost = cost[currentNode]

        # If the goal node is reached, return the cost to reach the goal
        if problem.is_goal_state(currentNode):
            return reconstruct_path(parents, problem.get_start_state(), currentNode), currentCost


        # If the current node has not been visited
        if currentNode not in visited:
            visited[currentNode] = currentCost

            # Iterate over the neighbors of the current node
            successors = problem.get_successors(currentNode)
            for successor, action, actionCost in successors:
                newCost = currentCost + actionCost

            # If the neighbor has not been visited or a cheaper cost path is found
            #     if successor not in cost or newCost < cost[successor]:
            #         cost[successor] = newCost
            #         priorityQueue.push(successor, newCost)
                if successor not in visited or newCost < cost[successor]:
                    cost[successor] = newCost
                    priorityQueue.push(successor, newCost)
                    parents[successor] = (currentNode, action)

    # If the goal node is not reachable, return infinity or an indicator of failure
    return []

# Karin's friend
# def uniform_cost_search(problem):
#     """
#     Search the node of least total cost first.
#     """
#     frontier = util.PriorityQueue()
#     frontier.push(problem.get_start_state(), priority=0)
#
#     visited = dict()
#     parents = dict()
#
#     parents[problem.get_start_state()] = None
#     visited[problem.get_start_state()] = 0  # costs of the visited nodes
#
#     while not frontier.isEmpty():
#         current = frontier.pop()
#
#         if problem.is_goal_state(current):
#             return reconstruct_path(parents, problem.get_start_state(),
#                                     current)
#
#         for successor, action, step_cost in problem.get_successors(current):
#             new_priority = step_cost + visited[current]
#
#             if successor not in visited or new_priority < visited[successor]:
#                 visited[successor] = new_priority
#                 parents[successor] = (current, action)
#                 frontier.push(successor, new_priority)
#
#     return []


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


# def a_star_search(problem, heuristic=null_heuristic):
#     """
#     Search the node that has the lowest combined cost and heuristic first.
#     """
#     "*** YOUR CODE HERE ***"
#     visited = set()
#     priority_queue = util.PriorityQueueWithFunction(heuristic)
#     start_state = problem.get_start_state()
#     state_cost_dict = {}  # To keep track of the least cost to reach each state from the start state
#     priority_queue.push((start_state, []))  # Initialize the priority queue with the starting node
#     state_cost_dict[start_state] = 0  # Initialize the cost to reach the start state
#
#     while not priority_queue.isEmpty():
#         node, path = priority_queue.pop()  # Get the node with the least cost
#
#         if problem.is_goal_state(node):
#             return path
#
#         if node not in visited:
#             visited.add(node)
#             for successor, action, step_cost in problem.get_successors(node):
#                 updated_cost = state_cost_dict[node] + step_cost
#                 if successor not in state_cost_dict or updated_cost < state_cost_dict[successor]:
#                     state_cost_dict[successor] = updated_cost
#                     updated_path = path + [action]
#                     priority_queue.push((successor, updated_path))
#
#     return []

def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue()
    start_state = problem.get_start_state()
    frontier.push(start_state, 0)

    visited = dict()
    parents = dict()
    costs = dict()

    parents[start_state] = None
    costs[start_state] = 0

    while not frontier.isEmpty():
        current_state = frontier.pop()

        if problem.is_goal_state(current_state):
            return reconstruct_path(parents, start_state, current_state)

        if current_state not in visited:
            visited[current_state] = costs[current_state]

            for successor, action, step_cost in problem.get_successors(
                    current_state):
                new_cost = costs[current_state] + step_cost
                heuristic_cost = new_cost + heuristic(successor, problem)

                if successor not in visited or new_cost < costs[successor]:
                    costs[successor] = new_cost
                    parents[successor] = (current_state, action)
                    frontier.push(successor, heuristic_cost)

    return []


def reconstruct_path(parents, start, goal):
    path = []
    current = goal
    while current != start:
        parent, action = parents[current]
        path.append((parent, action))
        current = parent
    path.reverse()  # Reverse the path to start from the beginning
    return path



# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
