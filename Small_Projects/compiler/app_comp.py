import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import json
import os

config_file = "exe_paths.json"

exe_paths = {}


def load_exe_paths():
    global exe_paths
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            exe_paths = json.load(file)
    else:
        exe_paths = {"App1": "", "App2": "", "App3": ""}


def save_exe_paths():
    with open(config_file, "w") as file:
        json.dump(exe_paths, file)


def import_exe(app_name):
    file_path = filedialog.askopenfilename(
        filetypes=[("Executable files", "*.exe")],
        title=f"Select {app_name}"
    )
    if file_path:
        exe_paths[app_name] = file_path
        save_exe_paths()
        update_run_button_text(app_name)
        messagebox.showinfo("Import Successful", f"{app_name} imported successfully!")


def run_exe(app_name):
    exe_path = exe_paths.get(app_name)
    if exe_path:
        try:
            subprocess.Popen(exe_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run {exe_path}\n{e}")
    else:
        messagebox.showwarning("Warning", f"{app_name} is not imported yet!")


def update_run_button_text(app_name):
    exe_path = exe_paths.get(app_name, "")
    if exe_path:
        exe_name = os.path.basename(exe_path)
        run_buttons[app_name].config(text=f"Run {exe_name}")
    else:
        run_buttons[app_name].config(text=f"Run {app_name}")


root = tk.Tk()
root.title("Import and Run EXE Applications")

load_exe_paths()

app_names = ["App1", "App2", "App3"]

run_buttons = {}

for app_name in app_names:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    import_button = tk.Button(frame, text=f"Import {app_name}", command=lambda name=app_name: import_exe(name))
    import_button.pack(side=tk.LEFT, padx=5)

    run_button = tk.Button(frame, text=f"Run {app_name}", command=lambda name=app_name: run_exe(name))
    run_button.pack(side=tk.LEFT, padx=5)

    run_buttons[app_name] = run_button
    update_run_button_text(app_name)

root.mainloop()
