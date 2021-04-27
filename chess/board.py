"""
Will contain an object with an array of pieces
"""
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    """
    Contains an 8x8 array.
    """

    def __init__(self, topc, bottomc):
        self.top_king = King(topc, 4, 0)
        self.bottom_king = King(bottomc, 4, 7)

        self.board_ = [
            [Rook(topc, 0, 0), Knight(topc, 1, 0), Bishop(topc, 2, 0),
                 Queen(topc, 3, 0), self.top_king, Bishop(topc, 5, 0), 
                 Knight(topc, 6, 0), Rook(topc, 7, 0)],
            [Pawn(topc, i, 1, 1) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn(bottomc, i, 6, 0) for i in range(8)],
            [Rook(bottomc, 0, 7), Knight(bottomc, 1, 7), Bishop(bottomc, 2, 7),
                 Queen(bottomc, 3, 7), self.bottom_king, Bishop(bottomc, 5, 7), 
                 Knight(bottomc, 6, 7), Rook(bottomc, 7, 7)]
        ]

    def print_colors(self):
        """
        Prints out all of the colors of the pieces on the board
        """
        for row in self.board_:
            for piece in row:
                if piece != None:
                    print(piece.color , end=' ')
            print('\n')