import pygame
import settings
import stateb
from state import State


class StateA(State):
    def __init__(self, fsm):
        super().__init__(fsm)

    def EnterState(self):
        super().EnterState()
        print("Entering State A")

    def Update(self, win, keys):
        super().Update(win, keys)

        win.fill(settings.BLACK)
        scene_text = settings.COMIC_SANS.render("A", True, settings.WHITE)
        win.blit(scene_text,  (settings.WIDTH // 2 - scene_text.get_width() // 2, settings.HEIGHT // 2 - scene_text.get_height() // 2))
        pygame.display.update()

        if keys[pygame.K_b]:
            self.fsm.SetState(stateb.StateB(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State A")
