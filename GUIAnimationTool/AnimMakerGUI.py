# Based on 'Make Paint in Python'
# https://www.youtube.com/watch?v=N20eXcfyQ_4
import os.path

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
    def check_for_erase_button_active():
        if toolbar.active_brush_button == toolbar.brush_buttons["Erase"]:
            button = toolbar.brush_buttons['Brush']
            button.events.on_clicked(button)

    menu_bar = MenuBar(pygame.Rect(0, 0, MENU_BAR_WIDTH, MENU_BAR_HEIGHT))
    canvas = Canvas(pygame.Rect(PADDING, PADDING + MENU_BAR_HEIGHT, CANVAS_WIDTH, CANVAS_HEIGHT))
    animator = Animator(pygame.Rect(PADDING, PADDING + canvas.rect.bottom, ANIMATOR_WIDTH, ANIMATOR_HEIGHT))
    toolbar = Toolbar(pygame.Rect(canvas.rect.right + PADDING, canvas.rect.top, TOOLBAR_WIDTH, TOOLBAR_HEIGHT))
    preview = Preview(pygame.Rect(animator.rect.right + PADDING, animator.rect.top, PREVIEW_WIDTH, PREVIEW_HEIGHT), animator.timeline)  # TODO: use events for when the frames change instead of passing the whole timeline

    animator.timeline.events.on_active_timeline_frame_index_changed += lambda index: canvas.set_frame(animator.timeline.timeline_frames[index].frame)
    animator.timeline.events.on_timeline_frame_added += lambda tf: preview.go_to_beginning()
    animator.timeline.events.on_timeline_frame_deleted += lambda tf: preview.go_to_beginning()
    animator.timeline.init()

    for button in toolbar.color_buttons:
        button.events.on_clicked += toolbar.set_active_color_button
        button.events.on_clicked += lambda button: canvas.change_draw_color(button.color)
        button.events.on_clicked += lambda button: check_for_erase_button_active()

    for button in toolbar.brush_buttons.values():
        button.events.on_clicked += toolbar.set_active_brush_button

    # I know using lambdas for events isn't the best as I lose the ability to remove them, but I dont ever need to
    toolbar.brush_buttons['Erase'].events.on_clicked += lambda b: canvas.set_to_erase()
    toolbar.brush_buttons['Brush'].events.on_clicked += lambda b: canvas.set_to_brush()
    toolbar.brush_buttons['Fill'].events.on_clicked += lambda b: canvas.set_to_fill()

    toolbar.other_buttons['Clear'].events.on_clicked += lambda b: canvas.clear()

    toolbar.color_buttons[0].events.on_clicked(toolbar.color_buttons[0])

    # Create TextInput-object
    run = True
    while run:
        clock.tick(FPS)

        events = pygame.event.get()

        preview.update(events)

        for event in events:
            if event.type == pygame.QUIT:
                run = False
                preview.pause()

            # TODO: make this more elegant (...matrix?)
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # if the left mouse button is clicked
                if menu_bar.rect.collidepoint(mouse_pos):
                    menu_bar.clicked(mouse_pos)
                elif toolbar.rect.collidepoint(mouse_pos):
                    toolbar.clicked(mouse_pos)
                elif canvas.rect.collidepoint(mouse_pos):
                    canvas.clicked(mouse_pos)
                elif animator.rect.collidepoint(mouse_pos):
                    animator.clicked(mouse_pos)
                elif preview.rect.collidepoint(mouse_pos):
                    preview.clicked(mouse_pos)
            elif pygame.mouse.get_pressed()[0]:  # if the left mouse button is held
                if canvas.rect.collidepoint(mouse_pos):
                    canvas.clicked(mouse_pos)
                elif animator.rect.collidepoint(mouse_pos):
                    animator.held(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    animator.timeline.set_active_timeline_frame_index(animator.timeline.active_timeline_frame_index - 1)
                elif event.key == pygame.K_RIGHT:
                    animator.timeline.set_active_timeline_frame_index(animator.timeline.active_timeline_frame_index + 1)
                elif event.key == pygame.K_q:
                    button = toolbar.brush_buttons['Brush']
                    button.events.on_clicked(button)
                elif event.key == pygame.K_w:
                    button = toolbar.brush_buttons['Fill']
                    button.events.on_clicked(button)
                elif event.key == pygame.K_e:
                    button = toolbar.brush_buttons['Erase']
                    button.events.on_clicked(button)

        draw(WIN, canvas, toolbar, animator, preview, menu_bar)

    pygame.quit()


# TODO?: Instead of redrawing the
#  whole grid just redraw the pixels (if any) that change this frame. '?' because this is just for optimisation,
#  and realistically that doesn't matter at all for this simple use case
def draw(win, canvas, toolbar, animator, preview, menu_bar):

    win.fill(DARK_BLUE)

    canvas_surface = canvas.get_surface()
    win.blit(canvas_surface, canvas.rect)

    toolbar_surface = toolbar.get_surface()
    win.blit(toolbar_surface, toolbar.rect)

    animator_surface = animator.get_surface()
    win.blit(animator_surface, animator.rect)

    preview_surface = preview.get_surface()
    win.blit(preview_surface, preview.rect)

    menu_bar_surface = menu_bar.get_surface()
    win.blit(menu_bar_surface, menu_bar.rect)

    pygame.display.update()


# Only run if this file is loaded directly (not through a module import)
if __name__ == "__main__":
    main()
