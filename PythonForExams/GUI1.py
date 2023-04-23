import tkinter as tk
parent = tk.Tk()
parent.resizable(0,0)
parent.title('-Basic GUI-')
my_label=tk.Label(parent,text='Hello',font=('Arial Bold',70))
my_label.grid(column=0,row=0)
parent.mainloop()


