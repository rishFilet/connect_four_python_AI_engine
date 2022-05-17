import numpy as np
from typing import List

def drop_piece(board: List[list], column: int, player_number: int) -> List[list]:
    for r in range(len(board)-1, -1, -1):
        if board[r][column-1] == 0:
            board[r][column-1] = player_number
            return board
    else:
        print(f"Cannot play on column {column}\n")
        return None


def check_for_winning_moves(board: List[list], player_number: int) -> bool:
    # check for horizontal wins
    for r in range(len(board)-1, -1, -1):
        for c in range(len(board)-2):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == player_number:
                board[r][c] = board[r][c+1] = board[r][c+2] = board[r][c+3] = 88
                print(board)
                print(f"Player {player_number} WINS!")
                return True

    # check for vertical wins
    for c in range(len(board[0])):
        for r in range(len(board)-1, 2, -1):
            if board[r][c] == board[r-1][c] == board[r-2][c] == board[r-3][c] == player_number:
                board[r][c] = board[r-1][c] = board[r-2][c] = board[r-3][c] = 88
                print(board)
                print(f"Player {player_number} WINS!")
                return True

    # Check for right upwards diagonals:
    for c in range(0, len(board[0])-4):
        for r in range(len(board)-1, -1, -1):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == player_number:
                board[r][c] = board[r-1][c+1] = board[r -
                                                      2][c+2] = board[r-3][c+3] = 88
                print(board)
                print(f"Player {player_number} WINS!")
                return True

    # Check for left upwards diagonals:
    for c in range(len(board[0])-1, 2, -1):
        for r in range(len(board)-1, -1, -1):
            if board[r][c] == board[r-1][c-1] == board[r-2][c-2] == board[r-3][c-3] == player_number:
                board[r][c] = board[r-1][c-1] = board[r -
                                                      2][c-2] = board[r-3][c-3] = 88
                print(board)
                print(f"Player {player_number} WINS!")
                return True
    else:
        return False


def check_for_draw(board: List[list]) -> bool:
    # I could make this whole thing one line but then i want to include a print statment for the outcome
    if np.count_nonzero(board == 0) == 0:
        print("DRAW | GAME OVER!")
        return True
    else:
        return False
