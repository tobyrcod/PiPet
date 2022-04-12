from utils import *
from .frame import Frame


class Animator:
    def __init__(self, rect):
        self.rect = rect
        self.frames = []
        self.add_new_frame()
        self.active_frame_index = 0

        new_frame_button_rect = pygame.Rect(0, 0, FRAME_WIDTH * 0.7, FRAME_WIDTH * 0.7)
        self.new_frame_button = Button(new_frame_button_rect, WHITE, "New")
        self.new_frame_button.button_events.on_clicked += self.add_new_frame

    def make_new_frame(self):
        frame = Frame(ROWS, COLS, WHITE)
        return frame

    def add_new_frame(self):
        frame = self.make_new_frame()
        self.frames.append(frame)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.new_frame_button.rect.collidepoint(local_pos):
            self.new_frame_button.button_events.on_clicked()

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)

        # Background
        animator_surface.fill(WHITE)

        # All the frames
        i = 0
        animator_frame_rect = pygame.Rect(0, 0, FRAME_WIDTH, (self.rect.height - 3 * FRAME_PADDING) * 0.8)
        for i, frame in enumerate(self.frames):
            animator_frame_rect.topleft = (FRAME_PADDING + i * (FRAME_WIDTH + FRAME_PADDING), FRAME_PADDING)
            animator_frame = AnimatorFrame(frame, animator_frame_rect)

            animator_frame_surface = animator_frame.get_surface()
            animator_surface.blit(animator_frame_surface, animator_frame_rect)

        # Add new frame button
        i += 1
        self.new_frame_button.rect.topleft = (FRAME_PADDING + i * (FRAME_WIDTH + FRAME_PADDING), FRAME_PADDING + animator_frame_rect.height / 2 - self.new_frame_button.rect.height / 2)
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


class AnimatorFrame:
    def __init__(self, frame, rect):
        self.frame = frame
        self.rect = rect
        self.frame_rect = pygame.Rect(FRAME_PADDING, FRAME_PADDING, rect.width - 2 * FRAME_PADDING, rect.width - 2 * FRAME_PADDING)

    def get_surface(self):

        animator_frame_surface = pygame.Surface(self.rect.size)

        animator_frame_surface.fill(BLACK)

        frame_surface = self.frame.get_surface(self.frame_rect)
        animator_frame_surface.blit(frame_surface, self.frame_rect)

        return animator_frame_surface
