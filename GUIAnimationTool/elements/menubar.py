from utils import *


class MenuBar:
    def __init__(self, rect, timeline, preview):
        self.rect = rect
        self.timeline = timeline
        self.preview = preview

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        self.save_timeline()

    def save_timeline(self):
        file, filename = prompt_save_file()

        if file is not None:
            frames = self.timeline.get_frames()
            grids = [frame.grid for frame in frames]

            save_json = {
                "name": filename,
                "delay": 1 / self.preview.fps,
                "faces": grids
            }

            file.write(json.dumps(save_json, indent=4))
            print("Animation Saved!")
            return
        
        print("Failed to save animation")

    def get_surface(self):

        preview_surface = pygame.Surface(self.rect.size)

        preview_surface.fill(BLACK)

        return preview_surface
