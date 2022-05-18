from typing import List
import random

# This function is a basic check to find a blocking move of the other player or the next win for the bot based on horizontal and vertical consecutives
def get_bot_move(board: List[list], player_number: int) -> int:
    # check for horizontal 3s
    for r in range(len(board)-1, -1, -1):
        for c in range(len(board[0])-2):
            # Last condition is so that the first condition does not check if there is a line of zeroes
            if (board[r][c] == board[r][c+1] == board[r][c+2] != player_number and board[r][c] != 0) or board[r][c] == board[r][c+1] == board[r][c+2] == player_number:
                if c == len(board[0]) - 3:
                    return c  # It is not c - 1 because the columns need to be returned as 1-indexed in this case due to the drop_piece method handling the -1 for the array
                else:
                    move_found = True
                    return c + 4

    # check for vertical 3s
    for c in range(len(board[0])):
        for r in range(len(board)-1, 1, -1):
            # Last condition is so that the first condition does not check if there is a line of zeroes
            if (board[r][c] == board[r-1][c] == board[r-2][c] != player_number and board[r][c] != 0 and board[r-3][c] == 0) or (board[r][c] == board[r-1][c] == board[r-2][c] == player_number and board[r-3][c] == 0):
                return c + 1
    else:
        return random.randint(1, 7)
