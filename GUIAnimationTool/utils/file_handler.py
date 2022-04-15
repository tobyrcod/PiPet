import os, json


def get_color_dict(filepath):
    colors_file = open(filepath, 'r')
    colors_text = colors_file.read()
    colors_json = json.loads(colors_text)
    colors_file.close()

    colors_dict = colors_json["colour_dict"]
    return colors_dict