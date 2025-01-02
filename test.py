import tkinter as tk
from tkinter import ttk

# Define the data for fruits and their corresponding options
fruit_options = {
    "Apple": ["Red", "Green", "Yellow"],
    "Banana": ["Yellow", "Green"],
    "Grapes": ["Green", "Red", "Purple"],
    "Orange": ["Navel", "Blood Orange", "Mandarin"]
}

# Create the main window
root = tk.Tk()
root.title("Interactive Dropdown")

# Function to update the second dropdown based on the first dropdown selection
def update_options(event):
    selected_fruit = fruit_combobox.get()
    # Clear the current options in the second dropdown
    option_combobox.set('')
    # Populate the second dropdown with the options related to the selected fruit
    option_combobox['values'] = fruit_options.get(selected_fruit, [])

# Create and pack the first dropdown (fruits)
fruit_label = tk.Label(root, text="Select a fruit:")
fruit_label.pack()

fruit_combobox = ttk.Combobox(root, values=list(fruit_options.keys()))
fruit_combobox.pack()
fruit_combobox.bind("<<ComboboxSelected>>", update_options)

# Create and pack the second dropdown (fruit options)
option_label = tk.Label(root, text="Select an option:")
option_label.pack()

option_combobox = ttk.Combobox(root)
option_combobox.pack()

# Start the main loop
root.mainloop()
