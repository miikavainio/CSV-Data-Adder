import tkinter as tk
from tkinter import messagebox

def show_instructions():
    instructions = (
        "NHL GameAdr\n\n"
        "Instructions:\n"
        "1. Enter the date in the format DD-MM-YYYY.\n"
        "2. Specify the start time (default is 02:00).\n"
        "3. Enter first letter of the teams and select correct.\n"
        "4. Enter scores for both home and visitor teams.\n"
        "5. Select the game status (Regulation, Overtime, Shootout).\n"
        "6. Click 'Add Game' to submit the details.\n"
        "7. All fields are mandatory.\n"
    )
    messagebox.showinfo("Instructions", instructions)

# Info button
def create_info_button(app):
    info_button = tk.Button(app, text="?", command=show_instructions)
    info_button.grid(row=8, column=0, pady=10, padx=(10, 0), sticky="w")
