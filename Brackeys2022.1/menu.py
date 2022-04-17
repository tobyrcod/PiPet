import pygame
import snake
import sys
from state import State


class MainMenu(State):  #main menu is a state
    def __init__(self, fsm):
        super().__init__(fsm)

    def EnterState(self):
        super().EnterState()
        print("Entering State A")

    def Update(self, win, keys):
        super().Update(win, keys)

        if keys[pygame.K_b]:
            self.fsm.SetState(snake.StateSnake(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting State A")


    #create the menu interface here

pygame.init()
res = (720, 720)

screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

font = pygame.font.SysFont('Corbel', 25)



w = (255, 255, 255)
b = (0, 0, 0)
r = (255, 0, 0)