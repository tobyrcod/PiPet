from settings import *
from state import State
import stateb

SCORE_COLOUR = (106, 164, 148)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 8

SPRITE_EGG = pygame.image.load('Pong/egg.png')
SPRITE_CHICKEN = pygame.image.load('Pong/chicken_paddle.png')
SPRITE_BG = pygame.image.load('Pong/bg_grass.png')
SPRITE_GRASS = pygame.image.load('Pong/grass.png')

SCORE_FONT = COMIC_SANS


class Paddle:
    COLOR = WHITE
    SPRITE = pygame.transform.scale(SPRITE_CHICKEN, (PADDLE_WIDTH * 2, PADDLE_HEIGHT))
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.SPRITE = pygame.transform.flip(self.SPRITE, self.x > WIDTH // 2, False)

    def draw(self, win):
        win.blit(self.SPRITE, (self.x - PADDLE_WIDTH // 2, self.y))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    ROT = 0
    ROT_SPEED = -3
    SPRITE = pygame.transform.scale(SPRITE_EGG, (20, 20 * SPRITE_EGG.get_height() / SPRITE_EGG.get_width()))

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        rot_sprite = pygame.transform.rotate(self.SPRITE, self.ROT)
        win.blit(rot_sprite, (self.x - self.SPRITE.get_width() // 2, self.y - self.SPRITE.get_height() // 2))

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.ROT += self.ROT_SPEED

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

        self.x_vel *= -1
        self.y_vel = 0


def draw(win, paddles, ball, left_score, right_score):
    win.blit(SPRITE_BG, (0, 0))

    win.blit(SPRITE_GRASS, (0, HEIGHT - SPRITE_GRASS.get_height()))
    win.blit(pygame.transform.flip(SPRITE_GRASS, True, True), (0, 0))
    win.blit(pygame.transform.rotate(SPRITE_GRASS, 270), (0, 0))
    win.blit(pygame.transform.rotate(SPRITE_GRASS, 90), (WIDTH - SPRITE_GRASS.get_height(), 0))

    left_score_text = SCORE_FONT.render(f"{left_score}", True, SCORE_COLOUR)
    right_score_text = SCORE_FONT.render(f"{right_score}", True, SCORE_COLOUR)

    win.blit(left_score_text,
             (WIDTH // 4 - left_score_text.get_width() // 2, HEIGHT // 2 - left_score_text.get_height() // 2))
    win.blit(right_score_text,
             (3 * WIDTH // 4 - right_score_text.get_width() // 2, HEIGHT // 2 - right_score_text.get_height() // 2))

    for paddle in paddles:
        paddle.draw(win)

    ball.draw(win)

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):
    # Left Paddle
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.height + left_paddle.VEL <= HEIGHT:
        left_paddle.move(up=False)

    # Right Paddle
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height + right_paddle.VEL <= HEIGHT:
        right_paddle.move(up=False)


def handle_collision(ball, left_paddle, right_paddle):
    # Collision with Floor
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    # Collision with Floor
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # Left Paddle
    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height // 2
                difference_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_y / reduction_factor
                ball.y_vel = -y_vel
    # Right Paddle
    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height // 2
                difference_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_y / reduction_factor
                ball.y_vel = -y_vel


def reset(ball, left_paddle, right_paddle):
    ball.reset()
    left_paddle.reset()
    right_paddle.reset()


class StateC(State):

    def __init__(self, fsm):
        super().__init__(fsm)
        # IMPORTANT: Remember in pygame (0,0) is the top left, so we need offsets to center things
        self.left_paddle = Paddle(40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.right_paddle = Paddle(WIDTH - 40 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

        # The Pong Ball
        self.ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

        # The Players Scores
        self.left_score = 0
        self.right_score = 0

    def EnterState(self):
        super().EnterState()
        print("Entering Pong")

    def Update(self, win, keys):
        super().Update(win, keys)

        draw(win, [self.left_paddle, self.right_paddle], self.ball, self.left_score, self.right_score)

        handle_paddle_movement(keys, self.left_paddle, self.right_paddle)

        self.ball.move()
        handle_collision(self.ball, self.left_paddle, self.right_paddle)

        if self.ball.x < 40:
            self.right_score += 1
            reset(self.ball, self.left_paddle, self.right_paddle)
        elif self.ball.x > WIDTH - 40:
            self.left_score += 1
            reset(self.ball, self.left_paddle, self.right_paddle)

        if keys[pygame.K_b]:
            self.fsm.SetState(stateb.StateB(self.fsm))

    def ExitState(self):
        super().ExitState()
        print("Exiting Pong")
