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

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
app.geometry(f"{window_width}x{window_height}+{x}+{y}")
# https://www.geeksforgeeks.org/how-to-center-a-window-on-the-screen-in-tkinter/

# Starts the loop
app.mainloop()