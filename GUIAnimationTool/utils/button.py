from .settings import *


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.button_events = ButtonEvents()

    def draw(self, win):
        # Square of Color
        pygame.draw.rect(win, self.color, (
            self.x, self.y,
            self.width, self.height
        ))

        if self.text:
            # Outline
            pygame.draw.rect(win, BLACK, (
                self.x, self.y,
                self.width, self.height
            ), 2)

            # Button Text
            button_font = get_font(22)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (
                self.x + self.width / 2 - text_surface.get_width() / 2,
                self.y + self.height / 2 - text_surface.get_height() / 2
            ))

    def is_mouse_over(self, pos):
        x, y = pos
        pixel = Vector2(x, y)

        if pixel.x < self.x or pixel.x >= self.x + self.width:
            return False

        if pixel.y < self.y or pixel.y >= self.y + self.height:
            return False

        return True


class ButtonEvents(Events):
    __events__ = 'on_clicked'
