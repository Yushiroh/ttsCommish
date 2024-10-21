import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title('Grid')
window.geometry('600x400')

# widgets 
label1 = ttk.Label(window, text = 'Category', anchor= 'center', borderwidth = '1', relief= "solid")
label2 = ttk.Label(window, text = 'Name', anchor= 'center', borderwidth = '1', relief= "solid")
label3 = ttk.Label(window, text = 'Ingredients', anchor= 'center', borderwidth = '1', relief= "solid")
label4 = ttk.Label(window, text = 'Allergens', anchor= 'center', borderwidth = '1', relief= "solid")
label5 = ttk.Label(window, text = 'Expiration', anchor= 'center', borderwidth = '1', relief= "solid")
label6 = ttk.Button(window, text = 'Text to Speech')
label7 = ttk.Button(window, text = 'Display Nutrition Facts')
# define a grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 2)
window.columnconfigure(2, weight = 2)
window.columnconfigure(3, weight = 1)
window.columnconfigure(4, weight = 3)

window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)
window.rowconfigure(2, weight = 2)
window.rowconfigure(3, weight = 2)
window.rowconfigure(4, weight = 1)
window.rowconfigure(5, weight = 1)

# place a widget
label1.grid(row = 1, column = 1, sticky = 'nsew')
label2.grid(row = 1, column = 2, sticky = 'nsew')
label3.grid(row = 2, column = 1, rowspan = 2, columnspan = 2, sticky = 'nsew')
label4.grid(row = 4, column = 1, sticky = 'nsew')
label5.grid(row = 4, column = 2, sticky = 'nsew')
label6.grid(row = 0, column = 4, rowspan = 3, sticky = 'nsew')
label7.grid(row = 3, column = 4, rowspan = 3, sticky = 'nsew')


#sample

# run
window.mainloop()
