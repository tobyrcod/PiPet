import pygame

import main


# TODO: Make scenes use their own surface which is then returned and blit to the main window
# TODO: Split States into their own files
# TODO: Add a draw method the the base update method in the State class and call it at the end of the polymorphised method
class State:
    def __init__(self, fsm):
        self.fsm = fsm

    def EnterState(self):
        pass

    def Update(self, win, keys):
        pass

    def ExitState(self):
        pass


class StateA(State):
    def __init__(self, fsm):
        super().__init__(fsm)

    def EnterState(self):
        super().EnterState()
        print("Entering State A")

    def Update(self, win, keys):
        super().Update(win, keys)

        win.fill(main.BLACK)
        scene_text = main.COMIC_SANS.render("A", True, main.WHITE)
        win.blit(scene_text,  (main.WIDTH // 2 - scene_text.get_width() // 2, main.HEIGHT // 2 - scene_text.get_height() // 2))
        pygame.display.update()

        if keys[pygame.K_b]:
            self.fsm.SetState(StateB(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State A")


class StateB(State):
    def EnterState(self):
        super().EnterState()
        print("Entering State B")

    def Update(self, win, keys):
        super().Update(win, keys)

        win.fill(main.WHITE)
        scene_text = main.COMIC_SANS.render("B", True, main.BLACK)
        win.blit(scene_text,
                 (main.WIDTH // 2 - scene_text.get_width() // 2, main.HEIGHT // 2 - scene_text.get_height() // 2))
        pygame.display.update()

        if keys[pygame.K_a]:
            self.fsm.SetState(StateA(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State B")


class FSM:
    current_state = None

    def __init__(self):
        pass

    def SetState(self, new_state: State):
        if self.current_state is not None:
            self.current_state.ExitState()

        self.current_state = new_state
        self.current_state.EnterState()

    def Update(self, win, keys):
        self.current_state.Update(win, keys)
