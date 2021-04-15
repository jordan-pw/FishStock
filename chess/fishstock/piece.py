"""
Will contain an object for each piece
"""
import pygame

def chk_move(color, x, y, board):
    """
    Checks if a move is valid, if the coordinate on the board is empty,
    the move is valid, if the coordinate contains an enemy, the move is
    valid, if the coordinate is out of bounds or contains a friend, the
    move is invalid
    """

    piece = board.array[x][y]
    if x < 0 or x > 7 or y < 0 or y > 7:
        # Out of bounds
        return False

    if piece == None:
        # Empty space
        return True
    else:
        if piece.color != color:
            # Enemy piece
            return True
        else:
            # Friend
            return False

    
def get_straight_moves(self,board):
    """
    Generates all possible legal horizontal and vertical moves
    Args:
        Instance of chess board
    Returns:
        legal_moves - set containing tuples (x,y) of coordinates of each valid move
    """
    # Vertical moves
    legal_moves = set()

    for i in(-1, 1):
        possible_y = self.y 
        while(True):
            possible_y += i
            if chk_move(self.color, self.x, possible_y, board):
                legal_moves.add((self.x, possible_y))
                if board.array[self.x, possible_y].color != color: # If there is an enemy piece
                    break
                else: # If the move is out of bounds or friendly piece
                    break

    # Horizontal moves
    for i in(-1, 1):
        possible_x = self.x 
        while(True):
            possible_x += i
            if chk_move(self.color, possible_x, self.y, board):
                legal_moves.add((possible_x, self.y))
                if board.array[possible_x, self.y].color != color: # If there is an enemy piece
                    break
                else: # If the move is out of bounds or friendly piece
                    break

    return legal_moves

def get_diag_moves(self,board):
    """
    Generates all possible legal diagonal moves
    Args:
        Instance of chess board
    Returns:
        legal_moves - set containing tuples (x,y) of coordinates of each valid move
    """
    legal_moves = set()

    for movement in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        possible_x = self.x 
        possible_y = self.y
        while(True):
            possible_x += movement[0]
            possible_y += movement[1]
            if chk_move(self.color, possible_x, possible_y, board):
                legal_moves.add((possible_x, possible_y))
                if board.array[possible_x, possible_y].color != color: # If there is an enemy piece
                    break
                else: # If the move is out of bounds or friendly piece
                    break
    return legal_moves

class Piece(pygame.sprite.Sprite):
    """
    Basic piece object, stores color and position
    """
    def __init__(self,color,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wpawn.png').convert()
        else: self.sprite = pygame.image.load('resources\\bpawn.png').convert()


    def generate_moves(self, board):
        """
        Generates the possible legal moves, not accounting for check
        Args:
            Instance of the legal moves
        Returns:
            legal_moves - set containing tuples (x,y) of coordinates of 
            each valid move
        """
        legal_moves = set()

        direction = {'w': -1, 'b': 1}
        col = self.color

        possible_y = self.y
        possible_y += direction[color]
        """
        Cannot use the chk_move method, as the pawn cannot capture piece in occupied
        squares directly ahead of it
        """
        piece = board.array[self.x][possible_y]
        if piece == None:
            # Empty square
            legal_moves.add((self.x, possible_y))
        if (y < 0 or y > 7) or (piece is not None):
            # Out of bounds or occupied, so check if the diagonally adjacent squares contain an enemy piece
            if (board.array[self.x+1].color != self.color):
                legal_moves.add((self.x+1, possible_y))
            else:
                if (board.array[self.x-1].color != self.color):
                    legal_moves.add((self.x-1, possible_y))
        return legal_moves
                
class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wrook.png').convert()
        else: self.sprite = pygame.image.load('resources\\brook.png').convert()

    def generate_moves(self, board):
        return self.get_straight_moves(board)

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wbishop.png').convert()
        else: self.sprite = pygame.image.load('resources\\bbishop.png').convert()

    def generate_moves(self, board):
        return self.get_diag_moves(board)

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wknight.png').convert()
        else: self.sprite = pygame.image.load('resources\\bknight.png').convert()

    def generate_moves(self, board):
        legal_moves = set()
        # Possible offset of the moves the knight can make from his starting position - starting(x,y) + (x, y)
        possible_moves = [(-1, 2), (1, 2), (-1, -2), (1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

        for move in possible_moves:
            possible_x = self.x + possible_moves[0]
            possible_y = self.y + possible_moves[1]
            if chk_move(self.color, possible_x, possible_y, board):
                legal_moves.add((possible_x, possible_y))
        return legal_moves

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wking.png').convert()
        else: self.sprite = pygame.image.load('resources\\bking.png').convert()

    def generate_moves(self, board):
        legal_moves = set()
        # Possible offset of the moves the king can make from his starting position
        possible_moves = [(-1, -1), (-1, 1), (1, -1), (1, -1), (1, 0), (-1, 0), (0, -1), (0, 1)]

        for move in possible_moves:
            possible_x = self.x + possible_moves[0]
            possible_y = self.y + possible_moves[1]
            if chk_move(self.color, possible_x, possible_y, board):
                legal_moves.add((possible_x, possible_y))
        return legal_moves

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wqueen.png')
        else: self.sprite = pygame.image.load('resources\\bqueen.png')

    def generate_moves(self, board):
        return self.get_diag_moves.union(self.get_straight_moves)


