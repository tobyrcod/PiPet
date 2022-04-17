import pygame, sys, random
import DisplayController.display_controller as funct

class Ball:
    def __init__(self):
        self.ball = pygame.Rect(screenWidth / 2 - 15, screenHeight / 2 - 15, 30, 30) #will have many ball.center, ball.x, ball.y etc as properties of the pygame object
        self.ballSpeedX = 7 * random.choice((1,-1))
        self.ballSpeedY = 7 * random.choice((1,-1))

    def ball_start(self, pointSide):
        #########################################
        #info to send into funct. file
        #which side won the point
        #by how much the point is lost (so by how much the health bar goes down by)
        if pointSide == "L":
            bar.health_bar_change(pointSide, 1, "idle_healthBar.pipet")


        elif pointSide == "R":
            #this is the returning animation
            bar.health_bar_change(pointSide, 1, "idle_healthBar.pipet")
            


        self.ball.center = (screenWidth / 2, screenHeight / 2)
        self.ballSpeedX *= random.choice((1,-1))
        self.ballSpeedY *= random.choice((1,-1))

class Sticks:
    def __init__(self):
        self.player = pygame.Rect(screenWidth - 20, screenHeight / 2 - 70, 10, 140)
        self.opponent = pygame.Rect(10, screenHeight / 2 - 70, 10, 140)

        self.playerSpeed = 0
        self.opponentSpeed = 7

        self.playerScore = 0
        self.opponentScore = 0

    def player_animation(self):
        self.player.y += self.playerSpeed
        
        if self.player.top <= 0:
            self.player.top = 0
        
        if self.player.bottom >= screenHeight:
            self.player.bottom = screenHeight


#outside ball class
def ball_animation():
    
    b.ball.x += b.ballSpeedX
    b.ball.y += b.ballSpeedY

    if b.ball.top <= 0 or b.ball.bottom >= screenHeight:
        b.ballSpeedY *= -1

    #player score 
    if b.ball.left <= 0:
        b.ball_start('R')
        stick.playerScore += 1

    #opponent score
    if b.ball.right >= screenWidth:
        b.ball_start('L')
        stick.opponentScore += 1

    if b.ball.colliderect(stick.player) or b.ball.colliderect(stick.opponent):
        b.ballSpeedX *= -1


def opponent_ai():     ##so its based on what position the ball is on the screen 
    if stick.opponent.top < b.ball.y:
        stick.opponent.y += stick.opponentSpeed

    if stick.opponent.bottom > b.ball.y:
        stick.opponent.y -= stick.opponentSpeed

    if stick.opponent.top <= 0:
        stick.opponent.top = 0

    if stick.opponent.bottom >= screenHeight:
        stick.opponent.bottom = screenHeight


#general setup
pygame.init()
clock = pygame.time.Clock()

#setting up main window
screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong")

#game rectangles for display
#(x,y) is the top left
game_font = pygame.font.Font("freesansbold.ttf", 32)
bg_colour = pygame.Color("grey12")
light_grey = (200, 200, 200)

bar = funct.Bar(6)   #creating an instance of the health bar on the sense hat
bar.displayToSH()

#class initiation
b = Ball()
stick = Sticks()

#idleAnimation = funct.Animation("/GUIAnimationTool/idle_healthBar.pipet", True)

while True:  #only checks whether user has pressed exist button
    #handling input

    for event in pygame.event.get():        #event is clikc of a button, movement of mouse, etc...
        if event.type == pygame.QUIT:   #pygame.quit is the exit button
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                stick.playerSpeed += 7
            if event.key == pygame.K_UP:
                stick.playerSpeed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                stick.playerSpeed -= 7
            if event.key == pygame.K_UP:
                stick.playerSpeed += 7  

    #game logic
    ball_animation()
    stick.player_animation()
    opponent_ai()

    #visuals
     #visuals
    screen.fill(bg_colour)  #background colour
    pygame.draw.rect(screen, light_grey, stick.player)    #does it matter whether you use Rect or rect?
    pygame.draw.rect(screen, light_grey, stick.opponent)
    pygame.draw.ellipse(screen, light_grey, b.ball)
    pygame.draw.aaline(screen, light_grey, (screenWidth/2,0), (screenWidth/2, screenHeight))   #anti ailias line

    #this needs to be above the background
    player_text = game_font.render(f"{stick.playerScore}", False, light_grey)#f"{p1.player_score}", False, light_grey)
    screen.blit(player_text, (660, 470)) #.blit puts one surface on top of another

    opponent_text = game_font.render(f"{stick.opponentScore}",False, light_grey) #f"{opp.opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    #updating window
    pygame.display.flip()
    clock.tick(60)
