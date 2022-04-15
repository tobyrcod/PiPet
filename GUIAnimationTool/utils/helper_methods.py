from .settings import *
from pygame_textinput import TextInputVisualizer, TextInputManager


def get_font(size):
    return pygame.font.SysFont(FONT_NAME, size)


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def create_text_input(font_size, font_color, manager):
    text_input_font = get_font(font_size)

    textinput_custom = TextInputVisualizer(
        manager=manager,
        font_object=text_input_font,
        cursor_width=4,
        cursor_color=GREY,
        cursor_blink_interval=400,
        antialias=True,
        font_color=font_color
    )

    return textinput_custom
