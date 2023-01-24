import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter")
        self.geometry("400x600")
        self.image = None

        self.browse_button = tk.Button(self, text="Load Image", command=self.browse_image)
        self.browse_button.pack()

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.save_button = tk.Button(self, text="Convert Image Ke", command=self.save_image)
        self.save_button.pack()

    def browse_image(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.original_image = Image.open(self.filename)
        self.original_image = ImageTk.PhotoImage(self.original_image)
        self.image_label.configure(image=self.original_image)

    def save_image(self):
        try:
            file_format = [("PNG", "*.png"), ("JPEG", "*.jpg"), ("GIF", "*.gif"), ("All Files", "*.*")]
            save_file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_format)
            image = Image.open(self.filename)
            image.save(save_file)
            self.status_label = tk.Label(self, text="Image Berhasil Di Convert!")
            self.status_label.pack()
        except:
            self.status_label = tk.Label(self, text="Gagal!!! Silahkan Ulangi!!!.")
            self.status_label.pack()


if __name__ == "__main__":
    converter = ImageConverter()
    converter.mainloop()
