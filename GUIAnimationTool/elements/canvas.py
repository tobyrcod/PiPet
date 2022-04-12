from utils import *
from .frame import Frame


# TODO: Upgrade to use frames instead of handling the grid directly, i.e make the canvas display the frames that are
#  in the animator, not the other way round
class Canvas:
    def __init__(self, rect):
        self.rect = rect
        self.draw_color = BLACK
        self.frame = None
        self.pixel_size = -1

    def set_frame(self, frame):
        self.frame = frame
        self.pixel_size = self.rect.width // frame.rows

    def get_coord_from_pos(self, pos):
        x, y = pos
        coord = Vector2(x // self.pixel_size, y // self.pixel_size)

        if coord.x < 0 or coord.x >= COLS:
            return None

        if coord.y < 0 or coord.y >= ROWS:
            return None

        return coord

    # I hate this button argument please fix it...
    # it should be color
    def change_draw_color(self, color):
        self.draw_color = color

    def clear(self):
        self.draw_color = BLACK

        if self.frame is not None:
            self.frame.clear()

    def clicked(self, mouse_pos):
        if self.frame is not None:
            local_pos = np.subtract(mouse_pos, self.rect.topleft)
            coord = self.get_coord_from_pos(local_pos)
            # Clicked on the canvas
            self.frame.paint_pixel(*coord, self.draw_color)

    def get_surface(self):
        canvas_surface = pygame.Surface(self.rect.size)
        canvas_surface.fill(WHITE)

        if self.frame is not None:
            frame_rect = pygame.Rect(0, 0, *self.rect.size)
            frame_surface = self.frame.get_surface(frame_rect, GRID_LINE_WIDTH)
            canvas_surface.blit(frame_surface, frame_rect)

        return canvas_surface
