# Based on 'Make Paint in Python'
# https://www.youtube.com/watch?v=N20eXcfyQ_4
from utils import *
from elements import *
# TODO: Change application icon

# Pygame variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PiPet Animation Maker")
clock = pygame.time.Clock()


# Main game Loop
def main():

    canvas = Canvas(pygame.Rect(0, 0, WIDTH, WIDTH))
    toolbar = Toolbar(pygame.Rect(0, WIDTH, WIDTH, TOOLBAR_HEIGHT))

    for button in toolbar.buttons:
        button.button_events.on_clicked += canvas.change_draw_color

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # if the left mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if canvas.rect.collidepoint(mouse_pos):
                    canvas.clicked(mouse_pos)
                elif toolbar.rect.collidepoint(mouse_pos):
                    toolbar.clicked(mouse_pos)

        draw(WIN, canvas, toolbar)

    pygame.quit()


# TODO: Draw the grid to a different canvas instead of directly to the main display TODO?: Instead of redrawing the
#  whole grid just redraw the pixels (if any) that change this frame. '?' because this is just for optimisation,
#  and realistically that doesn't matter at all for this simple use case
def draw(win, canvas, toolbar):

    win.fill(BG_COLOR)

    canvas_surface = canvas.get_surface()
    win.blit(canvas_surface, canvas.rect)

    toolbar_surface = toolbar.get_surface()
    win.blit(toolbar_surface, toolbar.rect)

    pygame.display.update()


# Only run if this file is loaded directly (not through a module import)
if __name__ == "__main__":
    main()
