import tkinter as tk


m = tk.Tk(className = 'sample')
m.attributes('-fullscreen', True)


label1 = tk.Label(m, text="Scan a product", bg="blue", padx=15, pady=15)
label2 = tk.Label(m, text="sample", bg="red", padx=15, pady=15)

#label2 = tk.Label(m, text="Label 2")
#label3 = tk.Label(m, text="Label 3")

label1.config(font=('Arial', 100))
label1.grid(row=0, column=0)

label2.config(font=('Arial', 100))
label2.grid(row=0, column=1)
#label3.grid(row=1, column=0)

m.mainloop()