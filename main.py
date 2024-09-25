import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Creates the window, title and size
app = tk.Tk()
app.title("NHL GameAdr")

# Centering the window
window_width = 400
window_height = 315
app.geometry(f"{window_width}x{window_height}")
app.resizable(False, False)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
# https://www.geeksforgeeks.org/how-to-center-a-window-on-the-screen-in-tkinter/


# Input fields

tk.Label(app, text="Date (DD-MM-YYYY)").grid(row=0, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=0, column=1, columnspan=2)

tk.Label(app, text="Start Time (HH:MM)").grid(row=1, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=1, column=1, columnspan=2)

tk.Label(app, text="Home Team").grid(row=2, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=2, column=1, columnspan=2)

tk.Label(app, text="Visitor Team").grid(row=3, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=3, column=1, columnspan=2)

tk.Label(app, text="Home Score").grid(row=4, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=4, column=1, columnspan=2)

tk.Label(app, text="Visitor Score").grid(row=5, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=5, column=1, columnspan=2)

tk.Label(app, text="Status").grid(row=6, column=0, sticky="e")
date_entry = tk.Entry(app)
date_entry.grid(row=6, column=1, columnspan=2)

# Centering the input fields, and keep it where they are
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)


# Starts the loop
app.mainloop()