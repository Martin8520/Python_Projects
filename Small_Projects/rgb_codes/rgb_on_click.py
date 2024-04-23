import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pyperclip

pil_image = None


def open_image():
    global img_label, canvas, img, image_loaded, pil_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        try:
            pil_image = Image.open(file_path)
            resize_image()
            img = ImageTk.PhotoImage(pil_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            img_label.config(text="Click on the image to get RGB")
            image_loaded = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")


def get_rgb(event):
    global img_label, image_loaded, pil_image

    try:
        if image_loaded and pil_image is not None:
            x, y = event.x, event.y
            scale_x = pil_image.width / canvas.winfo_width()
            scale_y = pil_image.height / canvas.winfo_height()
            x = int(x * scale_x)
            y = int(y * scale_y)
            rgb = pil_image.getpixel((x, y))
            r, g, b = [val for val in rgb]
            rgb_str = f"{r}, {g}, {b}"
            img_label.config(text=f"RGB: {rgb_str}")
            pyperclip.copy(rgb_str)
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


root = tk.Tk()
root.title("Color Extractor")
root.geometry("500x500")

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(top_frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

img_label = tk.Label(top_frame, text="Click on the image to get RGB")
img_label.pack(side=tk.LEFT, padx=10, pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

image_loaded = False

canvas.bind("<Button-1>", get_rgb)
root.bind("<Configure>", on_resize)

root.mainloop()
