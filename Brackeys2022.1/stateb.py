import pygame
import settings
import statea
import pong
from state import State


class StateB(State):
    def EnterState(self):
        super().EnterState()
        print("Entering State B")

    def Update(self, win, keys):
        super().Update(win, keys)

        win.fill(settings.WHITE)
        scene_text = settings.COMIC_SANS.render("B", True, settings.BLACK)
        win.blit(scene_text,
                 (settings.WIDTH // 2 - scene_text.get_width() // 2, settings.HEIGHT // 2 - scene_text.get_height() // 2))
        pygame.display.update()

        if keys[pygame.K_a]:
            self.fsm.SetState(statea.StateA(self.fsm))

        if keys[pygame.K_c]:
            self.fsm.SetState(pong.StateC(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State B")