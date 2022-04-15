import json
import tkinter


def get_color_dict(filepath):
    colors_file = open(filepath, 'r')
    colors_text = colors_file.read()
    colors_json = json.loads(colors_text)
    colors_file.close()

    colors_dict = colors_json["colour_dict"]
    return colors_dict


def convert_color_grid_to_key_grid(color_array):
    pass


def prompt_open_file():
    root = tkinter.Tk()
    root.title("Animation Tool")

    file_name = tkinter.filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=("json files", "*.json"),
    )