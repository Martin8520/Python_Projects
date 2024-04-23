import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

pil_image = None

def open_image():
    global img_label, canvas, img, image_loaded, pil_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        try:
            pil_image = Image.open(file_path)
            img = ImageTk.PhotoImage(pil_image)
            canvas.config(width=img.width(), height=img.height())
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            img_label.config(text="Click on the image to get RGB")
            image_loaded = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

def get_rgb(event):
    global img_label, image_loaded, pil_image

    try:
        if image_loaded and pil_image is not None:  # Check if pil_image is not None
            # Get the coordinates of the event
            x, y = event.x, event.y
            # Calculate the scaling factor for the coordinates
            scale_x = pil_image.width / canvas.winfo_width()
            scale_y = pil_image.height / canvas.winfo_height()
            # Adjust the coordinates based on the scaling factor
            x = int(x * scale_x)
            y = int(y * scale_y)
            # Get the RGB value of the pixel
            rgb = pil_image.getpixel((x, y))
            r, g, b = [val for val in rgb]
            img_label.config(text=f"RGB: {r}, {g}, {b}")
        else:
            messagebox.showerror("Error", "Please open an image first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def resize_image():
    global pil_image, img
    if pil_image is not None:  # Check if pil_image is not None
        window_width = root.winfo_width() - 20  # -20 for padding
        window_height = root.winfo_height() - 20  # -20 for padding

        # Calculate new width and height based on the aspect ratio
        aspect_ratio = pil_image.width / pil_image.height
        new_width = window_width
        new_height = int(window_width / aspect_ratio)
        if new_height > window_height:
            new_height = window_height
            new_width = int(window_height * aspect_ratio)

        # Resize the image
        pil_image_resized = pil_image.resize((new_width, new_height))

        img = ImageTk.PhotoImage(pil_image_resized)
        canvas.config(width=new_width, height=new_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img


def on_resize(event):
    resize_image()

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
root.bind("<Configure>", on_resize)

root.mainloop()
