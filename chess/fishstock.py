"""
Module handles the user input, decision making, and AI
"""
from board import *
import pygame
import sys

# Initialize pygame display
width, height = 826, 826
board_offset = 13 # Size of padding on board sprite
screen = pygame.display.set_mode((width, height))

# Load in images
surface = pygame.image.load('resources\\Board2.png').convert()
select = pygame.image.load('resources\\selection.png').convert_alpha()
highlight = pygame.image.load('resources\\highlight.png').convert_alpha()
highlightred = pygame.image.load('resources\\highlight_red.png').convert_alpha()
highlightgreen = pygame.image.load('resources\\highlight_green.png').convert_alpha()


# Set variables
black_check = False # True when king is in check
white_check = False
selected = False # True when a piece is selected
selection = None # Currently selected piece
debug = True # Enables extra highlighting, and allows you to move both sides
turn = 'w' # w when White's move, b when Black's move
playerc = 'w'
computerc = 'b'
color = (255, 0, 0)

def draw_pieces(board):
    """
    Loops through all the pieces on the board and draws them
    """
    pieces = board.board_
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            the_piece = pieces[i][j]
            if the_piece is not None:
                posx = pieces[i][j].x
                posy = pieces[i][j].y
                psprite = pygame.image.load(pieces[i][j].sprite).convert()
                screen.blit(psprite, (board_offset+(posx*100), board_offset+(posy*100)))

def show_position():
    """
    Highlights the square the mouse is currently over
    """
    x, y = pygame.mouse.get_pos()
    x = ((x // 100) * 100) + board_offset - 1
    y = ((y // 100) * 100) + board_offset - 1
    screen.blit(select, (x, y))

def highlight_moves(moveset):
    """
    Highlights all of the squares in a given set of moves
    Args:
        A piece's legal_move set()
    """
    for move in moveset:
        screen.blit(highlight, (move[0]*100 + board_offset, move[1]*100 + board_offset))

def select_piece(piece):
    """
    Selects a piece, and calls the highlight_moves method
    Args:
        A piece object
    """
    if piece is not None:
        screen.blit(highlight, (piece.x*100 + board_offset, piece.y*100 + board_offset))
        piece.generate_legal_moves(the_board)
        highlight_moves(piece.legal_moves)
        if debug == True:
            for attack in piece.attacked_by:
                screen.blit(highlightgreen, (attack[0]*100 + board_offset, attack[1]*100 + board_offset))
            for target in piece.attacking:
                screen.blit(highlightred, (target[0]*100 + board_offset, target[1]*100 + board_offset))

def check_square():
    """
    Checks the square of the board the mouse is currently over,
    selecting a piece if there is one
    Returns:
        selection: The object that was under the mouse at the time of checking
    """
    x, y = pygame.mouse.get_pos()
    selection = the_board.board_[y // 100][x // 100]
    if selection is not None: #and selection.color == playerc:
        return selection
    if selection is None:
        return None

def attempt_move(piece):
    """
    Attempts to make a move if the target coordinate is a legal move.
    Returns:
        True if the move is made, False otherwise
    """
    x, y = pygame.mouse.get_pos()
    x = x // 100
    y = y // 100
    if (piece is not None) and (x, y) in piece.legal_moves:
        piece.move(the_board, x, y)
        initialize_moves()
        update_moves()
        return True
    return False




the_board = Board(computerc, playerc)
all = the_board.board_

def initialize_moves():
    for row in all:
        for item in row:
            if item is not None:
                item.generate_moves(the_board)

def update_moves():
    """
    For every piece on the board, generates all pseudo-legal moves
    This updates the attack boards for both black and white
    """
    for row in all:
        for item in row:
            if item is not None:
                item.attacked_by = set()
                item.attacking = set()

    initialize_moves()
    
    for row in all:
        for item in row:
            if item is not None:
                item.generate_legal_moves(the_board)    
    the_board.bottom_king.check_status()
    the_board.top_king.check_status()

initialize_moves()
update_moves()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        # pylint: disable=no-member
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        # pylint: enable=no-member
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(selected)
            print(the_board.bottom_king.attacked_by)
            if selected == False:
                selection = check_square()
                if selection is not None:
                    selected = True
            if selected == True:
                if attempt_move(selection):
                    selected = False
                    selection = None
                else:
                    selection = check_square()
                    if selection is not None:
                        selected = True

    # Render pieces and other bits
    screen.blit(surface, (0,0))
    select_piece(selection)
    draw_pieces(the_board)
    show_position()
    pygame.display.update()

    # Gameplay loop
    chk_black_check = the_board.bottom_king.attacked_by
    chk_white_check = the_board.top_king.attacked_by
    # Generate caption
    turn_string = "White's turn"
    if (the_board.bottom_king.is_in_check) or (the_board.top_king.is_in_check):
        pygame.display.set_caption('Chess! (Check) ' + turn_string)
    else: pygame.display.set_caption('Chess! ' + turn_string)
    if turn == 'w':
        #update_moves()
        turn_string = "White's turn"
    else: # Black's turn
        #update_moves()
        turn_string = "Black's turn"
    


