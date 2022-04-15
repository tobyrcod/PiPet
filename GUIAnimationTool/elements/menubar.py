from utils import *


class MenuBar:
    def __init__(self, rect, color, text_color, timeline, preview):
        self.rect = rect
        self.color = color
        self.timeline = timeline
        self.preview = preview

        button_rect = pygame.Rect(0, 0, rect.width / 2, rect.height)
        self.load_button = Button(pygame.Rect(button_rect), color, 'Load', text_color, color)
        button_rect.bottomleft = self.load_button.rect.bottomright
        self.save_button = Button(pygame.Rect(button_rect), color, 'Save', text_color, color)

        self.load_button.events.on_clicked += lambda b: self.load_timeline()
        self.save_button.events.on_clicked += lambda b: self.save_timeline()

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)
        
        for button in [self.load_button, self.save_button]:
            if button.rect.collidepoint(local_pos):
                button.events.on_clicked(button)
                return

    def load_timeline(self):
        print('load')

    def save_timeline(self):
        print('st')
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

        load_button_surface = self.load_button.get_surface()
        preview_surface.blit(load_button_surface, self.load_button.rect)

        save_button_surface = self.save_button.get_surface()
        preview_surface.blit(save_button_surface, self.save_button.rect)

        return preview_surface
