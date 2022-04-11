from utils import *


class Animator:
    def __init__(self, rect):
        self.rect = rect

    def get_surface(self):

        animator_surface = pygame.Surface(self.rect.size)

        animator_surface.fill(WHITE)

        font = get_font(size=30)
        text_surface = font.render("Animator", 1, BLACK)
        animator_surface.blit(text_surface, (
            0,
            self.rect.height - text_surface.get_height()
        ))

        return animator_surface
