from utils import *


# TODO?: Add a Floodfill button. '?' because we probably dont need one but its cool
# TODO?: Add an Undo button. '?' because we probably dont need one but its cool
class Toolbar:
    def __init__(self, rect):
        self.rect = rect
        colors = [BLACK, RED, BLUE, GREEN]

        padding_count = TOOLBAR_COLUMNS + 1
        padded_space = TOOLBAR_PADDING * padding_count
        button_space = self.rect.width - padded_space
        button_width = button_height = button_space // TOOLBAR_COLUMNS
        self.color_buttons = []
        for i, color in enumerate(colors):
            button = Button(pygame.Rect(TOOLBAR_PADDING + (i % TOOLBAR_COLUMNS) * (TOOLBAR_PADDING + button_width),
                                        TOOLBAR_PADDING + (i // TOOLBAR_COLUMNS) * (TOOLBAR_PADDING + button_height),
                                        button_width, button_height), color)
            self.color_buttons.append(button)
        self.active_color_button = self.color_buttons[0]

        self.brush_buttons = {}
        for i, name in enumerate(["Brush", "Fill", "Erase"]):
            button = Button(pygame.Rect(TOOLBAR_PADDING + (i % TOOLBAR_COLUMNS) * (TOOLBAR_PADDING + button_width),
                                        (self.rect.height - TOOLBAR_PADDING - button_height) - (
                                            (i // TOOLBAR_COLUMNS) + 1) * (TOOLBAR_PADDING + button_height),
                                        button_width, button_height), WHITE, name, BLACK)
            self.brush_buttons[name] = button
        self.active_brush_button = self.brush_buttons["Brush"]

        self.other_buttons = {}
        for i, name in enumerate(["Clear"]):
            button = Button(pygame.Rect(TOOLBAR_PADDING + (i % TOOLBAR_COLUMNS) * (TOOLBAR_PADDING + button_width),
                                        (self.rect.height - TOOLBAR_PADDING - button_height) - (
                                                i // TOOLBAR_COLUMNS) * (TOOLBAR_PADDING + button_height),
                                        button_width, button_height), WHITE, name, BLACK)
            self.other_buttons[name] = button
        self.buttons = self.color_buttons + list(self.brush_buttons.values()) + list((self.other_buttons.values()))

    def set_active_color_button(self, button):
        self.active_color_button = button
        print(self.active_color_button)

    def set_active_brush_button(self, button):
        self.active_brush_button = button

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        for button in self.buttons:
            if not button.rect.collidepoint(local_pos):
                continue

            # If we clicked on this button
            button.events.on_clicked(button)

    def get_surface(self):

        toolbar_surface = pygame.Surface(self.rect.size)

        toolbar_surface.fill(WHITE)

        for button in self.color_buttons:
            button_surface = button.get_surface(button == self.active_color_button)
            toolbar_surface.blit(button_surface, button.rect)

        for button in self.brush_buttons.values():
            button_surface = button.get_surface(button == self.active_brush_button)
            toolbar_surface.blit(button_surface, button.rect)

        for button in self.other_buttons.values():
            button_surface = button.get_surface()
            toolbar_surface.blit(button_surface, button.rect)

        return toolbar_surface
