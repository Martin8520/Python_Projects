import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


class BatchImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Image Processor")
        self.root.geometry("600x400")

        self.upload_button = tk.Button(self.root, text="Upload Images", command=self.upload_images)
        self.upload_button.pack(pady=20)

        self.resize_label = tk.Label(self.root, text="Resize (Width x Height):")
        self.resize_label.pack()
        self.width_entry = tk.Entry(self.root, width=10)
        self.width_entry.pack(side=tk.LEFT, padx=5)
        self.height_entry = tk.Entry(self.root, width=10)
        self.height_entry.pack(side=tk.LEFT, padx=5)

        self.crop_label = tk.Label(self.root, text="Crop (Left, Top, Right, Bottom):")
        self.crop_label.pack()
        self.left_entry = tk.Entry(self.root, width=5)
        self.left_entry.pack(side=tk.LEFT, padx=5)
        self.top_entry = tk.Entry(self.root, width=5)
        self.top_entry.pack(side=tk.LEFT, padx=5)
        self.right_entry = tk.Entry(self.root, width=5)
        self.right_entry.pack(side=tk.LEFT, padx=5)
        self.bottom_entry = tk.Entry(self.root, width=5)
        self.bottom_entry.pack(side=tk.LEFT, padx=5)

        self.rename_label = tk.Label(self.root, text="Rename Prefix:")
        self.rename_label.pack()
        self.rename_entry = tk.Entry(self.root)
        self.rename_entry.pack()

        self.process_button = tk.Button(self.root, text="Process Images", command=self.process_images)
        self.process_button.pack(pady=20)

        self.images = []

    def upload_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_paths:
            self.images = file_paths
            messagebox.showinfo("Success", f"Uploaded {len(self.images)} images.")

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
                if width and height:
                    img = img.resize((int(width), int(height)))

                if left and top and right and bottom:
                    img = img.crop((int(left), int(top), int(right), int(bottom)))

                base, ext = os.path.splitext(image_path)
                if rename_prefix:
                    new_name = f"{rename_prefix}_{i + 1}{ext}"
                else:
                    new_name = f"{base}_processed{ext}"

                img.save(new_name)

        messagebox.showinfo("Success", "Images processed successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BatchImageProcessorApp(root)
    root.mainloop()
