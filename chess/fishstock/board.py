"""
Will contain an object with an array of pieces
"""
from piece import *

class Board:
    """
    Contains an 8x8 array.
    """

    def __init__(self):
        self.array = [
            [Rook('b', 0, 0), Knight('b', 0, 1), Bishop('b', 0, 2),
                 Queen('b', 0, 3), King('b', 0, 4), Bishop('b', 0, 5), 
                 Knight('b', 0, 6), Rook('b', 0, 7)],
            [Pawn('b', 1, i) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn('w', 6, i) for i in range(8)],
            [Rook('w', 7, 0), Knight('w', 7, 1), Bishop('w', 7, 2),
                 Queen('w', 7, 3), King('w', 7, 4), Bishop('w', 7, 5), 
                 Knight('w', 7, 6), Rook('w', 7, 7)],
        ]