from fileinput import filename
import json
import tkinter
import tkinter.filedialog
import os
from pathlib import Path

def get_color_dict(filepath):
    colors_file = open(filepath, 'r')
    colors_text = colors_file.read()
    colors_json = json.loads(colors_text)
    colors_file.close()

    colors_dict = colors_json["colour_dict"]
    return colors_dict

def prompt_open_file():
    root = tkinter.Tk()
    root.withdraw()
    root.title("Animation Tool")

    files = [('PiPet Animation Files', '*.pipet')]

    file = tkinter.filedialog.askopenfile(
        initialdir=os.path.curdir + "/animation_files",
        title="Select a file",
        filetypes=files,
        defaultextension=files
    )
    root.destroy()

    return file, None if file is None else Path(file.name).stem

def prompt_save_file():
    root = tkinter.Tk()
    root.withdraw()
    root.title("Animation Tool")

    files = [('PiPet Animation Files', '*.pipet')]

    file = tkinter.filedialog.asksaveasfile(
        initialdir=os.path.curdir + "/animation_files",
        title="Create a file",
        filetypes=files,
        defaultextension=files
    )
    root.destroy()

    return file, None if file is None else Path(file.name).stem
