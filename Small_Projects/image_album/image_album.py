import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
from wand.image import Image as WandImage


class ImageAlbumApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Album Viewer")
        self.images = []
        self.current_image_index = 0

        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.btn_prev = tk.Button(self.master, text="<< Prev", command=self.prev_image)
        self.btn_prev.pack(side=tk.LEFT, padx=10)

        self.btn_next = tk.Button(self.master, text="Next >>", command=self.next_image)
        self.btn_next.pack(side=tk.RIGHT, padx=10)

        self.btn_upload = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.btn_upload.pack(side=tk.BOTTOM, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.eps")])
        if file_path:
            if file_path.lower().endswith('.eps'):
                try:
                    with WandImage(filename=file_path, resolution=300) as img:
                        img.format = 'png'
                        png_data = img.make_blob(format='png')
                    image = Image.open(BytesIO(png_data))
                    self.images.append(image)
                    self.show_current_image()
                except Exception as e:
                    print("Error converting EPS:", e)
            else:
                image = Image.open(file_path)
                self.images.append(image)
                self.show_current_image()

    def show_current_image(self):
        if self.images:
            img = self.images[self.current_image_index]
            width, height = img.size
            max_width = self.master.winfo_width()
            max_height = self.master.winfo_height() - 50
            scale_factor = min(max_width / width, max_height / height)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            img = img.resize((new_width, new_height))
            self.photo_image = ImageTk.PhotoImage(img)
            self.canvas.delete("all")
            self.canvas.create_image((max_width - new_width) // 2, (max_height - new_height) // 2,
                                     anchor=tk.NW, image=self.photo_image)
            self.master.title(
                "Image Album Viewer - Image {} of {}".format(self.current_image_index + 1, len(self.images)))

    def prev_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_current_image()

    def next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_current_image()


def main():
    os.environ["PATH"] += os.pathsep + 'C:\Program Files\gs\gs10.03.0\bin'
    root = tk.Tk()
    app = ImageAlbumApp(root)
    root.geometry("800x600")
    root.mainloop()


if __name__ == "__main__":
    main()
