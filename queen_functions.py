import numpy as np
N = 8
board_state_memory = {}

def create_board_string(board):
    board_string = ''
    for i in range(N):
        for j in range(N):
            board_string += str(board[i][j])
    return board_string

def is_board_safe(board):

    board_key = create_board_string(board)

    if board_key in board_state_memory:
        print('Using cached information')
        return board_state_memory[board_key]

    row_sum = np.sum(board,axis = 1) # sum of each row
    if len(row_sum[np.where(row_sum > 1)]) > 0:
        board_state_memory[board_key] = False
        return False
    
    col_sum = np.sum(board, axis = 0)  # sum of each column
    if len(col_sum[np.where(col_sum > 1)]) > 0:
        board_state_memory[board_key] = False
        return False

    # sum of each diagonals up direction
    diags = [board[: :-1,:].diagonal(i) for i in range(-board.shape[0] + 1, board.shape[1])]
    # sum of each diagonals down direction
    diags.extend(board.diagonal(i) for i in range(board.shape[1] - 1, -board.shape[0], -1))

    for diag in diags:
        if np.sum(diag) > 1:
            board_state_memory[board_key] = False
            return False

    board_state_memory[board_key] = True
    return True

def place_queen(board,column):
    if column >= N:
        return True

    for row in range(N):
        board[row][column] = 1

        safe = False
        if is_board_safe(board):
            safe = place_queen(board,column + 1)

        if not safe:
            board[row][column] = 0
        else:
            break
    return safe