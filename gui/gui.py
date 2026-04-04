import ttkbootstrap as ttk
from pathlib import Path
import json
import signal
import subprocess
import os

# TODO Find a way to get the bot to terminate

Started = False

# By default the app should NOT be running.
process = None
running = False
is_running_text = 'Not running'

# Some basic code to get it to read the info based on the press of a button
try:
    # Config file path
    file_path = Path(__file__).resolve().parent.parent / "config.json"
except:
      print('Error. File path could not be found.')
# Make sure to get this to do it on its own.
def read():
    try: 
        with open(file_path, 'r') as file:
            data = json.load(file)

        input_welcome_id.delete(0, 'end')
        input_general_id.delete(0, 'end')
        input_log_id.delete(0, 'end')

        input_welcome_id.insert(0, data.get("welcomeId", ""))
        input_general_id.insert(0, data.get("generalId", ""))
        input_log_id.insert(0, data.get("logId", ""))

    except Exception as e:
        print(f'Error: {e}')

# TODO
def save():
    new_welcome_id = input_welcome_id.get()
    new_general_id = input_general_id.get()
    new_log_id = input_log_id.get()
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            data['welcomeId'] = new_welcome_id
            data['generalId'] = new_general_id
            data['logId'] = new_log_id

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print('Info written successfully!')           
    except Exception as e:
         print(f'Error: {e}')

def start_stop():
    global process, running, is_running_text
    try:
        if not running == True:
            process = subprocess.Popen(
                ['python', str(Path(__file__).parent.parent / 'main.py')],
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            running = True
            is_running_text = 'Now running!'
        else:
            subprocess.call(['taskkill', '/F', '/T', '/PID', str(process.pid)])
            process = None
            running = False
            is_running_text = "Not running"

        text_running.config(text=is_running_text)
    except Exception as e:
         print(f'An error occured! {e}')
        
          
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

# Save button
button_frame = ttk.Frame(window)
save_button= ttk.Button(button_frame, text = 'Save info', command = save)
button_frame.pack()
save_button.pack(side = 'left', padx = 10, pady = 10)

# Start/stop button
button_frame = ttk.Frame(window)
start_stop_button = ttk.Button(button_frame, text = 'Start/Stop', command = start_stop)
button_frame.pack()
start_stop_button.pack(side = 'left', padx = 10, pady = 10)
text_running = ttk.Label(text = is_running_text)
text_running.pack()

# Run the window/render it
window.after(100, read)
window.mainloop()