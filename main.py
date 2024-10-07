import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
from info import create_info_button
from teams import teams

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

##############################################################################################
# Input fields

tk.Label(app, text="Date (DD-MM-YYYY)").grid(row=0, column=0, sticky="e", padx=10, pady=5)
date_entry = tk.Entry(app)
date_entry.insert(0, datetime.now().strftime('%d-%m-%Y'))  # Default date is current day
date_entry.grid(row=0, column=1, columnspan=2, pady=5)

tk.Label(app, text="Start Time (HH:MM)").grid(row=1, column=0, sticky="e", padx=10, pady=5)
start_time_entry = tk.Entry(app)
start_time_entry.insert(0, "02:00")  # Default start time 02:00 since most of the games start then
start_time_entry.grid(row=1, column=1, columnspan=2, pady=5)

tk.Label(app, text="Home Team").grid(row=2, column=0, sticky="e", padx=10, pady=5)
date_entry = tk.Entry(app)
date_entry.grid(row=2, column=1, columnspan=2)

tk.Label(app, text="Visitor Team").grid(row=3, column=0, sticky="e", padx=10, pady=5)
date_entry = tk.Entry(app)
date_entry.grid(row=3, column=1, columnspan=2)

tk.Label(app, text="Home Score").grid(row=4, column=0, sticky="e", padx=10, pady=5)
date_entry = tk.Entry(app)
date_entry.grid(row=4, column=1, columnspan=2)

tk.Label(app, text="Visitor Score").grid(row=5, column=0, sticky="e", padx=10, pady=5)
date_entry = tk.Entry(app)
date_entry.grid(row=5, column=1, columnspan=2)



############################################################################################

# Status options
status_options = ["Regulation", "Overtime", "Shootout"]

tk.Label(app, text="Status").grid(row=6, column=0, sticky="e", padx=10, pady=5)
status_var = tk.StringVar(app)
status_var.set("Regulation")
status_combobox = ttk.Combobox(app, values=status_options, textvariable=status_var, width=17, state="readonly")
status_combobox.grid(row=6, column=1, columnspan=2, pady=5)

##################

def add_game():
    # Get the date and start time from the entries
    date_str = date_entry.get().strip()
    start_time_str = start_time_entry.get().strip()
    
    if date_str == " ":
        success_label.config(text="Date is mandatory!", fg="red")
        return

    if start_time_str == "":
        success_label.config(text="Start Time is mandatory!", fg="red")
        return
    
    if home_team_var.get() == "":
        success_label.config(text="Home Team is mandatory!", fg="red")
        return
    
    if visitor_team_var.get() == "":
        success_label.config(text="Visitor Team is mandatory!", fg="red")
        return

    if home_score_entry.get().strip() == "":
        success_label.config(text="Home Score is mandatory!", fg="red")
        return

    if visitor_score_entry.get().strip() == "":
        success_label.config(text="Visitor Score is mandatory!", fg="red")
        return

    if status_var.get() == "Select Status":
        success_label.config(text="Status is mandatory!", fg="red")
        return

    try:
        date = datetime.strptime(date_str, '%d-%m-%Y').strftime('%d-%m-%Y')
    except ValueError:
        success_label.config(text="Date format should be DD-MM-YYYY!", fg="red")
        return

    # Get the input values
    home_team = home_team_var.get()
    home_score = home_score_entry.get().strip()
    visitor_team = visitor_team_var.get()
    visitor_score = visitor_score_entry.get().strip()
    status = status_var.get()

    # Validate scores
    if not home_score.isdigit() or not visitor_score.isdigit():
        success_label.config(text="Scores must be numbers!", fg="red")
        return

    # Save to CSV
    with open('ice_hockey_games.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, start_time_str, home_team, home_score, visitor_team, visitor_score, status])

    # Clear fields after saving, keeping the date field
    start_time_entry.delete(0, tk.END)
    start_time_entry.insert(0, "02:00")  # Reset to default start time
    home_score_entry.delete(0, tk.END)
    visitor_score_entry.delete(0, tk.END)
    status_var.set("Select Status")
    home_team_var.set("")  # Reset Home Team variable
    visitor_team_var.set("")  # Reset Visitor Team variable

    # Update success message
    success_label.config(text="Game added successfully!", fg="green")


# Submit Button
submit_button = tk.Button(app, text="Add Game", command=add_game, width=17, bg="lightgreen")
submit_button.grid(row=7, column=1, columnspan=2, pady=10)

# Centering the input fields, and keep it where they are
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Info button
create_info_button(app)

# Success message label with default text "Welcome"
success_label = tk.Label(app, text="Welcome to GameAdr!", fg="blue")
success_label.grid(row=8, column=0, columnspan=3, pady=10)

# Starts the loop
app.mainloop()