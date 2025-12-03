# connect_4.py
import random

ROWS = 6
COLS = 7

def find_best_move_connect4(board, player, difficulty):
    # board is a 2D list: board[row][col]
    # For simplicity, easy/medium/hard → random column
    valid_cols = [c for c in range(COLS) if board[0][c]=='' ]
    if not valid_cols: return -1
    return random.choice(valid_cols)
