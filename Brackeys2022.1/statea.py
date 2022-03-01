import pygame
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

        if keys[pygame.K_b]:
            self.fsm.SetState(stateb.StateB(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State A")
