import pygame
from pygame.locals import *

pygame.init()

screen_size = screen_width, screen_height = 900, 1000
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sudoku Solver")

tile_size = screen_width / 9


def draw_grid():
    for line in range(10):
        width = 1
        if line % 3 == 0:
            width = 5
        pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (screen_width, line * tile_size), width=width)
        pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, screen_width), width=width)


run = True
while run:

    screen.fill((255, 255, 255))
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
