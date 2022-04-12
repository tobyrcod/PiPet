# Based on 'Make Paint in Python'
# https://www.youtube.com/watch?v=N20eXcfyQ_4
import pygame

from utils import *
from elements import *

# TODO: Change application icon

# Pygame variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PiPet Animation Maker")
clock = pygame.time.Clock()


# Main game Loop
def main():
    def change_canvas_draw_color(button):
        canvas.change_draw_color(button.color)

    def reset_canvas(button):
        canvas.clear()

    animator = Animator(pygame.Rect(PADDING, 2 * PADDING + CANVAS_HEIGHT, ANIMATOR_WIDTH, ANIMATOR_HEIGHT))
    canvas = Canvas(pygame.Rect(PADDING, PADDING, CANVAS_WIDTH, CANVAS_HEIGHT), animator.frames[0])
    toolbar = Toolbar(pygame.Rect(2 * PADDING + CANVAS_WIDTH, PADDING, TOOLBAR_WIDTH, TOOLBAR_HEIGHT))
    preview = Preview(pygame.Rect(2 * PADDING + CANVAS_WIDTH, 2 * PADDING + CANVAS_HEIGHT, PREVIEW_WIDTH, PREVIEW_HEIGHT))

    for button in toolbar.color_buttons:
        button.button_events.on_clicked += change_canvas_draw_color

    toolbar.other_buttons['Erase'].button_events.on_clicked += change_canvas_draw_color
    toolbar.other_buttons['Clear'].button_events.on_clicked += reset_canvas

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # TODO: make this more elegant (...matrix?)
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # if the left mouse button is clicked
                if toolbar.rect.collidepoint(mouse_pos):
                    toolbar.clicked(mouse_pos)
                elif canvas.rect.collidepoint(mouse_pos):
                    canvas.clicked(mouse_pos)
                elif animator.rect.collidepoint(mouse_pos):
                    animator.clicked(mouse_pos)
            elif pygame.mouse.get_pressed()[0]:  # if the left mouse button is held
                if canvas.rect.collidepoint(mouse_pos):
                    canvas.clicked(mouse_pos)

        draw(WIN, canvas, toolbar, animator, preview)

    pygame.quit()


# TODO?: Instead of redrawing the
#  whole grid just redraw the pixels (if any) that change this frame. '?' because this is just for optimisation,
#  and realistically that doesn't matter at all for this simple use case
def draw(win, canvas, toolbar, animator, preview):

    win.fill(CREAM)

    canvas_surface = canvas.get_surface()
    win.blit(canvas_surface, canvas.rect)

    toolbar_surface = toolbar.get_surface()
    win.blit(toolbar_surface, toolbar.rect)

    animator_surface = animator.get_surface()
    win.blit(animator_surface, animator.rect)

    preview_surface = preview.get_surface()
    win.blit(preview_surface, preview.rect)

    pygame.display.update()


# Only run if this file is loaded directly (not through a module import)
if __name__ == "__main__":
    main()
