import tkinter as tk



def erase():
    lvar.set('')
def write_text():
    lvar.set('Label done')


root=tk.Tk()
root.resizable(0,0)
root.title('-Basic GUI 2-')
root.geometry('400x400')
frame = tk.Frame(root)
frame.pack()
lvar = tk.StringVar()
lanel1 = tk.Label(root,width=8,height=5,bg='white',fg='red',textvariable=lvar)
lanel1.pack(side='bottom')
btn1 = tk.Button(frame,text='Hello',font=('Arial Bold',20),command=write_text,padx=10)
btn1.pack(side=tk.LEFT)

exitbtn = tk.Button(frame,text='Exit',font=('Arial Bold',20),bg='white',fg='red',command=erase)
exitbtn.pack(side=tk.RIGHT)

listbox1 = tk.Listbox(root,selectmode=tk.MULTIPLE)
listbox1.insert(0,'item 1')
listbox1.insert(1,'item 2')
listbox1.insert(2,'item 3')
listbox1.insert(3,'item 4')
listbox1.insert(4,'item 5')

listbox1.pack()

def print_selected_text():
    selected = listbox1.curselection()
    for item in selected:
        print(listbox1.get(item))
def erase1():
    selected=listbox1.curselection()
    for item in reversed(selected):
        listbox1.delete(item)
    
btn4 = tk.Button(frame,text='Hello',font=('Arial Bold',20),command=print_selected_text,padx=10)
btn4.pack(side=tk.LEFT)
exit1btn = tk.Button(frame,text='Exit',font=('Arial Bold',20),bg='white',fg='red',command=erase1)
exit1btn.pack(side=tk.RIGHT)

root.mainloop()
