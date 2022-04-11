from utils import *


class Frame:
    def __init__(self, rect):
        self.rect = rect

    def get_surface(self):

        frame_surface = pygame.Surface(self.rect.size)

        frame_surface.fill(BLACK)

        return frame_surface
