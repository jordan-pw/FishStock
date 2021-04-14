"""
Module handles the visual component of the chessboard and pieces
"""
import pygame
import sys

# Initialize pygame display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))

# Load in images
surface = pygame.image.load('resources\\Board2.png').convert()
surface = pygame.transform.scale(surface, (width, height))

# Render images
rect = surface.get_rect()
rect = rect.move((0, 0))
screen.blit(surface, rect)

# TODO
# to draw the pieces' sprites, multiply there x and y by 100, and add the offset of the borders of the board sprite

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