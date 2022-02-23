import pygame
import settings
from state import State
import stateb


class StateC(State):
    def EnterState(self):
        super().EnterState()
        print("Entering State C")

    def Update(self, win, keys):
        super().Update(win, keys)

        win.fill(settings.BLACK)
        scene_text = settings.COMIC_SANS.render("C", True, settings.WHITE)
        win.blit(scene_text,
                 (settings.WIDTH // 2 - scene_text.get_width() // 2, settings.HEIGHT // 2 - scene_text.get_height() // 2))
        pygame.display.update()

        if keys[pygame.K_b]:
            self.fsm.SetState(stateb.StateB(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State C")
