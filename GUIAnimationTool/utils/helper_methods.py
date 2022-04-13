from .settings import *


def get_font(size):
    return pygame.font.SysFont(FONT_NAME, size)


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))