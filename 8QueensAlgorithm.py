# Algorithm to place 8 Queens without crossing in any direction

import numpy as np
import queen_functions

from queen_functions import create_board_string
from queen_functions import is_board_safe
from queen_functions import place_queen

N = 8
# initialise board with zeros
board = np.zeros((N,N), np.int8)
# place the 8 queens (ones) to the board
placed = place_queen(board, 0)
print(board)

