# tic_tac_toe.py
import random

def find_best_move_tic_tac_toe(board, player, difficulty):
    # EASY → random move
    if difficulty == 'easy':
        empty_cells = [i for i, cell in enumerate(board) if cell == '']
        return random.choice(empty_cells) if empty_cells else -1

    # MEDIUM → depth-limited minimax
    max_depth = None
    if difficulty == 'medium':
        max_depth = 2  # shallow search

    best_score = -float('inf')
    best_move = -1

    for i in range(9):
        if board[i] == '':
            board[i] = player
            score = minimax_tic_tac_toe(
                board, False, player, -float('inf'), float('inf'), 0, max_depth
            )
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i

    # HARD → full-depth minimax
    if difficulty == 'hard' and best_move == -1:
        for i in range(9):
            if board[i] == '':
                board[i] = player
                score = minimax_tic_tac_toe(
                    board, False, player, -float('inf'), float('inf'), 0, None
                )
                board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i

    return best_move


def minimax_tic_tac_toe(board, is_maximizing, player, alpha, beta, depth, max_depth):
    if max_depth is not None and depth >= max_depth:
        return 0

    winner = check_winner_tic_tac_toe(board)
    if winner == player:
        return 1
    elif winner != '' and winner != player:
        return -1
    elif '' not in board:
        return 0

    opponent = 'O' if player == 'X' else 'X'

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = player
                score = minimax_tic_tac_toe(board, False, player, alpha, beta, depth+1, max_depth)
                board[i] = ''
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = opponent
                score = minimax_tic_tac_toe(board, True, player, alpha, beta, depth+1, max_depth)
                board[i] = ''
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score


def check_winner_tic_tac_toe(board):
    # Rows
    for i in range(0,9,3):
        if board[i] == board[i+1] == board[i+2] != '':
            return board[i]
    # Columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '':
            return board[i]
    # Diagonals
    if board[0] == board[4] == board[8] != '':
        return board[0]
    if board[2] == board[4] == board[6] != '':
        return board[2]
    return ''
