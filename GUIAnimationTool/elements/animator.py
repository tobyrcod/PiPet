from utils import *


class Animator:
    def __init__(self, rect):
        self.rect = rect

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)

        animator_surface.fill(BLACK)

        font = get_font(size=60)
        text_surface = font.render("Animator", 1, WHITE)
        animator_surface.blit(text_surface, (
            self.rect.width / 2 - text_surface.get_width() / 2,
            self.rect.height / 2 - text_surface.get_height() / 2
        ))

        return animator_surface
