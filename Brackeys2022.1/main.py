from settings import *
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PiPet")

from fsm import FSM
from statea import StateA


def main():
    STATE_MACHINE = FSM()
    STATE_MACHINE.SetState(StateA(STATE_MACHINE))

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        STATE_MACHINE.Update(WIN, keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


# Only runs main() if this file is being run directly,
# ie. not being imported as a module
if __name__ == '__main__':
    main()
