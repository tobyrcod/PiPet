from utils import *


class Preview:
    def __init__(self, rect):
        self.rect = rect

    def get_surface(self):

        preview_surface = pygame.Surface(self.rect.size)

        preview_surface.fill(BLACK)

        font = get_font(size=60)
        text_surface = font.render("Preview", 1, WHITE)
        preview_surface.blit(text_surface, (
            self.rect.width / 2 - text_surface.get_width() / 2,
            self.rect.height / 2 - text_surface.get_height() / 2
        ))

        return preview_surface
