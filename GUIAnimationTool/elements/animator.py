from utils import *
from .timeline import Timeline


class Animator:
    def __init__(self, rect):
        self.rect = rect

        timeline_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, self.rect.width - 2 * FRAME_PADDING, (self.rect.height - 3 * FRAME_PADDING) * 0.8)
        self.timeline = Timeline(timeline_rect)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.timeline.viewport_rect.collidepoint(local_pos):
            self.timeline.clicked(local_pos)

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)
        animator_surface.fill(WHITE)

        timeline_surface = self.timeline.get_surface()
        animator_surface.blit(timeline_surface, self.timeline.viewport_rect)

        return animator_surface
