import math
import random

import pygame

from settings import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish")

SKY_COLOR = (255, 116, 0)

SPAWN_FISH = pygame.USEREVENT
pygame.time.set_timer(SPAWN_FISH, 1000)


class Waves:
    speed = 0.3
    magnitude = 4

    def __init__(self):
        sprite_raw = pygame.image.load("Fish/waves.png")
        self.sprite = sprite_raw
        self.start_x = WIDTH // 2 - self.sprite.get_width() // 2

    def draw(self, win):
        pos_x = self.start_x + self.magnitude * math.sin(math.radians(pygame.time.get_ticks() * self.speed))
        win.blit(self.sprite, (pos_x, 10))


class Boat:
    speed = 4

    def __init__(self):
        sprite_raw = pygame.image.load("Fish/boat.png")
        height = 60
        self.sprite = pygame.transform.scale(sprite_raw,
                                             (height * sprite_raw.get_width() / sprite_raw.get_height(), height))
        self.x = 20
        self.y = 40

        self.line = None

    def draw(self, win):
        win.blit(self.sprite, (self.x, self.y))

    def move(self, x):
        if self.line is None:
            self.x += self.speed * x
            if self.x < 20:
                self.x = 20
            elif self.x > WIDTH - self.sprite.get_width() - 20:
                self.x = WIDTH - self.sprite.get_width() - 20

    def create_line(self):
        middle = self.x + self.sprite.get_width() // 2
        self.line = Line(middle, self.y + self.sprite.get_height())

    def destroy_line(self):
        self.line = None

    def lower_line(self, win):
        if self.line is not None:
            self.line.lower_line()
            self.line.draw(win)


class Line:

    speed = 3

    def __init__(self, x, top_y):
        self.x = x
        self.top_y = top_y
        self.height = 0

    def lower_line(self):
        if self.height <= HEIGHT - 120:
            self.height += self.speed

    def draw(self, win):
        pygame.draw.line(win, (0, 0, 0), (self.x, self.top_y), (self.x, self.top_y + self.height), 5)
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.top_y + self.height), 5)


class Fish:
    small_fish = [pygame.image.load("Fish/red_fish_1.png"),
                  pygame.image.load("Fish/orange_fish_1.png"),
                  pygame.image.load("Fish/yellow_fish_1.png")]

    big_fish = [pygame.image.load("Fish/red_fish_2.png"),
                pygame.image.load("Fish/orange_fish_2.png"),
                pygame.image.load("Fish/yellow_fish_2.png")]

    special_fish = pygame.image.load("Fish/black_fish.png")

    def __init__(self, type=-1):
        if type == 2:
            self.speed = 0.3

            sprite_raw = self.special_fish
            height = 40
            self.sprite = pygame.transform.scale(sprite_raw,
                                                 (height * sprite_raw.get_width() / sprite_raw.get_height(), height))

            dir = random.choice([0, 1])
            self.sprite = pygame.transform.flip(self.sprite, bool(dir), False)
            self.x = [-self.sprite.get_width(), WIDTH][dir]
            self.dir = dir * -2 + 1
            self.y = random.randint(HEIGHT - self.sprite.get_height() - 50, HEIGHT - self.sprite.get_height() - 10)
        else:
            self.speed = 0.6 + random.uniform(-0.3, 0.3)

            if type == -1:
                type = random.choice([1, 2])
            self.type = type

            sprite_raw = random.choice(self.small_fish) if type == 1 else random.choice(self.big_fish)
            height = 30
            self.sprite = pygame.transform.scale(sprite_raw,
                                                 (height * sprite_raw.get_width() / sprite_raw.get_height(), height))

            dir = random.choice([0, 1])
            self.sprite = pygame.transform.flip(self.sprite, bool(dir), False)
            self.x = [-self.sprite.get_width(), WIDTH][dir]
            self.dir = dir * -2 + 1
            self.y = random.randint(120, HEIGHT - self.sprite.get_height() - 10)

    def draw(self, win):
        win.blit(self.sprite, (self.x, self.y))

    def move(self):
        self.x += self.dir * self.speed


def main():
    run = True
    clock = pygame.time.Clock()

    boat = Boat()
    waves = Waves()
    fishes = []

    spawn_special = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == SPAWN_FISH:
                fishes.append(Fish())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    boat.create_line()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    boat.destroy_line()

        if spawn_special and pygame.time.get_ticks() > 10000:
            fishes.append(Fish(2))
            spawn_special = False

        WIN.fill(SKY_COLOR)

        waves.draw(WIN)
        boat.draw(WIN)

        for fish in fishes:
            fish.draw(WIN)
            fish.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            boat.move(-1)
        elif keys[pygame.K_d]:
            boat.move(1)

        if keys[pygame.K_SPACE]:
            boat.lower_line(WIN)

        pygame.display.update()

    pygame.quit()


# Only runs main() if this file is being run directly,
# ie. not being imported as a module
if __name__ == '__main__':
    main()
