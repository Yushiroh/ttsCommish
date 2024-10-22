import os
import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import ImageTk, Image

# window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title('Grid')
window.geometry('600x400')


descTTS = ["1a", "2a", "3a","4a", "5a", "6a"]

nfTTS = ["1b", "2b", "3b","4b", "5b", "6b"]


def butFunc(aString,bString):
    print("Pressed")
    print(aString)

    if but2["text"] == "Button2":
        os.system(f'mpg123 recordings/{aString}.mp3')
    else:
        os.system(f'mpg123 recordings/{bString}.mp3')
        

def butFunc1():
    print("img")
    nfDisplay = ImageTk.PhotoImage(Image.open("nfimg/nf1.PNG"))
    panel = tk.Label(window, image=nfDisplay)
    panel.image = nfDisplay
    panel.grid(column=0, row=1, rowspan = 2, columnspan = 2, sticky='nsew')

but1 = tk.Button(window, text="Button", command= lambda: butFunc(descTTS[0], nfTTS[0]))
but2 = tk.Button(window, text="Button2", command= lambda: butFunc1())

window.columnconfigure([0,1], weight = 1)
window.rowconfigure([0,1,3], weight = 1)

but1.grid(column=0, row=0, sticky='nsew')
but2.grid(column=1, row=0, sticky='nsew')


window.mainloop()
