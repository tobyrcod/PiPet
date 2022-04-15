from utils import *


class MenuBar:
    def __init__(self, rect, timeline):
        self.rect = rect
        self.timeline = timeline

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        self.save_timeline()

    def save_timeline():
        file = prompt_save_file()

        if file is not None:
            frames = self.timeline.get_frames()
            grids = [frame.grid for frame in frames]

            file.write(json.dumps(grids, indent=4))
            print("Animation Saved!")
            return
        
        print("Failed to save animation")

    def get_surface(self):

        preview_surface = pygame.Surface(self.rect.size)

        preview_surface.fill(BLACK)

        return preview_surface
