
#health bar change when recieving point loss
    #display this in the sense hat
    #

import DisplayController.display_controller as dispCont

class Bar:
    ##array that holds the health bar value
    #colours for at what point the bar should be (red for <10, green >90. etc
    #idle animation
    
    def __init__(self, gameLives):  #game lives can be a max of 6! because of pixels, or 8 if it looks better but 6 for now
        w = (255, 255, 255)
        b = (0, 0, 0)
        r = (255, 0, 0)
        o = (255, 165, 0)
        g = (0, 128, 0)

        self.totLives = gameLives

        self.pipetBar = self.totLives
        self.playerBar = self.totLives
        
        self.currDisplay = [    #initial display 
        b, b, b, b, b, b, b, b,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        g, b, b, b, b, b, b, g,
        b, b, b, b, b, b, b, b
        ]

        dispCont.load_Animations(filepath = "./DisplayController/animations.json")
        #loads all animations at the start of the game

        #can you habe a method in the init? if not we read from the json files settings nad animation
        # and leave curr Display as empty

        #maybe just keep this as the initial in terms of letters
        #and then overwrite it whenever there is a change using the json stuff
        #yeah so as soon as there is a change, load the display_controller py file
        
        

    def health_bar(self, lossSide, amount, animName):
        #side param = which side (pipet = L or player = R) the health bar should go down
        #amount param = by how much this bar should go down by (could be different in various games)

        #CHANGE IN ANIMATION
        dispCont.reaction(animName)  #with the new animation name as a param
        



        #successfully returns a dictionary of colour values
        
        #create a display of 2 full health bars, this will be in the init
        #access the json file to change it there?


        #if lossSide == 'L': #if pipet lost the point
            #create an algorithm that changes only the corresponding side 




        #print("heatlh bar is decreased for " + lossSide)
        #print("health bar decreased by " + str(amount))



        #update display of sense hat with corresponding decreased bar and 
        #shocked animation if pipet lost the point and happy animation if pipet won a point



#while True:     #idle animations
    


#animation change recievers