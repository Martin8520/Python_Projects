import os
import sys
from tkinter import Tk, Button, Frame


def launch_app1():
    os.system('python financial_tracker.py')


def launch_app2():
    os.system('python price_per_hour.py')


def launch_app3():
    os.system('python task_tracker.py')


def exit_app():
    sys.exit()


root = Tk()
root.title("Main Menu")

frame = Frame(root)
frame.pack(padx=20, pady=20)

button1 = Button(frame, text="Launch App 1", command=launch_app1)
button1.pack(fill="x", padx=10, pady=5)

button2 = Button(frame, text="Launch App 2", command=launch_app2)
button2.pack(fill="x", padx=10, pady=5)

button3 = Button(frame, text="Launch App 3", command=launch_app3)
button3.pack(fill="x", padx=10, pady=5)

exit_button = Button(frame, text="Exit", command=exit_app)
exit_button.pack(fill="x", padx=10, pady=5)

root.mainloop()
