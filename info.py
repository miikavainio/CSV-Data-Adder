import tkinter as tk
from tkinter import messagebox

def show_instructions():
    instructions = (
        "NHL GameAdr\n\n"
        "Instructions:\n"
        "1. Enter the date in the format DD-MM-YYYY.\n"
        "2. Specify the start time (default is 02:00).\n"
    )
    messagebox.showinfo("Instructions", instructions)

# Info button
def create_info_button(app):
    info_button = tk.Button(app, text="?", command=show_instructions)
    info_button.grid(row=8, column=0, pady=10, padx=(10, 0), sticky="w")
