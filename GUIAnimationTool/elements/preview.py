import numpy as np
import pygame.time
from threading import Thread
from utils import *


class Preview:
    def __init__(self, rect, timeline):
        self.rect = rect
        self.run = False
        self.fps = 1
        self.timeline = timeline
        self.current_frame_index = 0

        self.frame_rect = pygame.Rect(PREVIEW_PADDING, PREVIEW_PADDING, rect.width - 2 * PREVIEW_PADDING, rect.width - 2 * PREVIEW_PADDING)
        self.options_rect = pygame.Rect(PREVIEW_PADDING, self.frame_rect.bottom + FRAME_PADDING, self.frame_rect.width, rect.height - self.frame_rect.height - 3 * PREVIEW_PADDING)

        playpause_button_rect = pygame.Rect(0, 0, self.options_rect.height * 1.7, self.options_rect.height)
        playpause_button_rect.bottomright = self.options_rect.bottomright
        self.playpause_button = Button(playpause_button_rect, WHITE, 'PLAY')

        self.fps_input_rect = pygame.Rect(0, 0, self.options_rect.width - playpause_button_rect.width * 2 + PREVIEW_PADDING, playpause_button_rect.height)
        self.fps_input_rect.bottomright = np.add(playpause_button_rect.bottomleft, (1 * PREVIEW_PADDING, 0))

        self.fps_label_rect = pygame.Rect(0, 0, rect.width - 3 * PREVIEW_PADDING - self.fps_input_rect.width - playpause_button_rect.width, self.fps_input_rect.height)
        fps_label_font = get_font(size=40)
        self.fps_label_surface = fps_label_font.render('FPS:', 1, BLACK)
        self.fps_label_rect.bottom = np.add(self.fps_input_rect.bottom, self.fps_label_surface.get_height() / 4)
        self.fps_label_rect.left = self.frame_rect.left

        fps_input_manager = TextInputManager(
            initial='1',
            validator=lambda input: input == '' or (input.isdigit() and 1 <= int(input) <= 20)
        )
        self.fps_input = create_text_input(50, BLACK, fps_input_manager)

        self.thread = None
        self.clock = None
        self.playpause_button.events.on_clicked += self.play

    def update(self, events):
        self.fps_input.update(events)

        fps_value = self.fps_input.value
        self.fps = 1 if fps_value == '' else int(fps_value)

    def clicked(self, mouse_pos):
        local_pos = np.subtract(mouse_pos, self.rect.topleft)

        if self.playpause_button.rect.collidepoint(local_pos):
            self.playpause_button.events.on_clicked()

    def play(self):
        if self.thread is None and not self.run:
            clear_event(self.playpause_button.events.on_clicked)
            self.playpause_button.events.on_clicked += self.pause

            self.playpause_button.text = 'PAUSE'
            self.run = True
            self.thread = Thread(target=self.running)
            self.clock = pygame.time.Clock()
            self.thread.start()

    def running(self):
        while self.run:
            self.current_frame_index += 1
            self.current_frame_index %= len(self.timeline.timeline_frames)

            self.clock.tick(self.fps)

        self.playpause_button.text = 'PLAY'
        self.thread = None
        self.clock = None

    def pause(self):
        if self.thread is not None and self.run:
            clear_event(self.playpause_button.events.on_clicked)
            self.playpause_button.events.on_clicked += self.play

            self.run = False

    def go_to_beginning(self):
        self.current_frame_index = 0

    def get_surface(self):
        preview_surface = pygame.Surface(self.rect.size)

        # Background
        preview_surface.fill(WHITE)

        # Frames
        frame = self.timeline.timeline_frames[self.current_frame_index].frame
        frame_surface = frame.get_surface(self.frame_rect)
        preview_surface.blit(frame_surface, self.frame_rect)
        pygame.draw.rect(preview_surface, BLACK, self.frame_rect, PREVIEW_PADDING)

        # Options
        options_surface = pygame.Surface(self.options_rect.size)
        options_surface.fill(WHITE)
        preview_surface.blit(options_surface, self.options_rect)

        # Options -> Play/Pause Button
        playpause_button_surface = self.playpause_button.get_surface()
        preview_surface.blit(playpause_button_surface, self.playpause_button.rect)

        # Options -> FPS Label
        preview_surface.blit(self.fps_label_surface, self.fps_label_rect)

        # Options -> FPS input
        fps_input_surface = self.fps_input.surface
        preview_surface.blit(fps_input_surface, self.fps_input_rect)

        return preview_surface

