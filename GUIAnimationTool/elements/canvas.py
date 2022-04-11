from utils import *


class Canvas:
    def __init__(self, rect):
        self.rect = rect
        self.draw_color = BLACK
        self.grid = self.init_grid(ROWS, COLS, WHITE)

    def init_grid(self, rows, cols, start_color):
        grid = []

        for i in range(0, rows):
            grid.append([])
            for _ in range(0, cols):
                grid[i].append(start_color)

        return grid

    def get_coord_from_pos(self, pos):
        x, y = pos
        coord = Vector2(x // PIXEL_SIZE, y // PIXEL_SIZE)

        if coord.x < 0 or coord.x >= COLS:
            return None

        if coord.y < 0 or coord.y >= ROWS:
            return None

        return coord

    def paint_pixel(self, x, y):
        self.grid[y][x] = self.draw_color

    # I hate this button argument please fix it...
    # it should be color
    def change_draw_color(self, color):
        self.draw_color = color

    def reset(self):
        self.draw_color = BLACK
        self.grid = self.init_grid(ROWS, COLS, WHITE)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        coord = self.get_coord_from_pos(local_pos)
        # Clicked on the canvas
        self.paint_pixel(*coord)

    def get_surface(self):

        width, height = self.rect.size
        canvas_surface = pygame.Surface(self.rect.size)

        for y, row in enumerate(self.grid):
            for x, cell_color in enumerate(row):
                pygame.draw.rect(canvas_surface, cell_color, (
                    x * PIXEL_SIZE, y * PIXEL_SIZE,  # (x, y) position of the cell
                    PIXEL_SIZE, PIXEL_SIZE  # the size of the cell
                ))

        if DRAW_GRID_LINES:
            for i in range(0, ROWS + 1):
                pygame.draw.line(canvas_surface, BLACK, (0, i * PIXEL_SIZE + GRID_LINE_WIDTH / 2),
                                 (width, i * PIXEL_SIZE + GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)
            i = ROWS
            pygame.draw.line(canvas_surface, BLACK, (0, i * PIXEL_SIZE - GRID_LINE_WIDTH / 2),
                             (width, i * PIXEL_SIZE - GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)

            for i in range(0, COLS):
                pygame.draw.line(canvas_surface, BLACK, (i * PIXEL_SIZE + GRID_LINE_WIDTH / 2, 0),
                                 (i * PIXEL_SIZE + GRID_LINE_WIDTH / 2, height), GRID_LINE_WIDTH)
            i = COLS
            pygame.draw.line(canvas_surface, BLACK, (i * PIXEL_SIZE - GRID_LINE_WIDTH / 2, 0),
                             (i * PIXEL_SIZE - GRID_LINE_WIDTH / 2, height), GRID_LINE_WIDTH)
        return canvas_surface