import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageAlbumApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Album Viewer")
        self.images = []
        self.current_image_index = 0

        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.btn_prev = tk.Button(self.master, text="<< Prev", command=self.prev_image)
        self.btn_prev.pack(side=tk.LEFT, padx=10)

        self.btn_next = tk.Button(self.master, text="Next >>", command=self.next_image)
        self.btn_next.pack(side=tk.RIGHT, padx=10)

        self.btn_upload = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.btn_upload.pack(side=tk.BOTTOM, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            image = Image.open(file_path)
            self.images.append(ImageTk.PhotoImage(image))
            self.show_current_image()

    def show_current_image(self):
        if self.images:
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.images[self.current_image_index])
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
    root = tk.Tk()
    app = ImageAlbumApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
