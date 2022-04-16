from operator import inv
import pygame
import os
from .file_handler import *
from collections import namedtuple
from events import Events
pygame.init()
pygame.font.init()

# Palette Colors
KEY_COLOR_DICT = get_color_dict(os.path.abspath('colors.json'))

# Menu Settings
PADDING = 15
WHITE = KEY_COLOR_DICT["w"]
BLACK = KEY_COLOR_DICT["bk"]
RED = KEY_COLOR_DICT["r"]
GREEN = KEY_COLOR_DICT["g"]
BLUE = KEY_COLOR_DICT['be']
GREY = [100, 100, 100]

# Frame Settings
ROWS = COLS = 8
FRAME_PADDING = 10
FRAME_WIDTH = 2 * FRAME_PADDING + ROWS * 10

# Canvas Settings
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
GRID_LINE_WIDTH = 5
DRAW_GRID_LINES = True

# Preview Settings
PREVIEW_PADDING = 10
PREVIEW_WIDTH = 2 * PREVIEW_PADDING + ROWS * 23
PREVIEW_HEIGHT = PREVIEW_WIDTH + 50

# Toolbar Settings
TOOLBAR_WIDTH, TOOLBAR_HEIGHT = PREVIEW_WIDTH, CANVAS_HEIGHT
TOOLBAR_COLUMNS = 3
TOOLBAR_PADDING = 10

# Animator Settings
ANIMATOR_WIDTH, ANIMATOR_HEIGHT = TOOLBAR_WIDTH + CANVAS_WIDTH - PREVIEW_WIDTH, PREVIEW_HEIGHT

# Menu Bar
MENU_BAR_WIDTH, MENU_BAR_HEIGHT = PADDING + CANVAS_WIDTH + PADDING + TOOLBAR_WIDTH + PADDING, \
                                  50

# Scrollbar
SCROLL_PADDING = 4

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
WIDTH, HEIGHT = MENU_BAR_WIDTH, \
                PADDING + MENU_BAR_HEIGHT + PADDING + CANVAS_HEIGHT + PADDING + PREVIEW_HEIGHT
