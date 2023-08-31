import string
import random

import tkinter as tk
from tkinter import ttk

# Computes password
def generate_password(n):
    password = ""
    for i in range(n):
        random_letter = random.choice(string.ascii_letters)
        random_digit = random.choice(string.digits)
        random_punctuation = random.choice(string.punctuation)

        random_char = [random_letter, random_digit, random_punctuation]
        
        password += random.choice(random_char)
    
    return password

# Executes generates_password on button click
def on_click():
    result_text.delete("1.0", tk.END)  # Clear previous content
    selected_size = int(dropdown_var.get())  # Get the selected value from the dropdown
    result = generate_password(selected_size)  # Use the selected value as input
    result_text.insert(tk.END, result + "\n")  # Insert the result at the end of the text widget

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create drop-down menu
dropdown_frame = ttk.Frame(root)
dropdown_frame.pack(padx=10, pady=10)

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(dropdown_frame, textvariable=dropdown_var, values=[30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
dropdown.set("Select password size")
dropdown.pack()

# Create a button to trigger the method and output its result
process_button = ttk.Button(root, text="Generate Password", command=on_click)
process_button.pack()

# Create a Text widget for output
result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_text.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()