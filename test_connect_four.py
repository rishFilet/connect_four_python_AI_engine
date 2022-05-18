def test_board_generation():
    from board import Board
    import numpy as np

    board_obj = Board()
    assert board_obj.rows == 6
    assert board_obj.columns == 7
    assert np.count_nonzero(board_obj.board==0) == 42

    board_obj = Board(4, 6)
    assert board_obj.rows == 4
    assert board_obj.columns == 6
    assert np.count_nonzero(board_obj.board == 0) == 24

    board_obj = Board(2,2)
    assert board_obj.rows == 4
    assert board_obj.columns == 4
    assert np.count_nonzero(board_obj.board == 0) == 16

def test_player_generation():
    from player import Player
    player = Player(1)
    assert player.player == 1
    assert player.is_bot == False

    player = Player(2, is_bot=True)
    assert player.player == 2
    assert player.is_bot == True

def test_drop_piece():
    from board import Board
    from mechanics import drop_piece
    import numpy as np

    board_obj = Board()
    for c in range(board_obj.columns):
        new_board_obj = Board()
        dropped_board = drop_piece(new_board_obj.board, c+1, 1)
        assert np.count_nonzero(dropped_board==0) == 41
        assert dropped_board[5][c] == 1
        del new_board_obj

    board = np.full((6, 7), 1)
    for c in range(7):
        dropped_board = drop_piece(board, c+1, 1)
        assert dropped_board == None

def test_check_for_winning_moves_horizontal():
    from board import Board
    from mechanics import check_for_winning_moves
    import numpy as np

    init_board_obj = Board()
    for r in range(init_board_obj.rows-1, -1, -1):
        for c in range(init_board_obj.columns-3):
            board_obj = Board()
            board_obj.board[r][c] = board_obj.board[r][c +
                                                       1] = board_obj.board[r][c+2] = board_obj.board[r][c+3] = 1
            won = check_for_winning_moves(board_obj.board, 1)
            assert won == True
            del board_obj

def test_check_for_winning_moves_vertical():
    from board import Board
    from mechanics import check_for_winning_moves
    import numpy as np

    init_board_obj = Board()
    for c in range(init_board_obj.columns):
        for r in range(init_board_obj.rows-1, 2, -1):
            board_obj = Board()
            board_obj.board[r][c] = board_obj.board[r-1][c] = board_obj.board[r-2][c] = board_obj.board[r-3][c] = 1
            won = check_for_winning_moves(board_obj.board, 1)
            assert won == True
            del board_obj

def test_check_for_winning_moves_right_diagonal():
    from board import Board
    from mechanics import check_for_winning_moves
    import numpy as np

    init_board_obj = Board()
    for c in range(init_board_obj.columns - 4):
        for r in range(init_board_obj.rows-1, -1, -1):
            board_obj = Board()
            board_obj.board[r][c] = board_obj.board[r -
                                                    1][c+1] = board_obj.board[r-2][c+2] = board_obj.board[r-3][c+3] = 1
            won = check_for_winning_moves(board_obj.board, 1)
            assert won == True
            del board_obj

def test_check_for_winning_moves_left_diagonal():
    from board import Board
    from mechanics import check_for_winning_moves
    import numpy as np

    init_board_obj = Board()
    for c in range(init_board_obj.columns - 1, 2, -1):
        for r in range(init_board_obj.rows-1, -1, -1):
            board_obj = Board()
            board_obj.board[r][c] = board_obj.board[r -
                                                    1][c-1] = board_obj.board[r-2][c-2] = board_obj.board[r-3][c-3] = 1
            won = check_for_winning_moves(board_obj.board, 1)
            assert won == True
            del board_obj


def test_check_for_winning_moves_none():
    from board import Board
    from mechanics import check_for_winning_moves
    import numpy as np

    init_board_obj = Board()
    won = check_for_winning_moves(init_board_obj.board, 1)
    assert won == False

def test_check_for_draw():
    from board import Board
    from mechanics import check_for_draw
    import numpy as np

    board_empty = Board()
    assert check_for_draw(board_empty.board) == False

    board_full = np.full((6, 7), 1)
    assert check_for_draw(board_full) == True

def test_get_bot_move_consecutive_horiztonal():
    from board import Board
    from bot import get_bot_move

    board_obj = Board()
    board_obj.board[board_obj.rows-1][0] = board_obj.board[board_obj.rows -
                                                           1][1] = board_obj.board[board_obj.rows-1][2] = 1
    column = get_bot_move(board_obj.board, 1)
    assert column == 4
    del board_obj

    board_obj = Board()
    board_obj.board[board_obj.rows-1][board_obj.columns-1] = board_obj.board[board_obj.rows -
                                                                             1][board_obj.columns-2] = board_obj.board[board_obj.rows-1][board_obj.columns-3] = 1
    print(board_obj.board)
    column = get_bot_move(board_obj.board, 1)
    assert column == 4

def test_get_bot_move_consecutive_vertical():
    from board import Board
    from bot import get_bot_move

    init_board_obj = Board()
    for col in range(init_board_obj.columns-1):
        board_obj = Board()
        board_obj.board[board_obj.rows-1][col] = board_obj.board[board_obj.rows -
                                                            2][col] = board_obj.board[board_obj.rows-3][col] = 1
        column = get_bot_move(board_obj.board, 1)
        assert column == col+1
        del board_obj

# Added teardown for future work. Always good to have it.
def tear_down():
    pass