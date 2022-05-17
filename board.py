import numpy as np

ROWS = 6
COLUMNS = 7

class Board:
    def __init__(self, rows: int = ROWS, columns: int = COLUMNS) -> None:
        self.rows = rows # Used to get shape if needed
        self.columns = columns  # Used to get shape if needed
        self.board = np.zeros((rows, columns))

