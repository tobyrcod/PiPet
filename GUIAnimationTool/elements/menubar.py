from utils import *


class MenuBar:
    def __init__(self, rect):
        self.rect = rect

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        file_name = prompt_open_file()
        print(file_name)

    def get_surface(self):

        preview_surface = pygame.Surface(self.rect.size)

        preview_surface.fill(BLACK)

        return preview_surface
