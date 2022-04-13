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

        new_frame_button_rect = pygame.Rect(0, 0, FRAME_WIDTH * 0.7, FRAME_WIDTH * 0.7)
        self.new_frame_button = Button(new_frame_button_rect, WHITE, "New")
        self.new_frame_button.events.on_clicked += self.add_new_frame

        self.content_width = new_frame_button_rect.width
        self.content_offset = 0

        self.events.on_timeline_frame_added += lambda tf: self.add_content_width(self.timeline_frame_rect.width + FRAME_PADDING)
        self.events.on_timeline_frame_added += lambda tf: self.set_active_timeline_frame_index(tf.timeline_frame_index)
        self.events.on_timeline_frame_added += lambda tf: self.refresh_timeline_frames()

    def init(self):
        self.add_new_frame()

    def add_new_frame(self):
        frame = Frame(ROWS, COLS, WHITE)
        timeline_frame = TimelineFrame(pygame.Rect(self.timeline_frame_rect), self, frame)

        timeline_frame.events.on_clicked += lambda a: self.set_active_timeline_frame_index(a.timeline_frame_index)
        timeline_frame.left_button.events.on_clicked += lambda tf: self.swap_frames(tf, self.timeline_frames[tf.timeline_frame_index - 1])
        timeline_frame.right_button.events.on_clicked += lambda tf: self.swap_frames(tf, self.timeline_frames[tf.timeline_frame_index + 1])

        self.timeline_frames.append(timeline_frame)

        self.events.on_timeline_frame_added(timeline_frame)

    def swap_frames(self, tf_a, tf_b):
        tf_a.frame, tf_b.frame = tf_b.frame, tf_a.frame

        if self.active_timeline_frame_index in (tf_a.timeline_frame_index, tf_b.timeline_frame_index):
            self.set_active_timeline_frame_index(tf_b.timeline_frame_index)

    def set_active_timeline_frame_index(self, timeline_frame_index):
        timeline_frame_index %= len(self.timeline_frames)
        self.active_timeline_frame_index = timeline_frame_index
        self.events.on_active_timeline_frame_index_changed(self.active_timeline_frame_index)

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
        self.timeline_frame_index = len(timeline.timeline_frames)
        self.frame = frame
        self.frame_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, rect.width - 2 * FRAME_PADDING, rect.width - 2 * FRAME_PADDING)

        button_rect = pygame.Rect(0, 0, (self.frame_rect.width - FRAME_PADDING) / 2, rect.height - self.frame_rect.height - 3 * FRAME_PADDING)
        left_button_rect = pygame.Rect.move(button_rect, self.frame_rect.left, self.frame_rect.bottom + FRAME_PADDING)
        right_button_rect = pygame.Rect.move(left_button_rect, left_button_rect.width + FRAME_PADDING, 0)

        self.left_button = Button(left_button_rect, WHITE, "<", BLACK, WHITE)
        self.right_button = Button(right_button_rect, WHITE, ">", BLACK, WHITE)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.left_button.enabled and self.left_button.rect.collidepoint(local_pos):
            self.left_button.events.on_clicked(self)
            return

        if self.right_button.enabled and self.right_button.rect.collidepoint(local_pos):
            self.right_button.events.on_clicked(self)
            return

        self.events.on_clicked(self)

    def refresh(self):
        first_index = 0
        last_index = first_index + len(self.timeline.timeline_frames) - 1

        self.left_button.enabled = self.timeline_frame_index != first_index
        self.right_button.enabled = self.timeline_frame_index != last_index

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

        if is_active_frame:
            pygame.draw.rect(timeline_frame_surface, RED, (0, 0, *self.rect.size), 5)

        return timeline_frame_surface


class TimelineEvents(Events):
    __events__ = ('on_active_timeline_frame_index_changed', 'on_timeline_frame_added', 'on_content_width_changed')
