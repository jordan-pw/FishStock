"""
Module handles the visual component of the chessboard and pieces
"""
import pygame
from pygame.constants import *
import sys

width, height = 800, 800
screen = pygame.display.set_mode((width, height))

surface = pygame.image.load('resources\\Board2.png').convert()
surface = pygame.transform.scale(surface, (width, height))

rect = surface.get_rect()
rect = rect.move((0, 0))
screen.blit(surface, rect)

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