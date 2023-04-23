import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            # Do something with the content, e.g. print it
            print(content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            # Write some content to the file, e.g. "Hello, World!"
            file.write("Hello, World!")
    
root = tk.Tk()

# Create the menubar
menubar = tk.Menu(root)

# Create the "File" menu and add it to the menubar
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create the "Edit" menu and add it to the menubar
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=edit_menu)

# Configure the root window to use the menubar
root.config(menu=menubar)

# Start the main event loop
root.mainloop()
