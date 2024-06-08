from board import Board
from search import SearchProblem, ucs
import util
import math


class BlokusFillProblem(SearchProblem):
    """
    A one-player Blokus game as a search problem.
    This problem is implemented for you. You should NOT change it!
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """
        state: Search state
        Returns True if and only if the state is a valid goal state
        """
        return not any(state.pieces[0])

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, 1) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class BlokusCornersProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.expanded = 0

        "*** YOUR CODE HERE ***"
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.corners = [(0, 0), (0, board_h - 1), (board_w - 1, 0), (board_w - 1, board_h - 1)]

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        "*** YOUR CODE HERE ***"
        for corner in self.corners:
            x, y = corner
            if self.board.get_position(x, y) == -1:
                return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        "*** YOUR CODE HERE ***"
        total_cost = 0
        for action in actions:
            # not checking if the move is legal
            total_cost += action.piece.get_num_tiles()
        return total_cost


def blokus_corners_heuristic(state, problem):
    """
    Your heuristic for the BlokusCornersProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.
    """
    "*** YOUR CODE HERE ***"
    # state: board
    # problem: {get_start_state, is_goal_state, get_successors,
    # get_cost_of_actions}

    # corners = [
    #     (0, 0),
    #     (0, state.board_h - 1),
    #     (state.board_w - 1, 0),
    #     (state.board_w - 1, state.board_h - 1)
    # ]
    # uncovered_corners = get_uncovered_corners(problem, corners)
    #
    # total_min_distance = 0
    #
    # for corner in uncovered_corners:
    #     min_distance = math.inf
    #     for piece in state.pieces:
    #         for piece_part in piece.parts:
    #             piece_x, piece_y = piece_part
    #             distance = manhattan_distance((piece_x, piece_y), corner)
    #             if distance < min_distance:
    #                 min_distance = distance
    #     total_min_distance += min_distance
    #
    # return total_min_distance
    # Define the corners of the board
    # Define the corners of the board
    corners = [(0, 0), (0, state.board_h - 1), (state.board_w - 1, 0),
               (state.board_w - 1, state.board_h - 1)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

#     def l_1_distance(corner):
#
#         if corner == (0, state.board_h - 1):
#             starting_point_x = 1
#             starting_point_y = state.board_h - 1
#              while
#
#
#
#         visited = set()
#         queue = deque([(corner, 0)])
#         empty_levels = 0
#         current_level = 0
#
#         if state.get_position(*corner) != -1:
#             return 0
#
#         while queue:
#             (x, y), level = queue.popleft()
#
#             if level > current_level:
#                 if empty_levels == current_level:
#                     empty_levels += 1
#                 current_level = level
#
#             if (x, y) in visited:
#                 continue
#             visited.add((x, y))
#             global_visited.add((x, y))
#
#             if state.get_position(x, y) != -1:
#                 break
#
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < state.board_w and 0 <= ny < state.board_h and (nx, ny) not in visited:
#                     queue.append(((nx, ny), level + 1))
#
#         return empty_levels
#
#     global global_visited
#     global_visited = set()
#     total_empty_levels = sum(l_1_distance(corner) for corner in corners)
#     return total_empty_levels
#
#
# def iterate_diagonal_layers(board_h, board_w, corner):
#     x_corner, y_corner = corner
#     layers = []
#
#     if corner == (0, 0):  # Top-left corner
#         directions = [(0, 1), (1, 0)]
#     elif corner == (0, board_w - 1):  # Top-right corner
#         directions = [(0, -1), (1, 0)]
#     elif corner == (board_h - 1, 0):  # Bottom-left corner
#         directions = [(0, 1), (-1, 0)]
#     elif corner == (board_h - 1, board_w - 1):  # Bottom-right corner
#         directions = [(0, -1), (-1, 0)]
#     else:
#         raise ValueError("Invalid corner")
#
#     # Initialize the queue with the first layer of adjacent tiles
#     queue = [(x_corner + dx, y_corner + dy, 1) for dx, dy in directions if
#              0 <= x_corner + dx < board_w and 0 <= y_corner + dy < board_h]
#
#     visited = set(queue)
#
#     while queue:
#         x, y, layer = queue.pop(0)
#         layers.append((x, y, layer))
#
#         # Explore diagonals for the next layer
#         for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < board_w and 0 <= ny < board_h and (
#             nx, ny) not in visited:
#                 visited.add((nx, ny))
#                 queue.append((nx, ny, layer + 1))
#
#     return layers


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


class BlokusCoverProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=[(0, 0)]):
        self.targets = targets.copy()
        self.expanded = 0
        "*** YOUR CODE HERE ***"

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        "*** YOUR CODE HERE ***"
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
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def blokus_cover_heuristic(state, problem):
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def iterate_diagonals_from_corner(board_h, board_w):
    diagonals = []

    # The first diagonal contains the tiles adjacent to the top-left corner
    first_diagonal = [(0, 1), (1, 0)]
    diagonals.append(first_diagonal)

    # Initialize the next diagonal layer
    layer = 1

    while True:
        next_diagonal = []

        # Add the tiles that form the next diagonal
        for i in range(layer + 1):
            x = i
            y = layer - i

            # Check if the coordinates are within the bounds of the board
            if x < board_w and y < board_h:
                next_diagonal.append((x, y))

        if not next_diagonal:
            break

        diagonals.append(next_diagonal)
        layer += 1

    return diagonals

# Example usage
if __name__ == '__main__':

    board_h = 10
    board_w = 5

    diagonals = iterate_diagonals_from_corner(board_h, board_w)
    for diagonal in diagonals:
        print("Diagonal:", diagonal)