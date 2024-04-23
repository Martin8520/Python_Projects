import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def open_image():
    global img_label, canvas, img, image_loaded, pil_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        try:
            pil_image = Image.open(file_path)
            img = ImageTk.PhotoImage(pil_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            canvas.config(width=img.width(), height=img.height())
            canvas.image = img
            img_label.config(text="Click on the image to get RGB")
            image_loaded = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")


def get_rgb(event):
    global img_label, image_loaded, pil_image

    try:
        if image_loaded:
            x, y = event.x, event.y
            rgb = pil_image.getpixel((x, y))
            r, g, b = [val for val in rgb]
            img_label.config(text=f"RGB: {r}, {g}, {b}")
        else:
            messagebox.showerror("Error", "Please open an image first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Color Extractor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

img_label = tk.Label(frame, text="Click on the image to get RGB")
img_label.pack(side=tk.RIGHT)

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

image_loaded = False

canvas.bind("<Button-1>", get_rgb)

root.mainloop()
