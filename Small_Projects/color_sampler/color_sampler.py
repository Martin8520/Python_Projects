import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


class ColorPaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Palette Generator")
        self.root.geometry("500x400")

        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=20)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.num_colors_label = tk.Label(self.root, text="Number of Colors:")
        self.num_colors_label.pack()

        self.num_colors_entry = tk.Entry(self.root)
        self.num_colors_entry.pack()
        self.num_colors_entry.insert(0, "5")

        self.generate_button = tk.Button(self.root, text="Generate Palette", command=self.generate_palette)
        self.generate_button.pack(pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            self.image_path = file_path
            img = Image.open(self.image_path)
            img.thumbnail((200, 200))
            self.img = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.img)

    def get_colors(self, image, num_colors):
        small_image = image.resize((100, 100))
        result = small_image.getcolors(10000)
        result = sorted(result, reverse=True, key=lambda x: x[0])
        colors = [color[1] for color in result[:num_colors]]
        return colors

    def plot_colors(self, colors):
        fig, ax = plt.subplots(1, len(colors), figsize=(15, 5), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
        for sp, color in zip(ax, colors):
            sp.imshow(np.ones((10, 10, 3), dtype=np.uint8) * np.array(color, dtype=np.uint8)[None, None, :])
        plt.show()

    def generate_palette(self):
        if hasattr(self, 'image_path'):
            num_colors = int(self.num_colors_entry.get())
            image = Image.open(self.image_path)
            colors = self.get_colors(image, num_colors)
            self.plot_colors(colors)
        else:
            tk.messagebox.showerror("Error", "Please upload an image first.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPaletteApp(root)
    root.mainloop()
