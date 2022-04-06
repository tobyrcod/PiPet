import json, random
from sense_hat import SenseHat #use this when implementing in rasp pi
from time import sleep

s = SenseHat()


# TODO: Design JSON
# TODO: Load JSON
# TODO: Turn JSON into instance of face class
# TODO: Write a Play Face Controller

# We call the physical display the 'display', which we apply different faces too (the animations)
# (method) of animation = an order in which faces are shown up on the led

# idle animation whist there is no action from the keyboard
# just start doing object orientied animations

# expansion on it v
# Finite State Machine to handle which face is currently playing

# Loading the Display Settings

# have 2 keys essentially
# accessing via name, easy for us, nice to display in the GUI
# accessing via number, good for drawing out animations

# split it into coloru value and volor name
# better to do it this way instead of deriving the name of the colour
#   from a function to translate the rbg value into name of colour (next closest colour)
#   as this would be v inefficient, and uncessesary when theres this way

#object to store the json animation object

class Animation:
    def __init__(self):
        self.colourVals = []#"" vv
        self.anim_info = [] #will be an array of dictionaries
        self.faces = []

    #load all aniamtions at the start of a game
    def load_animations(self, filepath):  #can only load 1 animation at a time - a change in the current animation
        print("loading colour values...")
        print("file path = " + filepath)

        file = open(filepath)
        data = json.load(file)  #data is the array of contents of json file
        print(data)

        #########################################

        for colour_info in data["colour_values"]:
            tempDict = {}
            tempDict["key"] = colour_info["key"]
            tempDict["value"] = colour_info["value"]
            tempDict["name"] = colour_info["name"] 
            self.colourVals.append(tempDict)

        print(self.colourVals)  #successfully gets the information of each colour stored in json file

        ####################################

        print("loading animation info...")  #extracts all animations 
        #do we want to only extract the specified aniamtion? yes

        for animation_info in data["animations"]:
            #if animation_info["name"] == animName:
            tempDict = {}

            tempDict["name"] = animation_info["name"]
            tempDict["delay"] = animation_info["delay"]
            tempDict["reps"] = animation_info["reps"]
            tempDict["order"] = animation_info["order"]

            self.anim_info.append(tempDict)


        print(self.anim_info)    #successfully gets the required animation information

        #####################################
         
        for face in data["faces"]:   #extracts all faces
            self.faces.append(face)
            
        print(self.faces)   #this all works yay

        file.close()

        ####################################

    def reaction(self, animName):
        #hwo to access the dictionary from the aniamtion name

        print("updating aniamtion")
        print("new animation == " + animName)
        print(self.anim_info)

        reaction = ""

        for animation in self.anim_info:
            if animation["name"] == animName:   #so once found the corresponding animation and its details
                reaction = animation

        if reaction == "":    #if none were found
            print("no reaction found")
            return None


        print(reaction)

        #### displaying the animation now we have checked there is such animation
        delay = reaction["delay"]
        reps = reaction["reps"]
        order = reaction["order"]

        sleep(delay)    #just to offset the current display delay

        #so the sense hat is just reading the integers in the array so we need to directly extract/map keys to colours

        activeFrames = []
        #convert the colour dictionary to rgb arrays in each position in frame
        #so just do like .replace for each character
        #for each character replace it with the rgb code etc

        colours = []    #extracting used colours
        print(self.colourVals)

        for entry in self.colourVals:
            colours.append([entry["key"], entry["value"]])

        print(colours)

        for face in self.faces:
            for i in range(len(face)):  #might need to be for i in range face[i]
                for colour in colours:
                    if face[i] == colour[0]: #if index value == a key 
                        face[i] = colour[1]   #replace it with he rgb value
                        break   #no need to check the other colours :)
        print(self.faces)

        s.clear()
            

        for i in range(reps):  #reps = how many times the order is repeated
            #go through the order however many repetitions there another
            for index in order:

                s.set_pixels(self.faces[index]) #setting the frame to show up on the pipet
                sleep(delay) #how long to keep the frame for

        s.clear()

    
        


# newAnim = Animation()
# newAnim.load_animations("animations.json")
# newAnim.reaction("test1")

   