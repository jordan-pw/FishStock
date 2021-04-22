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
            [Rook('b', 0, 0), Knight('b', 1, 0), Bishop('b', 2, 0),
                 Queen('b', 3, 0), King('b', 4, 0), Bishop('b', 5, 0), 
                 Knight('b', 6, 0), Rook('b', 7, 0)],
            [Pawn('b', i, 1) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn('w', i, 6) for i in range(8)],
            [Rook('w', 0, 7), Knight('w', 1, 7), Bishop('w', 2, 7),
                 Queen('w', 3, 7), King('w', 4, 7), Bishop('w', 5, 7), 
                 Knight('w', 6, 7), Rook('w', 7, 7)],
        ]

    def print_colors(self):
        """
        Prints out all of the colors of the pieces on the board
        """
        for row in self.array:
            for piece in row:
                if piece != None:
                    print(piece.color , end=' ')
            print('\n')