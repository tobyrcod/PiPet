from utils import *
from interfaces import IDraggable


class Scrollbar:
    def __init__(self, rect, viewport_width, content_width):
        self.rect = rect

        self.content_width = content_width
        self.viewport_width = viewport_width

        max_width, height = np.subtract(self.rect.size, (2 * SCROLL_PADDING, 2 * SCROLL_PADDING))
        scroll_block_rect = pygame.Rect(SCROLL_PADDING, SCROLL_PADDING, max_width, height)
        self.scroll_block = ScrollBlock(scroll_block_rect, max_width)

    def set_content_width(self, width):
        self.content_width = width
        print(f'viewport width: {self.viewport_width}, content width: {self.content_width}')

        self.scroll_block.update_width(self.viewport_width, self.content_width)

    def get_surface(self):

        scrollbar_surface = pygame.Surface(self.rect.size)
        scrollbar_surface.fill(BLACK)

        scroll_block_surface = self.scroll_block.get_surface()
        scrollbar_surface.blit(scroll_block_surface, self.scroll_block.rect)

        return scrollbar_surface


class ScrollBlock(IDraggable):
    def __init__(self, rect, max_width):
        super().__init__(rect)

        self.max_width = max_width

    def update_width(self, viewport_width, content_width):
        if viewport_width >= content_width:
            self.rect.width = self.max_width
        else:
            self.rect.width = self.max_width / 2

    def get_surface(self):
        scroll_block_surface = pygame.Surface(self.rect.size)
        scroll_block_surface.fill(WHITE)
        return scroll_block_surface
