from utils import *


class Toolbar:
    def __init__(self, rect):
        self.rect = rect
        button_y = TOOLBAR_HEIGHT / 2 - 25
        self.buttons = [
            Button(pygame.Rect(10, button_y, 50, 50), BLACK),
            Button(pygame.Rect(70, button_y, 50, 50), RED),
            Button(pygame.Rect(130, button_y, 50, 50), GREEN),
            Button(pygame.Rect(190, button_y, 50, 50), BLUE),
            Button(pygame.Rect(250, button_y, 50, 50), WHITE, "Erase", BLACK),
            Button(pygame.Rect(310, button_y, 50, 50), WHITE, "Reset", BLACK),
        ]

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        for button in self.buttons:
            if not button.rect.collidepoint(local_pos):
                continue

            # If we clicked on this button
            button.button_events.on_clicked(button)

    def get_surface(self):

        toolbar_surface = pygame.Surface(self.rect.size)

        toolbar_surface.fill(WHITE)

        for button in self.buttons:
            button_surface = button.get_surface()
            toolbar_surface.blit(button_surface, button.rect)

        return toolbar_surface