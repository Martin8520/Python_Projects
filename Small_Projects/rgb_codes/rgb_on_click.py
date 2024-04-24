import threading
import tkinter as tk
from tkinter import messagebox, ttk

import pyperclip
from PIL import ImageGrab
from pynput import keyboard
from pynput.mouse import Controller
from pynput.mouse import Listener

sampling_mode = "RGB"
last_color = None
img_label = None
mouse_controller = Controller()
listener = None

def on_click(x, y, button, pressed):
    global last_color

    if pressed:
        try:
            color = ImageGrab.grab().getpixel((x, y))

            if sampling_mode == "RGB":
                color_str = f"{color[0]}, {color[1]}, {color[2]}"
            else:
                c, m, y, k = rgb_to_cmyk(*color)
                color_str = f"{int(c * 100):d}%, {int(m * 100):d}%, {int(y * 100):d}%, {int(k * 100):d}%"

            if color_str != last_color:
                last_color = color_str
                pyperclip.copy(color_str)
                update_label(f"{sampling_mode}: {color_str}")

        except IndexError:
            pass
        except Exception as e:
            show_error(e)

def on_release(key):
    if key == keyboard.Key.esc:
        stop_listener()
        return False

def switch_mode(mode):
    global sampling_mode
    sampling_mode = mode
    update_label("Click anywhere on the screen to get RGB" if sampling_mode == "RGB" else "Click anywhere on the screen to get CMYK")

def rgb_to_cmyk(r, g, b):
    c = 1 - (r / 255)
    m = 1 - (g / 255)
    y = 1 - (b / 255)

    min_cmy = min(c, m, y)
    if min_cmy == 1:
        return 0, 0, 0, 100
    else:
        k = min_cmy
        c = (c - k) / (1 - k)
        m = (m - k) / (1 - k)
        y = (y - k) / (1 - k)
        return c, m, y, k

def update_label(text):
    img_label.config(text=text)

def show_error(error):
    messagebox.showerror("Error", f"An error occurred: {error}")

def start_listener():
    global listener
    listener = Listener(on_click=on_click)
    listener.start()

def stop_listener():
    global listener
    if listener:
        listener.stop()

def stop_program():
    stop_listener()
    exit()

def start_tkinter():
    root = tk.Tk()
    root.title("Color Extractor")
    root.geometry("400x100")
    root.protocol("WM_DELETE_WINDOW", stop_program)

    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    sampling_mode_menu = ttk.Combobox(top_frame, values=["RGB", "CMYK"], state="readonly")
    sampling_mode_menu.current(0)
    sampling_mode_menu.bind("<<ComboboxSelected>>", lambda event: switch_mode(sampling_mode_menu.get()))
    sampling_mode_menu.pack(side=tk.LEFT, padx=10, pady=10)

    global img_label
    img_label = tk.Label(root, text="Click anywhere on the screen to get RGB")
    img_label.pack(padx=10, pady=10)

    root.mainloop()

threading.Thread(target=start_listener, daemon=True).start()

start_tkinter()
