from settings import *
import statea
import pong
import snake
from state import State


class StateB(State):
    def __init__(self, fsm):
        super().__init__(fsm)

    def EnterState(self):
        super().EnterState()
        print("Entering State B")

    def Update(self, win, keys):
        super().Update(win, keys)

        if keys[pygame.K_a]:
            self.fsm.SetState(statea.StateA(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State B")
