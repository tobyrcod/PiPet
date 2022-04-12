import numpy as np

from utils import *
from .frame import Frame
from interfaces import IClickable


class Timeline:
    def __init__(self, rect):
        self.rect = rect
        
        self.frames = []
        self.timeline_frames = []
        self.active_timeline_frame_index = -1
        self.events = TimelineEvents()

        self.timeline_frame_rect = pygame.Rect(0, 0, FRAME_WIDTH, self.rect.height)

        new_frame_button_rect = pygame.Rect(0, 0, FRAME_WIDTH * 0.7, FRAME_WIDTH * 0.7)
        self.new_frame_button = Button(new_frame_button_rect, WHITE, "New")
        self.new_frame_button.events.on_clicked += self.add_new_frame

        self.content_width = new_frame_button_rect.width
        self.content_offset = 20

    def init(self):
        self.add_new_frame()

    def add_new_frame(self):
        new_timeline_frame_index = new_frame_index = len(self.frames)

        frame = Frame(ROWS, COLS, WHITE)
        self.frames.append(frame)

        timeline_frame = TimelineFrame(pygame.Rect(self.timeline_frame_rect), new_timeline_frame_index, new_frame_index)
        timeline_frame.events.on_clicked += lambda a: self.set_active_timeline_frame_index(a.timeline_frame_index)
        self.timeline_frames.append(timeline_frame)
        self.content_width += timeline_frame.rect.width + FRAME_PADDING

        self.set_active_timeline_frame_index(timeline_frame.timeline_frame_index)

    def set_active_timeline_frame_index(self, timeline_frame_index):
        timeline_frame_index %= len(self.timeline_frames)
        self.active_timeline_frame_index = timeline_frame_index
        self.events.on_active_timeline_frame_index_changed(self.active_timeline_frame_index)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        local_pos = np.add(local_pos, (self.content_offset, 0))

        if self.new_frame_button.rect.collidepoint(local_pos):
            self.new_frame_button.events.on_clicked()
        else:
            for timeline_frame in self.timeline_frames:
                if timeline_frame.rect.collidepoint(local_pos):
                    timeline_frame.events.on_clicked(timeline_frame)

    def get_surface(self):

        timeline_surface = pygame.Surface(self.rect.size)
        timeline_surface.fill(GREEN)

        # Timeline Content
        content_rect = pygame.Rect(-self.content_offset, 0, self.content_width, self.rect.height)
        content_surface = pygame.Surface(content_rect.size)
        content_surface.fill(BLUE)

        # All the frames
        i = -1
        for i, timeline_frame in enumerate(self.timeline_frames):
            timeline_frame.rect.topleft = (i * (FRAME_WIDTH + FRAME_PADDING), 0)
            timeline_frame_surface = timeline_frame.get_surface(self.frames, i == self.active_timeline_frame_index)
            content_surface.blit(timeline_frame_surface, timeline_frame.rect)

        # Add new frame button
        i += 1
        self.new_frame_button.rect.topleft = (i * (FRAME_WIDTH + FRAME_PADDING), self.timeline_frame_rect.height / 2 - self.new_frame_button.rect.height / 2)
        new_frame_button_surface = self.new_frame_button.get_surface()
        content_surface.blit(new_frame_button_surface, self.new_frame_button.rect)

        timeline_surface.blit(content_surface, content_rect)
        return timeline_surface


class TimelineFrame(IClickable):
    def __init__(self, rect, timeline_frame_index, frame_index):
        super().__init__(rect)

        self.timeline_frame_index = timeline_frame_index
        self.frame_index = frame_index
        self.frame_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, rect.width - 2 * FRAME_PADDING, rect.width - 2 * FRAME_PADDING)

    def get_surface(self, frames, is_active_frame):

        timeline_frame_surface = pygame.Surface(self.rect.size)

        timeline_frame_surface.fill(BLACK)

        frame = frames[self.frame_index]
        frame_surface = frame.get_surface(self.frame_rect)
        timeline_frame_surface.blit(frame_surface, self.frame_rect)

        if is_active_frame:
            pygame.draw.rect(timeline_frame_surface, RED, (0, 0, *self.rect.size), 5)

        return timeline_frame_surface


class TimelineEvents(Events):
    __events__ = 'on_active_timeline_frame_index_changed'
