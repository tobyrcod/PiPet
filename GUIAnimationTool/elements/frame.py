from utils import *


class Frame:
    def __init__(self, rows, cols, start_color):
        self.grid = init_grid(rows, cols, start_color)

    def get_surface(self, rect):
        frame_surface = pygame.Surface(rect.size)

        frame_surface.fill(BLACK)

        return frame_surface


def init_grid(rows, cols, start_color):
    grid = []

    for i in range(0, rows):
        grid.append([])
        for _ in range(0, cols):
            grid[i].append(start_color)

    return grid
