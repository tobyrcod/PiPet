import json
from sense_hat import SenseHat #use this when implementing in rasp pi
from time import sleep
import sys
import numpy as np


s = SenseHat()

g = (0, 255, 0)
o = (255, 165, 0)
r = (255, 0, 0)
w = (0, 0, 0)

class Animation:
    def __init__(self, _name):

        self.name = _name   #"idle.py" for example
        self.delay = 0
        self.faces = []

        #array of arrays 
        #array of frames for the animation
            #each array then has arrays that represent rows of pixels
                #each row array has a pixels as elements

    #load all aniamtions at the start of a game
    def load_animations(self):  #can only load 1 animation at a time - a change in the current animation
        #open correspinding file
        print("animation file is being loaded") #hopefully this folder navigation works :)
        #print("./GUIAnimationTool/animation_files/" + self.name)
        file = open("GUIAnimationTool/animation_files/" + self.name) #this is the correct directory
        data = json.load(file)  #data is the array of contents of json file
        print(data)

        #########################################

        self.delay = data["delay"]
        self.faces = data["faces"] #extracting the info into a bit easier use
        #print(self.faces)
    
        file.close()

        displayFaces = []    #this might be a good thing to have in a separate function
        for face in self.faces:
            temp = []
            for row in face:
                for element in row:
                    temp.append(element)
            
            displayFaces.append(temp)

        #print(displayFaces) #####################################

        #s.clear()
        for i in displayFaces:
            s.set_pixels(i)
            sleep(self.delay)
        s.clear()

        ####################################

    
class Bar:
    ##array that holds the health bar value
    #colours for at what point the bar should be (red for <10, green >90. etc
    #idle animation
    
    def __init__(self, gameLives):  #game lives can be a max of 6! because of pixels, or 8 if it looks better but 6 for now

        self.max = gameLives
        self.pipetBar = 0
        self.playerBar = 0 

        self.healthBars = [ #full health bars on both sides
            [w, w, w, w, w, w, w, w],
            [g, w, w, w, w, w, w, g],
            [g, w, w, w, w, w, w, g],
            [g, w, w, w, w, w, w, g],
            [g, w, w, w, w, w, w, g],
            [g, w, w, w, w, w, w, g],
            [g, w, w, w, w, w, w, g],
            [w, w, w, w, w, w, w, w]
        ]

        self.displayToSH()
        
        
    def health_bar_change(self, lossSide, amount, animName):
        #side param = which side (pipet = L or player = R) the health bar should go down
        #amount param = by how much this bar should go down by (could be different in various games)

        #there is defo going ot be a way to make all the below pretty much repreatred things into 1 generalised section
        if lossSide == "R":
            self.playerBar += amount


            if self.playerBar >= 2:#self.max:
                #END THE GAME SOMEONE HAS WON
                s.clear()
                
                #print(self.playerBar + " >= " + self.max)

                Animation("playerlost.pipet").load_animations()
                
                import menu
                sys.modules.pop("menu")
                    

            else:
                #we can update the display 

                lboundary = self.playerBar + 1
                #the boundary is the position of the first coloured in block

                for i in range(lboundary - amount, lboundary):    #lowering the bar accordingly
                    #might need to be boundary -1  ^^
                    self.healthBars[i][0] = w
                
                if lboundary > 3 and lboundary < 5:
                    #colour the rest in orange
                    for i in range(lboundary, 7):
                        self.healthBars[i][0] = o

                elif lboundary == 5:
                    #colour rest in red
                    for i in range(lboundary, 7):
                        self.healthBars[i][0] = r

        else:
            self.pipetBar += amount

            if self.pipetBar >= 2:#self.max:

                s.clear()
                #print(self.pipetBar + " >= " + self.max)
                Animation("pipetlost.pipet").load_animations()
                
                import menu
                sys.modules.pop("menu")
                

            else:
                rboundary = self.pipetBar + 1
                #the boundary is the position of the first coloured in block

                for i in range(rboundary - amount, rboundary):    #lowering the bar accordingly
                    #might need to be boundary -1  ^^
                    self.healthBars[i][7] = w
                
                if rboundary > 3 and rboundary < 5:
                    #colour the rest in orange
                    for i in range(rboundary, 7):
                        self.healthBars[i][7] = o

                elif rboundary == 5:
                    #colour rest in red
                    for i in range(rboundary, 7):
                        self.healthBars[i][7] = r

    
        a = Animation(animName)
        a.load_animations()  #with the new animation name as a param, so shock face for example       

        #display the updated health bars for hte game to continue
        self.displayToSH()
        

    def displayToSH(self):
        displayHealthBars = []    #this might be a good thing to have in a separate function
        for row in self.healthBars:
            for element in row:
                displayHealthBars.append(element)

        #print(displayHealthBars) #####################################
        
        s.clear()
        s.set_pixels(displayHealthBars)
        

