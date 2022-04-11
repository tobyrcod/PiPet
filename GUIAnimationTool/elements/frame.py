from utils import *


# TODO: IMPORTANT! Split the frame into a 'frame' and a 'frame visual' class to handle the 'get_surface' method!
class Frame:
    def __init__(self, rows, cols, start_color):
        self.rows = rows
        self.cols = cols
        self.start_color = start_color
        self.grid = init_grid(rows, cols, start_color)

    def paint_pixel(self, x, y, color):
        self.grid[y][x] = color

    def clear(self):
        self.grid = init_grid(self.rows, self.cols, self.start_color)

    def get_surface(self, rect, draw_grid_lines=True):

        frame_surface = pygame.Surface(rect.size)

        width, height = rect.size
        pixel_size = width // self.rows

        for y, row in enumerate(self.grid):
            for x, cell_color in enumerate(row):
                pygame.draw.rect(frame_surface, cell_color, (
                    x * pixel_size, y * pixel_size,  # (x, y) position of the cell
                    pixel_size, pixel_size  # the size of the cell
                ))

        if draw_grid_lines:
            for i in range(0, ROWS + 1):
                pygame.draw.line(frame_surface, BLACK, (0, i * pixel_size + GRID_LINE_WIDTH / 2),
                                 (width, i * pixel_size + GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)
            i = ROWS
            pygame.draw.line(frame_surface, BLACK, (0, i * pixel_size - GRID_LINE_WIDTH / 2),
                             (width, i * pixel_size - GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)

            for i in range(0, COLS):
                pygame.draw.line(frame_surface, BLACK, (i * pixel_size + GRID_LINE_WIDTH / 2, 0),
                                 (i * pixel_size + GRID_LINE_WIDTH / 2, height), GRID_LINE_WIDTH)
            i = COLS
            pygame.draw.line(frame_surface, BLACK, (i * pixel_size - GRID_LINE_WIDTH / 2, 0),
                             (i * pixel_size - GRID_LINE_WIDTH / 2, height), GRID_LINE_WIDTH)

        return frame_surface


def init_grid(rows, cols, start_color):
    grid = []

    for i in range(0, rows):
        grid.append([])
        for _ in range(0, cols):
            grid[i].append(start_color)

    return grid
