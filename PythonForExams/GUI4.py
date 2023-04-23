import tkinter as tk


parent = tk.Tk()
parent.title('Button Tut')
parent.geometry('500x400')
def print_entry():
    print(evar.get())
btn=tk.Button(parent,text='Hello',font=('Arial',15,'bold'),bd=4,fg='red',bg='white',padx=10,pady=10,state='active',command=print_entry)
btn.pack()

check1 = tk.IntVar()
check1.set(1)
check2 = tk.IntVar()
check3 = tk.IntVar()
def chkstatus():
    print(check1.get(),check2.get(),check3.get())

f1= tk.Frame(parent,width=200,height=200,bg='cyan',bd=4)
f1.pack()

chkbtn1=tk.Checkbutton(f1,text='Vada Pav',font=('Arial',12),variable=check1,command=chkstatus)
chkbtn1.pack()


chkbtn2=tk.Checkbutton(f1,text='Samosa',font=('Arial',12),variable=check2,command=chkstatus)
chkbtn2.pack()


chkbtn3=tk.Checkbutton(f1,text='Pav Bhaji',font=('Arial',12),variable=check3,command=chkstatus)
chkbtn3.pack()

evar = tk.StringVar()
evar.set('Prasad')

entry1 = tk.Entry(parent,width=50,bd=3,show="*",textvariable=evar)
entry1.place(x=40,y=250)




parent.mainloop()
