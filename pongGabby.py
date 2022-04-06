
import pygame, sys, random

class Ball():
    def __init__(self):
        self.ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30,30)  #so ball is in the middle of the scrren
        self.ballSpeedX = 7 * random.choice((1,-1))
        self.ballSpeedY = 7 * random.choice((1,-1)) 
    
    def ball_restart(self):
        #self.ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30,30)  #so ball is in the middle of the scrren
        #this succesfully returns the ball back to the center, so essentially creates a new instance of hte ball
        #although it continues with an invisible ball... still being detected as a ball 

        self.center = (screenWidth/2, screenHeight/2)

        print("ball go!")
        self.ballSpeedY *= random.choice((1, -1))
        self.ballSpeedX *= random.choice((1, -1))

def ball_animation(self):
    _ball.x += b.ballSpeedX    #so this is the movement that is created
    _ball.y += b.ballSpeedY

    if _ball.top <= 0 or _ball.bottom >= screenHeight:  #if top of ball = 0 or bottom of ball = height of screen, y axis
        print("bottom is this bithc")
        b.ballSpeedY *= -1                           #then reverse the vertical ball speed

    if _ball.left <= 0:
        print("point has been gained")
        players.player_score += 1
        b.ball_restart()
    
    if _ball.right >= screenWidth:
        print("point has been lost")
        players.opponent_score += 1
        b.ball_restart()                            #x axis, multiply the speed by -1 to reverse, only speed not direction

    if _ball.colliderect(players.player) or _ball.colliderect(players.opponent):  #collisions for players
        b.ballSpeedX *= -1

####RIGHT, make sure this is all correct... so refernces comply withyhe classes


class Players():
    def __init__(self):
        self.player = pygame.Rect(screenWidth - 20, screenHeight/2-70, 10, 140)
        self.opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)

        self.player_score = 0
        self.opponent_score = 0

        self.playerSpeed = 0
        self.opponentSpeed = 7   

    def player_animation(self): #might need to put self as a parameter
        self.player.y += self.playerSpeed
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= screenHeight:
            self.player.bottom = screenHeight


def opponent_ai():          ##so its based on what position the ball is on the screen
    if players.opponent.top < _ball.y:
        players.opponent.top += players.opponentSpeed
    if players.opponent.bottom > _ball.y:
        players.opponent.bottom -= players.opponentSpeed

    if players.opponent.top <= 0:
        players.opponent.top = 0
    if players.opponent.bottom >= screenHeight:
        players.opponent.bottom = screenHeight




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
b = Ball()      #msybe issue is to do with the isntance of hte ball - go backt othe non object oriented and go from there. look back ar the video 
_ball = b.ball
players = Players()

p1 = players.player ##these two lines may not be needed
opp = players.opponent

game_font = pygame.font.Font("freesansbold.ttf", 32)

bg_colour = pygame.Color("grey12")
light_grey = (200, 200, 200)



while True:     #only checks whether user has pressed exist button
    
    #handling input
    for event in pygame.event.get():        #event is clikc of a button, movement of mouse, etc...
        if event.type == pygame.QUIT:   #pygame.quit is the exit button
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                players.playerSpeed += 7
            if event.key == pygame.K_UP:
                players.playerSpeed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                players.playerSpeed -= 7
            if event.key == pygame.K_UP:
                players.playerSpeed += 7                

    ball_animation(_ball)
    players.player_animation()
    opponent_ai()

    #visuals
    screen.fill(bg_colour)  #background colour
    pygame.draw.rect(screen, light_grey, p1)    #does it matter whether you use Rect or rect?
    pygame.draw.rect(screen, light_grey, opp)
    pygame.draw.ellipse(screen, light_grey, b.ball)
    pygame.draw.aaline(screen, light_grey, (screenWidth/2,0), (screenWidth/2, screenHeight))   #anti ailias line

    #this needs to be above the background
    player_text = game_font.render(f"{players.player_score}", False, light_grey)#f"{p1.player_score}", False, light_grey)
    screen.blit(player_text, (660, 470)) #.blit puts one surface on top of another

    opponent_text = game_font.render(f"{players.opponent_score}",False, light_grey) #f"{opp.opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    #updating window
    pygame.display.flip()
    clock.tick(60)





# import pygame, sys, random

# class Ball():
#     def __init__(self):
#         self.ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30,30)  #so ball is in the middle of the scrren
#         self.ballSpeedX = 7 * random.choice((1,-1))
#         self.ballSpeedY = 7 * random.choice((1,-1)) 
    
#     def ball_restart(self):
#         self.center = (screenWidth/2, screenHeight/2)
#         self.ballSpeedY *= random.choice((1, -1))
#         self.ballSpeedX *= random.choice((1, -1))

# def ball_animation():
#     _ball.x += b.ballSpeedX    #so this is the movement that is created
#     _ball.y += b.ballSpeedY

#     if _ball.top <= 0 or _ball.bottom >= screenHeight:  #if top of ball = 0 or bottom of ball = height of screen, y axis
#         print("bottom is this bithc")
#         b.ball *= -1                           #then reverse the vertical ball speed

#     if _ball.left <= 0:
#         p1.player_score += 1
#         b.ball_restart()

#     if _ball.right >= screenWidth:
#         opp.opponent_score += 1
#         b.ball_restart()                            #x axis, multiply the speed by -1 to reverse, only speed not direction

#     if _ball.colliderect(players.player) or _ball.colliderect(players.opponent):  #collisions for players
#         b.ballSpeedX *= -1

# ####RIGHT, make sure this is all correct... so refernces comply withyhe classes


# class Players():
#     def __init__(self):
#         self.player = pygame.Rect(screenWidth - 20, screenHeight/2-70, 10, 140)
#         self.opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)

#         self.player_score = 0
#         self.opponent_score = 0

#         self.playerSpeed = 0
#         self.opponentSpeed = 7   

#     def player_animation(self): #might need to put self as a parameter
#         self.player.y += self.playerSpeed
#         if self.player.top <= 0:
#             self.player.top = 0
#         if self.player.bottom >= screenHeight:
#             self.player.bottom = screenHeight




# def opponent_ai():          ##so its based on what position the ball is on the screen
#     if players.opponent.top < _ball.y:
#         players.opponent.top += players.opponentSpeed
#     if players.opponent.bottom > _ball.y:
#         players.opponent.bottom -= players.opponentSpeed

#     if players.opponent.top <= 0:
#         players.opponent.top = 0
#     if players.opponent.bottom >= screenHeight:
#         players.opponent.bottom = screenHeight







# #general setup
# pygame.init()
# clock = pygame.time.Clock()

# #setting up main window
# screenWidth = 1280
# screenHeight = 960 

# screen = pygame.display.set_mode((screenWidth, screenHeight))
# pygame.display.set_caption("Pong")

# #game rectangles for display
# #(x,y) is the top left
# b = Ball()
# _ball = b.ball
# players = Players()

# p1 = players.player ##these two lines may not be needed
# opp = players.opponent

# game_font = pygame.font.Font("freesansbold.ttf", 32)

# bg_colour = pygame.Color("grey12")
# light_grey = (200, 200, 200)



# while True:     #only checks whether user has pressed exist button
#     #handling input
#     for event in pygame.event.get():        #event is clikc of a button, movement of mouse, etc...
#         if event.type == pygame.QUIT:   #pygame.quit is the exit button
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 players.playerSpeed += 7
#             if event.key == pygame.K_UP:
#                 players.playerSpeed -= 7

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_DOWN:
#                 players.playerSpeed -= 7
#             if event.key == pygame.K_UP:
#                 players.playerSpeed += 7                

#     ball_animation()
#     players.player_animation()
#     opponent_ai()

#     #visuals
#     screen.fill(bg_colour)  #background colour
#     pygame.draw.rect(screen, light_grey, p1)    #does it matter whether you use Rect or rect?
#     pygame.draw.rect(screen, light_grey, opp)
#     pygame.draw.ellipse(screen, light_grey, b.ball)
#     pygame.draw.aaline(screen, light_grey, (screenWidth/2,0), (screenWidth/2, screenHeight))   #anti ailias line

#     #this needs to be above the background
#     player_text = game_font.render(f"{players.player_score}", False, light_grey)
#     screen.blit(player_text, (660, 470)) #.blit puts one surface on top of another

#     opponent_text = game_font.render(f"{players.opponent_score}", False, light_grey)
#     screen.blit(opponent_text, (600, 470))

#     #updating window
#     pygame.display.flip()
#     clock.tick(60)


