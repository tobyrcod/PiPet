import json
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


def load_display_settings(filepath):
    file = open(filepath)
    data = json.load(file)

    dict_colorsvals = {}
    for color in data["color_values"]:
        dict_colorsvals[color["key"]] = color["value"]

    return dict_colorsvals


if __name__ == '__main__':
    colors = load_display_settings("display_settings.json")

   #when adding a frame/face in gui, this will do all the work for youin that you wont have to
   #have a set colours, colour keys will prob go 0 to 1 or something
   #so will create this 8 x 8 grid and you need to click them into existence




