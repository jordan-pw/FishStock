"""
Will contain an object with an array of pieces
"""


class Board:
    """
    Contains an 8x8 array.
    """

    def __init__(self):
        self.board_array = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]