import tkinter as tk


root = tk.Tk()
root.title('RadioButton')
root.geometry('500x400')

f1 = tk.Frame(root,width=200,height=150,bg='white')
f1.grid(column=0,row=0)

rgrp = tk.IntVar()
rbtn = tk.Radiobutton(f1,text='Male',font=('Arial',12,),variable=rgrp,value=0)
rbtn.pack(anchor= 'w',ipady=5)
rbtn1 = tk.Radiobutton(f1,text='Female',font=('Arial',12),variable=rgrp,value=1)
rbtn1.pack(anchor = 'w')


root.mainloop()
