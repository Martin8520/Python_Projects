import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pyperclip

pil_image = None
teal_dot = None
sampling_mode = "RGB"


def open_image():
    global img_label, canvas, img, image_loaded, pil_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        try:
            pil_image = Image.open(file_path)
            resize_image()
            img = ImageTk.PhotoImage(pil_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            img_label.config(text="Click on the image to get RGB" if sampling_mode == "RGB" else "Click on the image to get CMYK")
            image_loaded = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")


def get_color(event):
    global img_label, image_loaded, pil_image

    try:
        if image_loaded and pil_image is not None:
            x, y = event.x, event.y
            color = pil_image.getpixel((x, y))
            if sampling_mode == "RGB":
                color_str = f"{color[0]}, {color[1]}, {color[2]}"
            else:
                if len(color) == 3:  # RGB mode, convert to CMYK
                    r, g, b = color
                    c, m, y, k = rgb_to_cmyk(r, g, b)
                else:  # CMYK mode
                    c, m, y, k = color
                color_str = f"{int(c * 100):d}%, {int(m * 100):d}%, {int(y * 100):d}%, {int(k * 100):d}%"
            pyperclip.copy(color_str)
            img_label.config(text=f"{sampling_mode}: {color_str}")
            update_teal_dot(x, y)
        else:
            messagebox.showerror("Error", "Please open an image first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def resize_image():
    global pil_image, img
    if pil_image is not None:
        window_width = root.winfo_width() - 20
        window_height = root.winfo_height() - 20
        pil_image_resized = pil_image.copy()
        pil_image_resized.thumbnail((window_width, window_height))
        img = ImageTk.PhotoImage(pil_image_resized)
        canvas.config(width=window_width, height=window_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img


def on_resize(event):
    resize_image()


def update_cursor(event):
    global teal_dot
    if event is not None:
        x, y = event.x, event.y
        canvas.delete("teal_dot")
        canvas.create_image(x, y, image=teal_dot, anchor=tk.CENTER, tags="teal_dot")


def switch_mode(mode):
    global sampling_mode, img_label
    sampling_mode = mode
    if image_loaded and pil_image is not None:
        img_label.config(text="Click on the image to get RGB" if sampling_mode == "RGB" else "Click on the image to get CMYK")


def rgb_to_cmyk(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0

    k = 1 - max(r, g, b)
    if k == 1:  # black
        c = m = y = 0
    else:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

    return c, m, y, k


def update_teal_dot(x, y):
    global teal_dot
    teal_dot_image = Image.new("RGB", (teal_dot_size, teal_dot_size), "teal")
    teal_dot = ImageTk.PhotoImage(teal_dot_image)
    update_cursor(None)  # Refresh cursor


root = tk.Tk()
root.title("Color Extractor")
root.geometry("500x500")

teal_dot_size = 6
teal_dot_image = Image.new("RGB", (teal_dot_size, teal_dot_size), "teal")
teal_dot = ImageTk.PhotoImage(teal_dot_image)

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(top_frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

sampling_mode_menu = ttk.Combobox(top_frame, values=["RGB", "CMYK"], state="readonly")
sampling_mode_menu.current(0)  # Set default value
sampling_mode_menu.bind("<<ComboboxSelected>>", lambda event: switch_mode(sampling_mode_menu.get()))
sampling_mode_menu.pack(side=tk.LEFT, padx=10, pady=10)

img_label = tk.Label(top_frame, text="Click on the image to get RGB")
img_label.pack(side=tk.LEFT, padx=10, pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

image_loaded = False

canvas.bind("<Button-1>", get_color)
canvas.bind("<Motion>", update_cursor)
root.bind("<Configure>", on_resize)

root.mainloop()
