from .settings import *


class Button:
    def __init__(self, rect, color, text=None, text_color=BLACK):
        self.rect = rect
        self.color = color
        self.text = text
        self.text_color = text_color
        self.button_events = ButtonEvents()

    def get_surface(self):
        button_surface = pygame.Surface(self.rect.size)
        # Square of Color
        button_surface.fill(self.color)

        if self.text:
            # Outline
            pygame.draw.rect(button_surface, BLACK, (0, 0, *self.rect.size), 3)

            # Button Text
            button_font = get_font(size=22)
            text_surface = button_font.render(self.text, 1, self.text_color)
            button_surface.blit(text_surface, (
                self.rect.width / 2 - text_surface.get_width() / 2,
                self.rect.height / 2 - text_surface.get_height() / 2
            ))

        return button_surface


class ButtonEvents(Events):
    __events__ = 'on_clicked'
