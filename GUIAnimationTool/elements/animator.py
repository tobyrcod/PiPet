from utils import *
from .frame import Frame


class Animator:
    def __init__(self, rect):
        self.rect = rect
        self.frames = []
        self.frames.append(self.make_new_frame())

    def make_new_frame(self):
        frame = Frame(ROWS, COLS, WHITE)
        return frame

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)

        animator_surface.fill(WHITE)

        frame_rect = pygame.Rect(0, 0, FRAME_WIDTH, (self.rect.height - 3 * PADDING) * 0.8)
        for i, frame in enumerate(self.frames):
            frame_rect.topleft = (PADDING + i * (FRAME_WIDTH + PADDING), PADDING)

            frame_surface = frame.get_surface(frame_rect)
            animator_surface.blit(frame_surface, frame_rect)

        font = get_font(size=30)
        text_surface = font.render("Animator", 1, BLACK)
        animator_surface.blit(text_surface, (
            0,
            self.rect.height - text_surface.get_height()
        ))

        return animator_surface
