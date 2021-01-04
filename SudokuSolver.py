import pygame
import logic
from pygame.locals import *
import PygameUtils as pu


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
blue = (0, 0, 255)
black = (0, 0, 0)
light_green = (0, 255, 0, 0.1)

tile_size = grid_size / 9
pos = [0, 0]
is_invalid_input = False
grid_font = pygame.font.SysFont("", 48)
message_font = pygame.font.SysFont("", 32)

grid = None
grid_text_color = None
# button = pu.button((150, 250, 150), 100, 650, 150, 50, "Solve")


def init_grid():
    global grid, grid_text_color
    grid = [[0] * 9 for _ in range(9)]
    grid_text_color = [[blue] * 9 for _ in range(9)]
    global is_invalid_input
    is_invalid_input = False


def show_text():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = grid_font.render(str(grid[i][j]), True, grid_text_color[i][j])
                text_rect = text.get_rect()
                text_rect.center = (offset + tile_size * (i + 0.5), offset + tile_size * (j + 0.5))
                screen.blit(text, text_rect)

    # show warning if input is not valid
    # else, prompt to press enter
    if is_invalid_input:
        text = message_font.render("Invalid input! Please overwrite the red digits.", True, red)
        text_rect = text.get_rect()
        text_rect.center = (300, 670)
        screen.blit(text, text_rect)
    else:
        messages = ["Navigation: Arrow keys", "Solve: ENTER", "Clear cell: 0", "Clear grid: x"]
        for i in range(len(messages)):
            text = message_font.render(messages[i], True, blue)
            text_rect = text.get_rect()
            text_rect.topleft = (100, 620+i*20)
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


def draw_button():
    # button.draw(screen)
    pass


def attempt_solve():
    if is_invalid_input:
        return

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid_text_color[i][j] = black
    logic.solve(grid)


def update_screen():
    screen.fill(white)
    # draw_button()
    draw_grid()
    draw_highlighted_cell()
    show_text()
    pygame.display.update()


def handle_events():
    for event in pygame.event.get():
        # mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
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
                global is_invalid_input
                is_invalid_input = logic.check_input(grid, grid_text_color)
            if event.key == pygame.K_x:
                init_grid()
            if event.key == pygame.K_RETURN:
                attempt_solve()

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if button.isOver(mouse_pos):
        #         print("Button")
        #     # elif checkb1.isOver(pos):
        #     #     checkb1.convert()
        #     #     print("Checkb1")
        #
        # if event.type == pygame.MOUSEMOTION:
        #     if button.isOver(mouse_pos):
        #         button.color = (100, 250, 100)
        #     else:
        #         button.color = (150, 250, 150)

init_grid()
while True:
    handle_events()
    update_screen()
