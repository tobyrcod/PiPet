from settings import *
from state import State
import numpy as np

CELL_SIZE = 55
CELL_COUNT = Vector2(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

SPRITE_BONE = pygame.image.load('Snake/bone.png')


def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))


class Snake:
    def __init__(self):
        self.body = [Vector2(2, 0), Vector2(1, 0), Vector2(0, 0)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        sprite_head = pygame.image.load('Snake/head.png')
        sprite_tail = pygame.image.load('Snake/body_tail.png')
        sprite_body_straight = pygame.image.load('Snake/body_straight.png')
        sprite_body_corner = pygame.image.load('Snake/body_corner.png')

        sprite_head = pygame.transform.scale(sprite_head, (CELL_SIZE, CELL_SIZE))
        sprite_tail = pygame.transform.scale(sprite_tail, (CELL_SIZE, CELL_SIZE))
        sprite_body_straight = pygame.transform.scale(sprite_body_straight, (CELL_SIZE, CELL_SIZE))
        self.sprite_body_corner = pygame.transform.scale(sprite_body_corner, (CELL_SIZE, CELL_SIZE))

        self.head_up = pygame.transform.rotate(sprite_head, 180)
        self.head_down = sprite_head
        self.head_right = pygame.transform.rotate(sprite_head, 90)
        self.head_left = pygame.transform.rotate(sprite_head, 270)

        self.tail_up = sprite_tail
        self.tail_down = pygame.transform.rotate(sprite_tail, 180)
        self.tail_right = pygame.transform.rotate(sprite_tail, 270)
        self.tail_left = pygame.transform.rotate(sprite_tail, 90)

        self.body_vertical = sprite_body_straight
        self.body_horizontal = pygame.transform.rotate(sprite_body_straight, 90)

    def draw_snake(self, win):

        # Draw Head
        head = self.body[0]
        # create a rectangle
        head_rect = pygame.Rect(int(head.x * CELL_SIZE), int(head.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # get the rotation of the sprite
        head_relation = head - self.body[1]
        # draw the rectangle
        win.blit(pygame.transform.rotate(self.head_down, angle_between(Vector2(0, 1), head_relation)), head_rect)

        for i in range(1, len(self.body) - 1):
            # get all the neighbour blocks
            block = self.body[i]
            previous_block = self.body[i + 1] - block
            next_block = self.body[i - 1] - block

            # create a rectangle
            block_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)

            if previous_block.x == next_block.x:
                win.blit(self.body_vertical, block_rect)
            elif previous_block.y == next_block.y:
                win.blit(pygame.transform.rotate(self.body_vertical, 90), block_rect)
            else:
                if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                    win.blit(pygame.transform.rotate(self.sprite_body_corner, 270), block_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                    win.blit(self.sprite_body_corner, block_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                    win.blit(pygame.transform.rotate(self.sprite_body_corner, 180), block_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                    win.blit(pygame.transform.rotate(self.sprite_body_corner, 90), block_rect)
        # Draw Head
        tail = self.body[-1]
        # create a rectangle
        tail_rect = pygame.Rect(int(tail.x * CELL_SIZE), int(tail.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # get the rotation of the sprite
        tail_relation = self.body[-2] - self.body[-1]
        # draw the rectangle
        win.blit(pygame.transform.rotate(self.tail_up, angle_between(Vector2(0, -1), tail_relation)), tail_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def set_direction(self, direction):
        if self.direction.dot(direction) == 0:
            self.direction = direction

    def add_block(self):
        self.new_block = True


class Fruit:
    def __init__(self):
        # create an x and y position
        self.pos = Vector2(0, 0)
        self.randomize()
        self.sprite = pygame.transform.scale(SPRITE_BONE, (CELL_SIZE, CELL_SIZE))

    def draw_fruit(self, win):
        # create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        win.blit(self.sprite, fruit_rect)

    def randomize(self):
        self.pos = Vector2(random.randint(0, int(CELL_COUNT.x) - 1), random.randint(0, int(CELL_COUNT.y) - 1))


class Main:
    def __init__(self, fsm):
        self.fsm = fsm
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw(self, win):
        win.fill((175, 215, 70))
        self.draw_grass(win)
        self.snake.draw_snake(win)
        self.fruit.draw_fruit(win)
        pygame.display.update()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # the head of the snake is on the fruit
            # reposition the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()

    def check_fail(self):
        # check for going off-screen
        if not 0 <= self.snake.body[0].x < CELL_COUNT.x:
            self.game_over()
        elif not 0 <= self.snake.body[0].y < CELL_COUNT.y:
            self.game_over()

        # check for eating your tail
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pass
        # pygame.quit()
        # sys.exit()
        # TODO: transition back to this state i.e starting over
        self.fsm.SetState(StateSnake(self.fsm))

    def draw_grass(self, win):
        grass_color = (167, 209, 61)

        for col in range(0, int(CELL_COUNT.x) + 1):
            for row in range(0, int(CELL_COUNT.y) + 1):
                if col % 2 == row % 2:
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(win, grass_color, grass_rect)


class StateSnake(State):

    def __init__(self, fsm):
        super().__init__(fsm)
        self.main_game = Main(fsm)

    def EnterState(self):
        super().EnterState()
        print("Entering Snake")

    def Update(self, win, keys):

        self.main_game.draw(win)

        if keys[pygame.K_w]:
            self.main_game.snake.set_direction(Vector2(0, -1))
        elif keys[pygame.K_s]:
            self.main_game.snake.set_direction(Vector2(0, 1))
        elif keys[pygame.K_a]:
            self.main_game.snake.set_direction(Vector2(-1, 0))
        elif keys[pygame.K_d]:
            self.main_game.snake.set_direction(Vector2(1, 0))

        for event in pygame.event.get():
            if event.type == SCREEN_UPDATE:
                self.main_game.update()

    def ExitState(self):
        super().ExitState()
        print("Exiting Snake")
