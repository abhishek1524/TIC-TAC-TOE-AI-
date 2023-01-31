"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # we will count number of X and O, one has lesser value will have next move
    count_for_x = 0
    count_for_O = 0

    for a in range(len(board)):
        for b in range(len(board[0])):

            if board[a][b] == X:
                count_for_x +=1
            
            if board[a][b] == O:
                count_for_O +=1

    return X if count_for_x == count_for_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allmoves = set()

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == EMPTY:
                allmoves.add((i,j))
 
    return allmoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
 # we will raise an exception if action is invalid else we will add action(or move) to the board
    (i,j) = action
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
        raise IndexError

    # now make deepcopy 
    copy_board = [rows[:] for rows in board]
    copy_board[i][j] = player(board)
    return copy_board

# we will create some funtions which will determine if same player's value is there in continuos rows,cols or diagonals

# for rows
def check_for_row(board,player):

    for row in range(len(board)):
        val= 0
        for col in range(len(board[0])):

            if board[row][col] == player:
                val +=1

        if val == len(board[0]):
            return True
     # we return false if there is no player having same value in continuous rows               
    return False

 # for columns
def check_for_col(board,player):

    for cols in range(len(board[0])):
        var = 0 
        for rows in range(len(board)):

            if board[rows][cols] == player:
                var += 1

        if var == len(board):
            return True
     # we return false if there is no player having same value in continuous columns
    return False

 # for first diagonal 
def check_for_digonal_one(board,player):
    var = 0
    
    for rows in range(len(board)):
        for cols in range(len(board[0])):

            if rows == cols and board[rows][cols] == player:
                var +=1

    return var == len(board[0])

 # for second diagonal
def check_for_diagonal_two(board,player):
    var = 0 
    for rows in range(len(board)):
        for cols in range(len(board[0])):

            if (len(board) - rows - 1) == cols and board[rows][cols] == player:
                var +=1

    return var == len(board[0])

# cheking if no one wins game
def check_tie(board):

    number_of_empty = (len(board) * len(board[0]))
    for rows in range(len(board)):
        for cols in range(len(board[0])):

            if board[rows][cols] is not EMPTY:
                number_of_empty -=1

    if number_of_empty == 0:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if any of functions we made above is true means it means we have a winner
    if check_for_row(board,X) or check_for_col(board,X) or check_for_digonal_one(board,X) or check_for_diagonal_two(board,X):
        return X

    elif check_for_row(board,O) or check_for_col(board,O) or check_for_digonal_one(board,O) or check_for_diagonal_two(board,O):
        return O

    else:
        return None

    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or check_tie(board):
        return True
    else:
        return False

    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if O wins the game
    if winner(board) == O:
        return -1
    # if X wins the game
    elif winner(board) == X:
        return 1
    # if no one wins the game
    else:
        return 0
   
# we will make 2 funtions maxval and minval then use these funtions in implementing minimax function
# maxval function
def max_val(board):
    ans = -math.inf
    if terminal(board):
        return utility(board), None

    any_move = None
    all_actions = actions(board)

    for action in all_actions:
        res, mov = min_val(result(board, action))

        if res > ans:
            ans = res
            any_move = action

    return ans, any_move

# minval function
def min_val(board):
    ans = math.inf
    if terminal(board):
        return utility(board), None

    any_move = None
    all_actions = actions(board)

    for action in all_actions:
        res, mov = max_val(result(board, action))

        if res < ans:
            ans = res
            any_move = action

    return ans, any_move

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    else:
        if player(board) == O:

            ans,action = min_val(board)
            return action

        else:
            ans,action = max_val(board)
            return action
