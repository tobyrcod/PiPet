import pygame, sys



pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):   
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
            
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):           
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):  #checks if we are clicking on button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play(): #the play button 
    pygame.display.set_caption("Play")  #this needs to run pong
    import pongpt2
    sys.modules.pop("pongpt2")
    
    

    #while True:
        #PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("black")    #illusion of user being shown a different screen 
        
        #this runs the file just need to wait for the button ot be clicked
        
        
        
        
        
            

       # pygame.display.update()
        
        
        # PLAY_TEXT = get_font(45).render("this is the play screen", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center = (640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # PLAY_BACK = Button(image = None, pos = (640, 460), text_input = "BACK", font = get_font(75), base_color = "White", hovering_color = "Green")

        # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # PLAY_BACK.update(SCREEN)

        # for event in pygame.event.get():    #quitting the program 
        #     if event.type == pygame.QUIT:   
        #         pygame.quit()
        #         sys.exit()

        #     if event.type == pygame.MOUSEBUTTONDOWN:    #navigation to the main menu
        #         if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
        #             main_menu()

        

def main_menu(): #main menu screen
    pygame.display.set_caption("Menu")

    while True: #running like a game, this will always be shown 
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center = (640, 1000))

        PLAY_BUTTON = Button(image = pygame.image.load("assets/Play Rect.png"), pos = (640, 250), text_input = "PLAY", font = get_font(75), base_color="#d7fcd4", hovering_color = "White")

        QUIT_BUTTON = Button(image = pygame.image.load("assets/Quit Rect.png"), pos = (640, 500), text_input = "QUIT", font = get_font(75), base_color="#d7fcd4", hovering_color = "White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():    #clicking the x on the window
            if event.type == pygame.QUIT:   
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()


#multiple screens in pygame
#just cover it with a fill  function
