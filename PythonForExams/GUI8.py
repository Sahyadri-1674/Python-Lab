import tkinter as tk
root = tk.Tk()
text_var = tk.DoubleVar()
spin_box = tk.Spinbox(
root,
from_=0.6,
to=50.0,
increment=.01,
textvariable=text_var
)
print(text_var.set(25))

spin_box.pack()
root.mainloop()



import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk


