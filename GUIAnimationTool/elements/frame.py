from utils import *


class Frame:
    def __init__(self, rows, cols, start_color):
        self.rows = rows
        self.cols = cols
        self.start_color = start_color
        self.grid = init_grid(rows, cols, start_color)

    def is_coord_valid(self, coord):
        if coord.x < 0 or coord.x >= self.cols:
            return False

        if coord.y < 0 or coord.y >= self.rows:
            return False

        return True

    def paint_pixel(self, x, y, color):
        if not self.is_coord_valid(Vector2(x, y)):
            return

        self.grid[y][x] = color

    def flood_fill_pixel(self, x, y, fill_color, original_color=None):

        print(Vector2(x, y))
        if not self.is_coord_valid(Vector2(x, y)):
            return

        if original_color is None:
            original_color = self.grid[y][x]

        if self.grid[y][x] != original_color or self.grid[y][x] == fill_color:
            return

        self.paint_pixel(x, y, fill_color)

        self.flood_fill_pixel(x + 1, y, fill_color, original_color)
        self.flood_fill_pixel(x - 1, y, fill_color, original_color)
        self.flood_fill_pixel(x, y + 1, fill_color, original_color)
        self.flood_fill_pixel(x, y - 1, fill_color, original_color)

    def clear(self):
        self.grid = init_grid(self.rows, self.cols, self.start_color)

    def get_surface(self, rect, grid_lines_width=-1):

        frame_surface = pygame.Surface(rect.size)

        width, height = rect.size
        pixel_size = width // self.rows
        for y, row in enumerate(self.grid):
            for x, cell_color in enumerate(row):
                pygame.draw.rect(frame_surface, cell_color, (
                    x * pixel_size, y * pixel_size,  # (x, y) position of the cell
                    pixel_size, pixel_size  # the size of the cell
                ))

        if grid_lines_width != -1:
            for i in range(0, self.rows + 1):
                pygame.draw.line(frame_surface, BLACK, (0, i * pixel_size + grid_lines_width / 2),
                                 (width, i * pixel_size + grid_lines_width / 2), grid_lines_width)
            i = self.rows
            pygame.draw.line(frame_surface, BLACK, (0, i * pixel_size - grid_lines_width / 2),
                             (width, i * pixel_size - grid_lines_width / 2), grid_lines_width)

            for i in range(0, self.cols):
                pygame.draw.line(frame_surface, BLACK, (i * pixel_size + grid_lines_width / 2, 0),
                                 (i * pixel_size + grid_lines_width / 2, height), grid_lines_width)
            i = self.cols
            pygame.draw.line(frame_surface, BLACK, (i * pixel_size - grid_lines_width / 2, 0),
                             (i * pixel_size - grid_lines_width / 2, height), grid_lines_width)

        return frame_surface


def init_grid(rows, cols, start_color):
    grid = []

    for i in range(0, rows):
        grid.append([])
        for _ in range(0, cols):
            grid[i].append(start_color)

    return grid
