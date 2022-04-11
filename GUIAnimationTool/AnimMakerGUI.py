# Based on 'Make Paint in Python'
# https://www.youtube.com/watch?v=N20eXcfyQ_4
from utils import *

# TODO: Change application icon

# Pygame variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PiPet Animation Maker")
clock = pygame.time.Clock()


class Canvas:
    def __init__(self):
        self.grid = self.init_grid(ROWS, COLS, WHITE)
        self.draw_color = RED

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

    def change_draw_color(self, new_color):
        self.draw_color = new_color

    def clicked(self, mouse_pos):
        coord = self.get_coord_from_pos(mouse_pos)
        # Clicked on the canvas
        self.paint_pixel(*coord)

    def get_surface(self):

        canvas_surface = pygame.Surface([WIDTH, WIDTH])

        for y, row in enumerate(self.grid):
            for x, cell_color in enumerate(row):
                pygame.draw.rect(canvas_surface, cell_color, (
                    x * PIXEL_SIZE, y * PIXEL_SIZE,  # (x, y) position of the cell
                    PIXEL_SIZE, PIXEL_SIZE  # the size of the cell
                ))

        if DRAW_GRID_LINES:
            for i in range(0, ROWS + 1):
                pygame.draw.line(canvas_surface, BLACK, (0, i * PIXEL_SIZE + GRID_LINE_WIDTH / 2),
                                 (WIDTH, i * PIXEL_SIZE + GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)
            i = ROWS
            pygame.draw.line(canvas_surface, BLACK, (0, i * PIXEL_SIZE - GRID_LINE_WIDTH / 2),
                             (WIDTH, i * PIXEL_SIZE - GRID_LINE_WIDTH / 2), GRID_LINE_WIDTH)

            for i in range(0, COLS):
                pygame.draw.line(canvas_surface, BLACK, (i * PIXEL_SIZE + GRID_LINE_WIDTH / 2, 0),
                                 (i * PIXEL_SIZE + GRID_LINE_WIDTH / 2, HEIGHT - TOOLBAR_HEIGHT), GRID_LINE_WIDTH)
            i = COLS
            pygame.draw.line(canvas_surface, BLACK, (i * PIXEL_SIZE - GRID_LINE_WIDTH / 2, 0),
                             (i * PIXEL_SIZE - GRID_LINE_WIDTH / 2, HEIGHT - TOOLBAR_HEIGHT), GRID_LINE_WIDTH)
        return canvas_surface


class Toolbar:
    def __init__(self):
        button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
        self.buttons = [
            Button(10, button_y, 50, 50, BLACK),
            Button(70, button_y, 50, 50, RED),
            Button(130, button_y, 50, 50, GREEN),
            Button(190, button_y, 50, 50, BLUE),
            Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
        ]

    def clicked(self, mouse_pos):
        for button in self.buttons:
            if not button.is_mouse_over(mouse_pos):
                continue

            # If we clicked on this button
            button.button_events.on_clicked(button)

    def draw(self, win):
        for button in self.buttons:
            button.draw(win)


# Main game Loop
def main():

    canvas = Canvas()
    toolbar = Toolbar()

    for button in toolbar.buttons:
        button.button_events.on_clicked += lambda button: canvas.change_draw_color(button.color)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                canvas.clicked(mouse_pos)

        draw(WIN, canvas, toolbar)

    pygame.quit()


# TODO: Draw the grid to a different canvas instead of directly to the main display TODO?: Instead of redrawing the
#  whole grid just redraw the pixels (if any) that change this frame. '?' because this is just for optimisation,
#  and realistically that doesn't matter at all for this simple use case
def draw(win, canvas, toolbar):

    win.fill(BG_COLOR)

    canvas_surface = canvas.get_surface()
    win.blit(canvas_surface, (0, 0))

    toolbar.draw(win)

    pygame.display.update()


# Only run if this file is loaded directly (not through a module import)
if __name__ == "__main__":
    main()
