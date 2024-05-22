import os
import sys
import logging
from tkinter import Tk, Button, Frame
import subprocess

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

def launch_app(script_path):
    logging.info(f"Launching {script_path}")
    root.withdraw()  # Hide current Tkinter window
    subprocess.Popen([sys.executable, script_path])

def switch_to_frame(frame):
    frame.tkraise()

def exit_app():
    logging.info("Exiting Application")
    root.destroy()  # Close Tkinter window
    sys.exit()

logging.info("Starting Application")

root = Tk()
root.title("Main Menu")

frame1 = Frame(root)
frame1.pack(padx=20, pady=20)

button1 = Button(frame1, text="Launch App 1", command=lambda: launch_app("financial_tracker.py"))
button1.pack(fill="x", padx=10, pady=5)

button2 = Button(frame1, text="Launch App 2", command=lambda: launch_app("price_per_hour.py"))
button2.pack(fill="x", padx=10, pady=5)

button3 = Button(frame1, text="Launch App 3", command=lambda: launch_app("task_tracker.py"))
button3.pack(fill="x", padx=10, pady=5)

exit_button = Button(frame1, text="Exit", command=exit_app)
exit_button.pack(fill="x", padx=10, pady=5)

frame2 = Frame(root)
frame2.pack(padx=20, pady=20)

# You can add more frames for different "pages" if needed

# Switching between frames
switch_to_frame(frame1)

root.mainloop()

logging.info("Application Closed")
