from utils import *
from .frame import Frame
from interfaces import IClickable


class Animator:
    def __init__(self, rect):
        self.rect = rect
        self.frames = []
        self.events = AnimatorEvents()

        self.animator_frame_rect = pygame.Rect(0, 0, FRAME_WIDTH, (self.rect.height - 3 * FRAME_PADDING) * 0.8)
        self.animator_frames = []
        self.active_frame_index = -1

        new_frame_button_rect = pygame.Rect(0, 0, FRAME_WIDTH * 0.7, FRAME_WIDTH * 0.7)
        self.new_frame_button = Button(new_frame_button_rect, WHITE, "New")
        self.new_frame_button.events.on_clicked += self.add_new_frame

    def init(self):
        self.add_new_frame()

    def add_new_frame(self):
        frame = Frame(ROWS, COLS, WHITE)
        self.frames.append(frame)

        animator_frame = AnimatorFrame(self.animator_frame_rect, frame)
        self.animator_frames.append(animator_frame)

        self.set_active_frame_index(len(self.frames) - 1)

    def set_active_frame_index(self, index):
        self.active_frame_index = index
        self.events.on_active_frame_index_changed(self.active_frame_index)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.new_frame_button.rect.collidepoint(local_pos):
            self.new_frame_button.events.on_clicked()

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)

        # Background
        animator_surface.fill(WHITE)

        # All the frames
        i = -1
        for i, animator_frame in enumerate(self.animator_frames):
            animator_frame.rect.topleft = (FRAME_PADDING + i * (FRAME_WIDTH + FRAME_PADDING), FRAME_PADDING)

            animator_frame_surface = animator_frame.get_surface(i == self.active_frame_index)
            animator_surface.blit(animator_frame_surface, animator_frame.rect)

        # Add new frame button
        i += 1
        self.new_frame_button.rect.topleft = (FRAME_PADDING + i * (FRAME_WIDTH + FRAME_PADDING), FRAME_PADDING + self.animator_frame_rect.height / 2 - self.new_frame_button.rect.height / 2)
        new_frame_button_surface = self.new_frame_button.get_surface()
        animator_surface.blit(new_frame_button_surface, self.new_frame_button.rect)

        # Text to say which element this is
        font = get_font(size=30)
        text_surface = font.render("Animator", 1, BLACK)
        animator_surface.blit(text_surface, (
            0,
            self.rect.height - text_surface.get_height()
        ))

        return animator_surface


class AnimatorFrame(IClickable):
    def __init__(self, rect, frame):
        super().__init__(rect)

        self.frame = frame
        self.frame_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, rect.width - 2 * FRAME_PADDING, rect.width - 2 * FRAME_PADDING)

    def get_surface(self, is_active_frame):

        animator_frame_surface = pygame.Surface(self.rect.size)

        animator_frame_surface.fill(BLACK)

        frame_surface = self.frame.get_surface(self.frame_rect)
        animator_frame_surface.blit(frame_surface, self.frame_rect)

        if is_active_frame:
            pygame.draw.rect(animator_frame_surface, RED, (0, 0, *self.rect.size), 5)

        return animator_frame_surface


class AnimatorEvents(Events):
    __events__ = 'on_active_frame_index_changed'
