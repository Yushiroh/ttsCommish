import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title('Grid')
window.geometry('600x400')

entry1 = tk.Entry(window)
but1 =tk.Button(window)

def func(event):
    sampleText = entry1.get()
    label = tk.Label(window, text= sampleText)
    entry1.delete(0, tk.END)
    label.pack()


window.bind('<Return>', func)

entry1.pack()
but1.pack()


window.mainloop()
