"""
Will contain an object for each piece
"""
import pygame

def chk_move(self, color, x, y, board):
    """
    Checks if a move is valid, if the coordinate on the board is empty,
    the move is valid, if the coordinate contains an enemy, the move is
    valid, if the coordinate is out of bounds or contains a friend, the
    move is invalid
    """
    if x < 0 or x > 7 or y < 0 or y > 7:
        # Out of bounds
        return False
    
    piece = board.board_[y][x]
    if piece == None:
        # Empty Space
        return True
    else:
        if piece.color != color:
            piece.attacked_by.add((self.x, self.y))
            # Enemy piece
            return True
        if piece.color == color:
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

            if chk_move(self, self.color, self.x, possible_y, board):
                if self.color == 'w': # Set all attacked positions
                    board.white_attack_board[possible_y][self.x] = 1
                else: 
                    board.black_attack_board[possible_y][self.x] = 1

                if (board.board_[possible_y][self.x] != None):
                    legal_moves.add((self.x, possible_y))
                    self.attacking.add((self.x, possible_y))
                    break
                else:
                    legal_moves.add((self.x, possible_y))
            else:
                break

    # Horizontal moves
    for i in(-1, 1):
        possible_x = self.x 
        while(True):
            possible_x += i

            if chk_move(self, self.color, possible_x, self.y, board):
                if self.color == 'w': # Set all attacked positions
                    board.white_attack_board[self.y][possible_x] = 1
                else: 
                    board.black_attack_board[self.y][possible_x] = 1

                if (board.board_[self.y][possible_x] != None): # If there is an enemy piece
                    legal_moves.add((possible_x, self.y))
                    self.attacking.add((possible_x, self.y))
                    break
                else: # If board is empty here
                    legal_moves.add((possible_x, self.y))
            else:
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
            if chk_move(self, self.color, possible_x, possible_y, board):
                if self.color == 'w': # Set all attacked positions
                    board.white_attack_board[possible_y][possible_x] = 1
                else: 
                    board.black_attack_board[possible_y][possible_x] = 1

                if (board.board_[possible_y][possible_x] != None): # If there is an enemy piece
                    legal_moves.add((possible_x, possible_y))
                    self.attacking.add((possible_x, possible_y))
                    break
                else: # If the board is empty here
                    legal_moves.add((possible_x, possible_y))
            else:
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
        self.attacking = set()
        self.attacked_by = set()

    def generate_legal_moves(self, moveset):
        legal_moves = set()
        
            

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

        possible_y = self.y + direction[col]
        """
        Cannot use the chk_move method, as the pawn cannot capture piece in occupied
        squares directly ahead of it
        """
        piece = board.board_[possible_y][self.x]
        if (possible_y >= 0 or possible_y <= 7) and piece == None:
            if self.color == 'w': # Set all attacked positions
                board.white_attack_board[possible_y][self.x] = 1
            else: 
                board.black_attack_board[possible_y][self.x] = 1

            legal_moves.add((self.x, possible_y))

        # Out of bounds or occupied, so check if the diagonally adjacent squares contain an enemy piece
        if (self.x+1 <= 7): # Check if the piece you're looking at is off the board
            enemy1 = board.board_[possible_y][self.x+1]

            if self.color == 'w': # Set all attacked positions
                board.white_attack_board[possible_y][self.x+1] = 1
            else: 
                board.black_attack_board[possible_y][self.x+1] = 1
        else: enemy1 = None
        if (self.x-1 >= 0): # Check if the piece you're looking at is off the board
            enemy2 = board.board_[possible_y][self.x-1]

            if self.color == 'w': # Set all attacked positions
                board.white_attack_board[possible_y][self.x-1] = 1
            else: 
                board.black_attack_board[possible_y][self.x-1] = 1
        else: enemy2 = None

        # Check if the two spaces contain an enemy
        if ((enemy1 is not None) and (enemy1.color != col)):
            self.attacking.add((self.x+1, possible_y))
            legal_moves.add((self.x+1, possible_y))
        if ((enemy2 is not None) and (enemy2.color != col)):
            self.attacking.add((self.x-1, possible_y))
            legal_moves.add((self.x-1, possible_y))
        return legal_moves

    
class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wrook.png').convert()
        else: self.sprite = pygame.image.load('resources\\brook.png').convert()

    def generate_moves(self, board):
        return get_straight_moves(self, board)

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wbishop.png').convert()
        else: self.sprite = pygame.image.load('resources\\bbishop.png').convert()

    def generate_moves(self, board):
        return get_diag_moves(self,board)

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
            possible_x = self.x + move[0]
            possible_y = self.y + move[1]
            if chk_move(self, self.color, possible_x, possible_y, board):
                legal_moves.add((possible_x, possible_y))
                if (board.board_[possible_y][possible_x] is not None) and (board.board_[possible_y][possible_x].color != self.color):
                    self.attacking.add((possible_x, possible_y))
        return legal_moves

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wking.png').convert()
        else: self.sprite = pygame.image.load('resources\\bking.png').convert()
        self.is_in_check = False

    def generate_moves(self, board):
        legal_moves = set()
        # Possible offset of the moves the king can make from his starting position
        possible_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

        for move in possible_moves:
            possible_x = self.x + move[0]
            possible_y = self.y + move[1]
            if chk_move(self, self.color, possible_x, possible_y, board):
                legal_moves.add((possible_x, possible_y))
                if (board.board_[possible_y][possible_x] is not None) and (board.board_[possible_y][possible_x].color != self.color):
                    self.attacking.add((possible_x, possible_y))
        return legal_moves

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        if (color == 'w'):
            self.sprite = pygame.image.load('resources\\wqueen.png')
        else: self.sprite = pygame.image.load('resources\\bqueen.png')

    def generate_moves(self, board):
        return get_diag_moves(self,board).union(get_straight_moves(self,board))


