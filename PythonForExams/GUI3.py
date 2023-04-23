import tkinter as tk

# Create a new window
window = tk.Tk()

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="Hello, " + entry.get() + "!")

# Create a label widget
label = tk.Label(window, text="Enter your name:")

# Create an entry widget
entry = tk.Entry(window)

# Create a button widget
button = tk.Button(window, text="Say Hello", command=button_click)

# Create a checkbutton widget
checkbutton = tk.Checkbutton(window, text="Check me out!")

# Create a radio button widget
radio1 = tk.Radiobutton(window, text="Option 1")
radio2 = tk.Radiobutton(window, text="Option 2")
radio3 = tk.Radiobutton(window, text="Option 3")

# Create a listbox widget
listbox = tk.Listbox(window)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")

# Create a scrollbar widget
scrollbar = tk.Scrollbar(window)

# Attach the scrollbar to the listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a text widget
text = tk.Text(window)

# Add some text to the text widget
text.insert(tk.END, "This is a text widget.")

# Create a menu widget
menu = tk.Menu(window)
menu.add_command(label="File")
menu.add_command(label="Edit")
menu.add_command(label="Help")

# Add the menu to the window
window.config(menu=menu)

# Place the widgets on the window using grid layout
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
checkbutton.grid(row=1, column=0)
radio1.grid(row=1, column=1)
radio2.grid(row=1, column=2)
radio3.grid(row=1, column=3)
listbox.grid(row=2, column=0)
scrollbar.grid(row=2, column=1, sticky="NS")
text.grid(row=2, column=2, columnspan=2)

# Start the event loop
window.mainloop()


