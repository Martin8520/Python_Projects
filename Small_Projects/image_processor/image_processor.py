import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class BatchImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Image Processor")
        self.root.geometry("1200x700")

        self.upload_button = tk.Button(self.root, text="Upload Images", command=self.upload_images)
        self.upload_button.pack(pady=20)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.resize_label = tk.Label(self.frame, text="Resize (Width x Height):")
        self.resize_label.grid(row=0, column=0, sticky=tk.W)
        self.width_entry = tk.Entry(self.frame, width=10)
        self.width_entry.grid(row=0, column=1, padx=5)
        self.height_entry = tk.Entry(self.frame, width=10)
        self.height_entry.grid(row=0, column=2, padx=5)

        self.crop_label = tk.Label(self.frame, text="Crop (Left, Top, Right, Bottom):")
        self.crop_label.grid(row=1, column=0, sticky=tk.W)
        self.left_entry = tk.Entry(self.frame, width=5)
        self.left_entry.grid(row=1, column=1, padx=5)
        self.top_entry = tk.Entry(self.frame, width=5)
        self.top_entry.grid(row=1, column=2, padx=5)
        self.right_entry = tk.Entry(self.frame, width=5)
        self.right_entry.grid(row=1, column=3, padx=5)
        self.bottom_entry = tk.Entry(self.frame, width=5)
        self.bottom_entry.grid(row=1, column=4, padx=5)

        self.rename_label = tk.Label(self.frame, text="Rename Prefix:")
        self.rename_label.grid(row=2, column=0, sticky=tk.W)
        self.rename_entry = tk.Entry(self.frame, width=20)
        self.rename_entry.grid(row=2, column=1, columnspan=4, padx=5, pady=10, sticky=tk.W)

        self.process_button = tk.Button(self.root, text="Process Images", command=self.process_images)
        self.process_button.pack(pady=20)

        self.original_image_label = tk.Label(self.root)
        self.original_image_label.pack(side=tk.LEFT, padx=10)

        self.processed_image_label = tk.Label(self.root)
        self.processed_image_label.pack(side=tk.RIGHT, padx=10)

        self.default_values_label = tk.Label(self.root, text="")
        self.default_values_label.pack(pady=10)

        self.images = []

    def upload_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_paths:
            self.images = file_paths
            messagebox.showinfo("Success", f"Uploaded {len(self.images)} images.")
            self.display_original_image()

    def display_original_image(self):
        if self.images:
            self.current_image_index = 0
            self.show_image(self.images[self.current_image_index], self.original_image_label)
            self.display_default_values(self.images[self.current_image_index])

    def show_image(self, image_path, label):
        image = Image.open(image_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

    def display_default_values(self, image_path):
        with Image.open(image_path) as img:
            width, height = img.size
            self.default_values_label.config(text=f"Default Dimensions: {width} x {height}\n"
                                                  f"Default Crop: Left=0, Top=0, Right={width}, Bottom={height}")

    def process_images(self):
        if not self.images:
            messagebox.showerror("Error", "Please upload images first.")
            return

        width = self.width_entry.get()
        height = self.height_entry.get()
        left = self.left_entry.get()
        top = self.top_entry.get()
        right = self.right_entry.get()
        bottom = self.bottom_entry.get()
        rename_prefix = self.rename_entry.get()

        for i, image_path in enumerate(self.images):
            with Image.open(image_path) as img:
                try:
                    if width and height:
                        img = img.resize((int(width), int(height)))

                    if left and top and right and bottom:
                        left, top, right, bottom = map(int, [left, top, right, bottom])
                        if left < 0 or top < 0 or right > img.width or bottom > img.height:
                            raise ValueError("Crop coordinates are out of image bounds")
                        img = img.crop((left, top, right, bottom))

                    base, ext = os.path.splitext(image_path)
                    if rename_prefix:
                        new_name = f"{rename_prefix}_{i+1}{ext}"
                    else:
                        new_name = f"{base}_processed{ext}"

                    img.save(new_name)

                    if i == self.current_image_index:
                        self.show_image(new_name, self.processed_image_label)

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to process image {image_path}: {e}")
                    continue

        messagebox.showinfo("Success", "Images processed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatchImageProcessorApp(root)
    root.mainloop()
