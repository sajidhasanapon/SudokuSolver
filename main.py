import pygame
import time
# import logic
from pygame.locals import *


def is_valid(board):
    # row validation
    for row in board:
        seen = set()
        for cell in row:
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)

    # column validation
    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)

    # slice validation
    for i in range(3):
        for j in range(3):
            seen = set()
            for p in range(3 * i, 3 * i + 3):
                for q in range(3 * j, 3 * j + 3):
                    cell = board[p][q]
                    if cell != 0:
                        if cell in seen:
                            return False
                        seen.add(cell)

    # no inconsistency found
    return True


def get_possibilities(board, row, col):
    ret = {1,2,3,4,5,6,7,8,9}
    invalid = set()

    for i in range(9):
        invalid.add(board[row][i])

    for j in range(9):
        invalid.add(board[j][col])

    slice_r = (row // 3) * 3
    slice_c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            invalid.add(board[slice_r + i][slice_c + j])

    return ret - invalid


def solver(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for x in get_possibilities(board, i, j):
                    board[i][j] = x
                    if solver(board):
                        return True
                board[i][j] = 0
                return False

    return True






pygame.init()

offset = 10
grid_size = 600
screen_size = screen_width, screen_height = 2 * offset + grid_size, offset + grid_size + 100
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Sudoku Solver")

# colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

tile_size = grid_size / 9
pos = [1, 2]
font = pygame.font.Font("freesansbold.ttf", 32)

grid = [[0] * 9 for _ in range(9)]
grid_text = []


def init_grid():
    pass


def show_text():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, black)
                text_rect = text.get_rect()
                text_rect.center = (offset + tile_size * (i + 0.5), offset + tile_size * (j + 0.5))
                screen.blit(text, text_rect)


def draw_grid():
    for line in range(10):
        width = 1
        if line % 3 == 0:
            width = 5

        # horizontal grid lines
        start = (offset, offset + line * tile_size)
        end = (offset + grid_size, offset + line * tile_size)
        pygame.draw.line(screen, black, start, end, width=width)

        # vertical grid lines
        start = (offset + line * tile_size, offset)
        end = (offset + line * tile_size, offset + grid_size)
        pygame.draw.line(screen, black, start, end, width=width)


def draw_highlighted_cell():
    left = offset + pos[0] * tile_size
    top = offset + pos[1] * tile_size
    width = tile_size
    height = tile_size
    pygame.draw.rect(screen, red, (left, top, width, height), width=5)


run = True
i = 0
while run:
    screen.fill(white)
    draw_grid()
    draw_highlighted_cell()
    show_text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(event.key)
            print(pygame.K_RETURN)
            if event.key == pygame.K_LEFT:
                pos[0] = (pos[0] + 8) % 9
            if event.key == pygame.K_RIGHT:
                pos[0] = (pos[0] + 1) % 9
            if event.key == pygame.K_UP:
                pos[1] = (pos[1] + 8) % 9
            if event.key == pygame.K_DOWN:
                pos[1] = (pos[1] + 1) % 9
            if 0 <= event.key-ord('0') <= 9:
                grid[pos[0]][pos[1]] = event.key-ord('0')
            if event.key == pygame.K_RETURN:
                solver(grid)

    pygame.display.update()

pygame.quit()
