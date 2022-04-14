import pygame.time

from utils import *


class Preview:
    def __init__(self, rect, timeline):
        self.rect = rect
        self.clock = pygame.time.Clock()
        self.run = True
        self.timeline = timeline
        self.current_frame_index = 0

        self.frame_rect = pygame.Rect(PREVIEW_PADDING, PREVIEW_PADDING, rect.width - 2 * PREVIEW_PADDING, rect.width - 2 * PREVIEW_PADDING)

    def start(self):
        while self.run:
            self.clock.tick(1)

            self.current_frame_index += 1
            self.current_frame_index %= len(self.timeline.timeline_frames)

    def reset(self):
        self.current_frame_index = 0

    def get_surface(self):

        preview_surface = pygame.Surface(self.rect.size)
        preview_surface.fill(WHITE)

        frame = self.timeline.timeline_frames[self.current_frame_index].frame
        frame_surface = frame.get_surface(self.frame_rect)
        preview_surface.blit(frame_surface, self.frame_rect)

        pygame.draw.rect(preview_surface, BLACK, self.frame_rect, PREVIEW_PADDING)

        return preview_surface
