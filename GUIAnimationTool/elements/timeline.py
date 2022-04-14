import pygame

from utils import *
from .frame import Frame
from interfaces import IClickable


class Timeline:
    def __init__(self, rect):
        self.rect = rect

        self.timeline_frames = []
        self.active_timeline_frame_index = -1
        self.events = TimelineEvents()

        self.timeline_frame_rect = pygame.Rect(0, 0, FRAME_WIDTH, self.rect.height)

        new_frame_button_rect = pygame.Rect(0, 0, FRAME_WIDTH * 0.5, FRAME_WIDTH * 0.5)
        self.new_frame_button = Button(new_frame_button_rect, WHITE, "New")
        self.new_frame_button.events.on_clicked += self.add_new_frame

        self.content_width = new_frame_button_rect.width
        self.content_offset = 0

        self.events.on_timeline_frame_added += lambda tf: self.add_content_width(self.timeline_frame_rect.width + FRAME_PADDING)
        self.events.on_timeline_frame_added += lambda tf: self.set_active_timeline_frame_index(tf.index)
        self.events.on_timeline_frame_added += lambda tf: self.refresh_timeline_frames()

        self.events.on_timeline_frame_deleted += lambda tf: self.add_content_width(-(self.timeline_frame_rect.width + FRAME_PADDING))
        self.events.on_timeline_frame_deleted += lambda tf: self.handle_active_timeline_index_on_delete(tf.index)
        self.events.on_timeline_frame_deleted += lambda tf: self.refresh_timeline_frames()

    def init(self):
        self.add_new_frame()

    def add_new_frame(self):
        frame = Frame(ROWS, COLS, WHITE)
        timeline_frame = TimelineFrame(pygame.Rect(self.timeline_frame_rect), self, frame)

        timeline_frame.events.on_clicked += lambda tf: self.set_active_timeline_frame_index(tf.index)
        timeline_frame.left_button.events.on_clicked += lambda tf: self.swap_frames(tf, self.timeline_frames[tf.index - 1])
        timeline_frame.right_button.events.on_clicked += lambda tf: self.swap_frames(tf, self.timeline_frames[tf.index + 1])
        timeline_frame.delete_button.events.on_clicked += lambda tf: self.delete_frame(tf)

        self.timeline_frames.append(timeline_frame)

        self.events.on_timeline_frame_added(timeline_frame)

    def swap_frames(self, tf_a, tf_b):
        tf_a.frame, tf_b.frame = tf_b.frame, tf_a.frame

        if self.active_timeline_frame_index in (tf_a.index, tf_b.index):
            self.set_active_timeline_frame_index(tf_b.index)

    def delete_frame(self, delete_timeline_frame):
        # move the frame we want to delete into the last timeline frame
        # shuffle everything else down one frame to fill the space

        # For every frame from the next one to the last one
        for i in range(delete_timeline_frame.index + 1, len(self.timeline_frames)):
            previous_timeline_frame = self.timeline_frames[i - 1]
            next_timeline_frame = self.timeline_frames[i]

            previous_timeline_frame.frame, next_timeline_frame.frame = next_timeline_frame.frame, previous_timeline_frame.frame

        # Remove the last timeline frame
        self.timeline_frames = self.timeline_frames[:-1]

        # Fire event
        self.events.on_timeline_frame_deleted(delete_timeline_frame)

    def get_frames(self):
        return [tf.frame for tf in self.timeline_frames]

    def set_active_timeline_frame_index(self, timeline_frame_index):
        timeline_frame_index %= len(self.timeline_frames)
        self.active_timeline_frame_index = timeline_frame_index
        self.events.on_active_timeline_frame_index_changed(self.active_timeline_frame_index)

    def handle_active_timeline_index_on_delete(self, deleted_index):
        if self.active_timeline_frame_index == deleted_index:
            if deleted_index == len(self.timeline_frames):
                self.set_active_timeline_frame_index(self.active_timeline_frame_index - 1)
            else:
                self.set_active_timeline_frame_index(self.active_timeline_frame_index)
        elif self.active_timeline_frame_index > deleted_index:
            self.set_active_timeline_frame_index(self.active_timeline_frame_index - 1)

    def add_content_width(self, width):
        self.content_width += width
        self.events.on_content_width_changed(self.content_width)

    def set_content_offset(self, offset):
        self.content_offset = offset

    def refresh_timeline_frames(self):
        for timeline_frame in self.timeline_frames:
            timeline_frame.refresh()

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        local_pos = np.add(local_pos, (self.content_offset, 0))

        if self.new_frame_button.rect.collidepoint(local_pos):
            self.new_frame_button.events.on_clicked()
        else:
            for timeline_frame in self.timeline_frames:
                if timeline_frame.rect.collidepoint(local_pos):
                    timeline_frame.clicked(local_pos)

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
            timeline_frame_surface = timeline_frame.get_surface(i == self.active_timeline_frame_index)
            content_surface.blit(timeline_frame_surface, timeline_frame.rect)

        # Add new frame button
        i += 1
        self.new_frame_button.rect.topleft = (i * (FRAME_WIDTH + FRAME_PADDING), self.timeline_frame_rect.height / 2 - self.new_frame_button.rect.height / 2)
        new_frame_button_surface = self.new_frame_button.get_surface()
        content_surface.blit(new_frame_button_surface, self.new_frame_button.rect)

        timeline_surface.blit(content_surface, content_rect)
        return timeline_surface


class TimelineFrame(IClickable):
    def __init__(self, rect, timeline, frame):
        super().__init__(rect)

        self.timeline = timeline
        self.index = len(timeline.timeline_frames)
        self.frame = frame
        self.frame_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, rect.width - 2 * FRAME_PADDING, rect.width - 2 * FRAME_PADDING)

        button_rect = pygame.Rect(0, 0, (self.frame_rect.width - FRAME_PADDING) / 2, (rect.height - self.frame_rect.height - 4 * FRAME_PADDING) / 2)
        left_button_rect = pygame.Rect.move(button_rect, self.frame_rect.left, self.frame_rect.bottom + FRAME_PADDING)
        right_button_rect = pygame.Rect.move(left_button_rect, left_button_rect.width + FRAME_PADDING, 0)

        self.left_button = Button(left_button_rect, WHITE, "<", BLACK, WHITE)
        self.right_button = Button(right_button_rect, WHITE, ">", BLACK, WHITE)

        delete_button_rect = pygame.Rect(self.frame_rect.left, left_button_rect.bottom + FRAME_PADDING, self.frame_rect.width, rect.height - self.frame_rect.height - button_rect.height - 4 * FRAME_PADDING)
        self.delete_button = Button(delete_button_rect, WHITE, "DELETE", RED, RED)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.left_button.enabled and self.left_button.rect.collidepoint(local_pos):
            self.left_button.events.on_clicked(self)
            return

        if self.right_button.enabled and self.right_button.rect.collidepoint(local_pos):
            self.right_button.events.on_clicked(self)
            return

        if self.delete_button.enabled and self.delete_button.rect.collidepoint(local_pos):
            self.delete_button.events.on_clicked(self)
            return

        self.events.on_clicked(self)

    def refresh(self):
        first_index = 0
        last_index = first_index + len(self.timeline.timeline_frames) - 1

        self.left_button.enabled = self.index != first_index
        self.right_button.enabled = self.index != last_index
        self.delete_button.enabled = first_index != last_index

    def get_surface(self, is_active_frame):

        timeline_frame_surface = pygame.Surface(self.rect.size)
        timeline_frame_surface.fill(BLACK)

        frame_surface = self.frame.get_surface(self.frame_rect, 1)
        timeline_frame_surface.blit(frame_surface, self.frame_rect)

        if self.left_button.enabled:
            left_button_surface = self.left_button.get_surface()
            timeline_frame_surface.blit(left_button_surface, self.left_button.rect)

        if self.right_button.enabled:
            right_button_surface = self.right_button.get_surface()
            timeline_frame_surface.blit(right_button_surface, self.right_button.rect)

        if self.delete_button.enabled:
            delete_button_surface = self.delete_button.get_surface()
            timeline_frame_surface.blit(delete_button_surface, self.delete_button.rect)

        if is_active_frame:
            pygame.draw.rect(timeline_frame_surface, RED, (0, 0, *self.rect.size), 5)

        return timeline_frame_surface


class TimelineEvents(Events):
    __events__ = ('on_active_timeline_frame_index_changed', 'on_timeline_frame_added', 'on_timeline_frame_deleted', 'on_content_width_changed')
