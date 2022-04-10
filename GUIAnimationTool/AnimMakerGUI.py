# Based on 'Make Paint in Python'
# https://www.youtube.com/watch?v=N20eXcfyQ_4
from utils import *

# Pygame variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PiPet Animation Maker")
clock = pygame.time.Clock()


def init_grid(rows, cols, start_color):
    grid = []

    for i in range(0, rows):
        grid.append([])
        for _ in range(0, cols):
            grid[i].append(start_color)

    return grid


# TODO: Draw the grid to a different canvas instead of directly to the main display
def draw(win, grid):
    def draw_grid(WIN, grid):
        for y, row in enumerate(grid):
            for x, cell_color in enumerate(row):
                pygame.draw.rect(WIN, cell_color, (
                    x * PIXEL_SIZE, y * PIXEL_SIZE,  # (x, y) position of the cell
                    PIXEL_SIZE, PIXEL_SIZE  # the size of the cell
                ))

    win.fill(BG_COLOR)
    draw_grid(WIN, grid)
    pygame.display.update()


# Main game Loop
def main():

    grid = init_grid(ROWS, COLS, BLUE)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(WIN, grid)

    pygame.quit()


if __name__ == "__main__":
    main()
