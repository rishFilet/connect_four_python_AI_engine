import numpy as np

ROWS = 6
COLUMNS = 7
MIN_ROW_SIZE = 4
MIN_COL_SIZE = 4
class Board:
    def __init__(self, rows: int = ROWS, columns: int = COLUMNS) -> None:
        self.rows, self.columns = self.validate_board_size(
            rows, columns)  # Used to get shape if needed
        self.board = np.zeros((self.rows, self.columns))

    # Used to keep the board size a minimum. Can be set in constants.
    def validate_board_size(self, rows: int, columns: int) -> list:
        rows = MIN_ROW_SIZE if rows < MIN_ROW_SIZE else rows
        columns = MIN_COL_SIZE if columns < MIN_COL_SIZE else columns
        return rows, columns

