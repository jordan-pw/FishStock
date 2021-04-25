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

# Render images
rect = surface.get_rect()
rect = rect.move((0, 0))
screen.blit(surface, rect)

# Set variables
black_check = False # True when king is in check
white_check = False
turn = 'w' # w when White's move, b when Black's move

def draw_pieces(board):
    pieces = board.board_
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            the_piece = pieces[i][j]
            if the_piece is not None:
                posx = pieces[i][j].x
                posy = pieces[i][j].y
                psprite = pieces[i][j].sprite
                screen.blit(psprite, (board_offset+(posx*100), board_offset+(posy*100)))


the_board = Board()
all = the_board.board_


def update_moves():
    """
    For every piece on the board, generates all pseudo-legal moves
    This updates the attack boards for both black and white
    """
    for row in all:
        for item in row:
            if item is not None:
                item.generate_legal_moves(the_board)


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
    draw_pieces(the_board)
    pygame.display.update()

    # Gameplay loop
    chk_black_check = the_board.black_king.attacked_by
    chk_white_check = the_board.white_king.attacked_by
    turn_string = "White's turn"
    if (len(chk_white_check)) or (len(chk_black_check)):
        pygame.display.set_caption('Chess! (Check) ' + turn_string)
    else: pygame.display.set_caption('Chess! ' + turn_string)
    if turn == 'w':
        update_moves()
        turn_string = "White's turn"
    else: # Black's turn
        update_moves()
        turn_string = "Black's turn"
    

# Board evaluation initiliazitaion
pawn_map = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0,
]

knight_map = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

bishop_map = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]

rook_map = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]

queen_map = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]

king_map = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]

