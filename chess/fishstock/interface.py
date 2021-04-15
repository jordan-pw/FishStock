"""
Module handles the visual component of the chessboard and pieces
"""

import pygame
import sys

# Initialize pygame display
width, height = 800, 800
board_offset = 13 # Size of padding on board sprite
screen = pygame.display.set_mode((width, height))

# Load in images
surface = pygame.image.load('resources\\Board2.png').convert()
surface = pygame.transform.scale(surface, (width, height))

# Render images
rect = surface.get_rect()
rect = rect.move((0, 0))
screen.blit(surface, rect)

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
    pygame.display.update()

def load_pieces(board):
    pieces = board.array
    print(test)
    for row in pieces:
        for item in row:
            print(test)
            posx = array[row][item].x
            posx = array[row][item].y
            psprite = array[row][item].sprite
            psprite = pygame.transform.scale(psprite, (width, height))
            screen.blit(psprite, (board_offset+(posx*100), board_offset+(posy*100)))
            