import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from financial_tracker import run_finance_tracker
from price_per_hour import TaskManager
from task_tracker import TaskManager

root = Tk()

# 2. Instantiate the TaskManager class with the Tk instance as its argument
app = TaskManager(root)

# 3. Set up the window dimensions and position if needed
window_width = 800
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# 4. Start the Tkinter event loop
root.mainloop()