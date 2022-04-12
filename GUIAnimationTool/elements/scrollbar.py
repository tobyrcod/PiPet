from utils import *
from interfaces import IClickable


class Scrollbar:
    def __init__(self, rect):
        self.rect = rect

        max_width, height = np.subtract(self.rect.size, (2 * SCROLL_PADDING, 2 * SCROLL_PADDING))
        scroll_block_rect = pygame.Rect(SCROLL_PADDING, SCROLL_PADDING, max_width, height)
        self.scroll_block = ScrollBlock(scroll_block_rect)

    def get_surface(self):

        scrollbar_surface = pygame.Surface(self.rect.size)
        scrollbar_surface.fill(BLACK)

        scroll_block_surface = self.scroll_block.get_surface()
        scrollbar_surface.blit(scroll_block_surface, self.scroll_block.rect)

        return scrollbar_surface


class ScrollBlock:
    def __init__(self, rect):
        self.rect = rect
        self.events = ScrollbarEvents()

    def get_surface(self):
        scroll_block_surface = pygame.Surface(self.rect.size)
        scroll_block_surface.fill(WHITE)
        return scroll_block_surface


class ScrollbarEvents(Events):
    __events__ = ('on_clicked', 'on_drag')
