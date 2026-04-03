import tkinter as tk
import ttkbootstrap as ttk
from pathlib import Path
import json
import os


# Some basic code to get it to read the info based on the press of a button
# Make sure to get this to do it on its own.
def read():
    file_path = Path(__file__).resolve().parent.parent / "config.json"
    with open(file_path, 'r') as file:
              data = json.load(file)
              print(data)

              # Insert values into the boxes
              input_welcome_id.insert(0, data.get("welcomeId", ""))
              input_general_id.insert(0, data.get("generalId", ""))
              input_log_id.insert(0, data.get("logId", ""))

# TODO
def save():
    pass


# TKinter
# Window
window = ttk.Window(themename = 'journal')
window.title('Bot.exe')
window
window.geometry('500x500')

# Render input boxes
# Welcome ID
text_welcome_id = ttk.Label(text = 'Welcome ID')
text_welcome_id.pack()
input_welcome_id = ttk.Entry(window)
input_welcome_id.pack(pady = 10)

# General ID
text_general_id = ttk.Label(text = 'General ID')
text_general_id.pack()
input_general_id = ttk.Entry(window)
input_general_id.pack(pady = 10)

# Log ID
text_log_id = ttk.Label(text = 'Log ID')
text_log_id.pack()
input_log_id = ttk.Entry(window)
input_log_id.pack(pady = 10)

# Read button
button_frame = ttk.Frame(window)
read = ttk.Button(button_frame, text = 'Read info', command = read)
button_frame.pack()
read.pack(side = 'left', padx = 10, pady = 10)
# Save button
button_frame = ttk.Frame(window)
save = ttk.Button(button_frame, text = 'Save info', command = save)
button_frame.pack()
save.pack(side = 'left', padx = 10, pady = 10)


# TODO Start button

# Run the window/render it
window.mainloop()