from utils import *
from .timeline import Timeline
from.scrollbar import Scrollbar

class Animator:
    def __init__(self, rect):
        self.rect = rect

        padding_space = 4 * FRAME_PADDING
        timeline_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, self.rect.width - 2 * FRAME_PADDING, (self.rect.height - padding_space) * 0.8)
        self.timeline = Timeline(timeline_rect)

        scrollbar_rect = pygame.Rect(FRAME_PADDING, timeline_rect.bottom + FRAME_PADDING, timeline_rect.width, (self.rect.height - timeline_rect.height - padding_space) / 2)
        self.scrollbar = Scrollbar(scrollbar_rect)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.timeline.rect.collidepoint(local_pos):
            self.timeline.clicked(local_pos)

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)
        animator_surface.fill(WHITE)

        timeline_surface = self.timeline.get_surface()
        animator_surface.blit(timeline_surface, self.timeline.rect)

        scollbar_surface = self.scrollbar.get_surface()
        animator_surface.blit(scollbar_surface, self.scrollbar.rect)

        return animator_surface
