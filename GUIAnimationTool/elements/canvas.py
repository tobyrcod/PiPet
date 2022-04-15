from utils import *
from .frame import Frame
from interfaces import IClickable


class Canvas(IClickable):
    def __init__(self, rect):
        super().__init__(rect)

        self.set_to_brush()

        self.draw_color = BLACK

        self.frame = None
        self.pixel_size = -1

    def set_frame(self, frame):
        self.frame = frame
        self.pixel_size = self.rect.width // frame.rows

    def set_to_brush(self):
        self.events.on_clicked.remove_all_callbacks()
        self.events.on_clicked += lambda coord: self.frame.paint_pixel(*coord, self.draw_color)

    def set_to_fill(self):
        self.events.on_clicked.remove_all_callbacks()
        self.events.on_clicked += lambda coord: self.frame.flood_fill_pixel(*coord, self.draw_color)

    def set_to_erase(self):
        self.events.on_clicked.remove_all_callbacks()
        self.events.on_clicked += lambda coord: self.frame.paint_pixel(*coord, WHITE)

    def get_coord_from_pos(self, pos):
        x, y = pos
        coord = Vector2(x // self.pixel_size, y // self.pixel_size)

        if coord.x < 0 or coord.x >= COLS:
            return None

        if coord.y < 0 or coord.y >= ROWS:
            return None

        return coord

    def change_draw_color(self, color):
        self.draw_color = color

    def clear(self):
        if self.frame is not None:
            self.frame.clear()

    def clicked(self, mouse_pos):
        if self.frame is not None:
            local_pos = np.subtract(mouse_pos, self.rect.topleft)
            coord = self.get_coord_from_pos(local_pos)
            # Clicked on the canvas
            self.events.on_clicked(coord)

    def get_surface(self):
        canvas_surface = pygame.Surface(self.rect.size)
        canvas_surface.fill(WHITE)

        if self.frame is not None:
            frame_rect = pygame.Rect(0, 0, *self.rect.size)
            frame_surface = self.frame.get_surface(frame_rect, GRID_LINE_WIDTH)
            canvas_surface.blit(frame_surface, frame_rect)

        return canvas_surface
