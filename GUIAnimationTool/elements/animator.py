from utils import *
from .timeline import Timeline
from.scrollbar import Scrollbar


class Animator:
    def __init__(self, rect):
        self.rect = rect

        padding_space = 3 * FRAME_PADDING
        timeline_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, self.rect.width - 2 * FRAME_PADDING, (self.rect.height - padding_space) * 0.7)
        self.timeline = Timeline(timeline_rect)

        scrollbar_rect = pygame.Rect(FRAME_PADDING, timeline_rect.bottom + FRAME_PADDING, timeline_rect.width, (self.rect.height - timeline_rect.height - padding_space) / 2)
        self.scrollbar = Scrollbar(scrollbar_rect, self.timeline.rect.width, self.timeline.content_width)

        self.timeline.events.on_content_width_changed += self.scrollbar.set_content_width
        self.timeline.new_frame_button.events.on_clicked += lambda: self.scrollbar.scroll_block.move_scroll_block(99999)
        self.scrollbar.events.on_offset_changed += self.timeline.set_content_offset

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.timeline.rect.collidepoint(local_pos):
            self.timeline.clicked(local_pos)
        elif self.scrollbar.rect.collidepoint(local_pos):
            self.scrollbar.clicked(local_pos)

    # TODO: USE EVENTS INSTEAD OF THIS NESTING HELL
    def held(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.scrollbar.rect.collidepoint(local_pos):
            self.scrollbar.held(local_pos)

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)
        animator_surface.fill(WHITE)

        timeline_surface = self.timeline.get_surface()
        animator_surface.blit(timeline_surface, self.timeline.rect)

        scollbar_surface = self.scrollbar.get_surface()
        animator_surface.blit(scollbar_surface, self.scrollbar.rect)

        return animator_surface
