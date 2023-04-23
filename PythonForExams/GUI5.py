import tkinter as tk

# Create a new window
window = tk.Tk()

# Create a Listbox widget
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)

# Add items to the Listbox
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
listbox.insert(2, "Item 3")
listbox.insert(3, "Item 4")
listbox.insert(4, "Item 5")

# Pack the Listbox widget onto the window
listbox.pack()

# Create a function to print the selected items
def print_selected_items():
    # Get the selected items from the Listbox
    selected_items = listbox.curselection()
    # Print the selected items
    for item in selected_items:
        print(listbox.get(item))

# Create a button to trigger the print_selected_items function
button1 = tk.Button(window, text="Print selected items", command=print_selected_items)
button1.pack()

# Create a function to delete the selected items
def delete_selected_items():
    # Get the selected items from the Listbox
    selected_items = listbox.curselection()
    # Delete the selected items from the Listbox
    for item in reversed(selected_items):
        listbox.delete(item)

# Create a button to trigger the delete_selected_items function
button2 = tk.Button(window, text="Delete selected items", command=delete_selected_items)
button2.pack()

# Start the event loop
window.mainloop()
