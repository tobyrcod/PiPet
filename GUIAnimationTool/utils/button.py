from .settings import *
from .helper_methods import *
from interfaces import IClickable


class Button(IClickable):
    def __init__(self, rect, color, text=None, text_color=BLACK, border_color=BLACK):
        super().__init__(rect)

        self.color = color
        self.text = text
        self.text_color = text_color
        self.border_color = border_color
        self.enabled = True

    def get_surface(self, is_active=False):
        button_surface = pygame.Surface(self.rect.size)
        # Square of Color
        button_surface.fill(self.color)

        if self.text:
            # Border
            border_color = RED if is_active else self.border_color
            pygame.draw.rect(button_surface, border_color, (0, 0, *self.rect.size), 3)

            # Button Text
            button_font = get_font(size=22)
            text_surface = button_font.render(self.text, 1, self.text_color)
            button_surface.blit(text_surface, (
                self.rect.width / 2 - text_surface.get_width() / 2,
                self.rect.height / 2 - text_surface.get_height() / 2
            ))
        else:
            if is_active:
                pygame.draw.rect(button_surface, BLACK, (0, 0, *self.rect.size), 2)
                pygame.draw.rect(button_surface, WHITE, (2, 2, self.rect.width - 4, self.rect.height - 4), 2)
        return button_surface

