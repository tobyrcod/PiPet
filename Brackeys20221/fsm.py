from state import State


# TODO: Make scenes use their own surface which is then returned and blit to the main window
# TODO: Split States into their own files
# TODO: Add a draw method the the base update method in the State class and call it at the end of the polymorphised methodc


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
