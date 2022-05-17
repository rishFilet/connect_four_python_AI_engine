import numpy as np
from board import Board
from player import Player
from bot import get_bot_move
from mechanics import drop_piece, check_for_winning_moves, check_for_draw


if __name__ == '__main__':
    board_obj = Board()
    cols = board_obj.columns
    curr_board = board_obj.board
    player_list = [Player(1), Player(2, is_bot=True)]
    print("Ready to play! Player 1 goes first\n")

    game_over = False
    curr_player = player_list[0]

    while not game_over:
        print(curr_board)
        print("  1  2  3  4  5  6  7") # Column labels
        updated_board = None
        while updated_board is None:
            while True:
                if curr_player.is_bot:
                    drop_column = get_bot_move(curr_board, curr_player.player)
                    print(f"Player 2 plays on column {drop_column}")
                    break
                else:
                    drop_column = int(input(f"Choose a column number between 1-{cols} to drop your piece\n"))
                    if drop_column > 0 and drop_column < cols + 1:
                        break
                    else:
                        print("Invalid column choice\n")
            updated_board = drop_piece(curr_board, drop_column, curr_player.player)
        curr_board = updated_board
        if check_for_winning_moves(curr_board, curr_player.player) or check_for_draw(curr_board):
            game_over = True
        if not game_over:
            if curr_player.player != len(player_list):
                curr_player = player_list[curr_player.player]
            else:
                curr_player = player_list[0]
            print(f"\n--------------------\nPlayer {curr_player.player} goes next\n")



