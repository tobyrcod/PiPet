import pygame
from collections import namedtuple
from events import Events
pygame.init()
pygame.font.init()

# Palette Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Menu Settings
PADDING = 15

# Canvas Settings
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
GRID_LINE_WIDTH = 5
DRAW_GRID_LINES = True

# Toolbar Settings
TOOLBAR_WIDTH, TOOLBAR_HEIGHT = 200, CANVAS_HEIGHT
TOOLBAR_COLUMNS = 2
TOOLBAR_PADDING = 10

# Preview Settings
PREVIEW_WIDTH, PREVIEW_HEIGHT = TOOLBAR_WIDTH, TOOLBAR_WIDTH

# Animator Settings
ANIMATOR_WIDTH, ANIMATOR_HEIGHT = TOOLBAR_WIDTH + CANVAS_WIDTH - PREVIEW_WIDTH, PREVIEW_HEIGHT

# Frame Settings
ROWS = COLS = 8
FRAME_PADDING = 10
FRAME_WIDTH = 2 * FRAME_PADDING + ROWS * 8

# Menu Colors
ACCENT_RED = (255, 0, 75)
DARK_BROWN = (45, 33, 27)
DARK_BLUE = (1, 118, 122)
LIGHT_BLUE = (1, 197, 189)
CREAM = (249, 248, 201)

# Other
FONT_NAME = "Ariel"
Vector2 = namedtuple('Vector2', 'x y')

# Pygame Settings
FPS = 60
WIDTH, HEIGHT = PADDING + CANVAS_WIDTH + PADDING + TOOLBAR_WIDTH + PADDING, \
                PADDING + CANVAS_HEIGHT + PADDING + PREVIEW_HEIGHT + PADDING


# Methods
def get_font(size):
    return pygame.font.SysFont(FONT_NAME, size)
