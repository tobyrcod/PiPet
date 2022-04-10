import pygame
pygame.init()
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pygame Settings
FPS = 60
WIDTH, HEIGHT = 600, 700

# Canvas Settings
ROWS = COLS = 8
TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // ROWS
BG_COLOR = WHITE
DRAW_GRID_LINES = True

# Other
FONT_NAME = "Ariel"


# Methods
def get_font(size):
    return pygame.font.SysFont(FONT_NAME, size)
