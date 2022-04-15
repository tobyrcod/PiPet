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

    file = tkinter.filedialog.askopenfile(
        initialdir="/",
        title="Select a file"
    )
    root.destroy()

    return file

def prompt_save_file():
    root = tkinter.Tk()
    root.withdraw()
    root.title("Animation Tool")

    files = [('All Files', '*.json')]

    file = tkinter.filedialog.asksaveasfile(
        initialdir=os.path.curdir + "/animation_files",
        title="Select a file",
        filetypes=files,
        defaultextension=files
    )
    root.destroy()

    return file, Path(file.name).stem
