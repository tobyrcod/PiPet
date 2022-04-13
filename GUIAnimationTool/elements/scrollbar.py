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

        print(self.scroll_block.rect.left)

    def set_content_width(self, width):
        self.content_width = width
        print(f'viewport width: {self.viewport_width}, content width: {self.content_width}')

        self.scroll_block.update_width(self.viewport_width, self.content_width)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.scroll_block.rect.collidepoint(local_pos):
            self.scroll_block.clicked(local_pos)

    def held(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.scroll_block.rect.collidepoint(local_pos):
            self.scroll_block.held(local_pos)

    def get_surface(self):

        scrollbar_surface = pygame.Surface(self.rect.size)
        scrollbar_surface.fill(BLACK)

        pygame.draw.rect(scrollbar_surface, WHITE, (SCROLL_PADDING, SCROLL_PADDING, self.scroll_block.max_width, self.scroll_block.rect.height))

        scroll_block_surface = self.scroll_block.get_surface()
        scrollbar_surface.blit(scroll_block_surface, self.scroll_block.rect)

        return scrollbar_surface


class ScrollBlock(IDraggable):
    def __init__(self, rect, max_width):
        super().__init__(rect)

        self.max_width = max_width
        self.initial_hold_mouse_position = None
        self.initial_scroll_block_position = None

    def update_width(self, viewport_width, content_width):
        if viewport_width >= content_width:
            self.rect.width = self.max_width
        else:
            self.rect.width = self.max_width * (viewport_width / content_width)

    def set_rect_pos(self, new_rect_pos):
        new_rect_pos = clamp(new_rect_pos, SCROLL_PADDING, SCROLL_PADDING + self.max_width - self.rect.width)
        self.rect.left = new_rect_pos

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        self.initial_hold_mouse_position = local_pos
        self.initial_scroll_block_position = self.rect.topleft

    def held(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.initial_hold_mouse_position is not None:
            mouse_delta_x, _ = np.subtract(local_pos, self.initial_hold_mouse_position)
            new_rect_pos = self.rect.left + mouse_delta_x
            self.set_rect_pos(new_rect_pos)

    def get_surface(self):
        scroll_block_surface = pygame.Surface(self.rect.size)
        scroll_block_surface.fill(BLUE)
        return scroll_block_surface
