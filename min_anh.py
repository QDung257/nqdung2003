import cv2
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Tk, Label, Button, Scale
from PIL import Image, ImageTk, ImageFilter

def open_image():
    global image_path
    image_path = filedialog.askopenfilename()
    if image_path:
        load_and_display_image(image_path)

def load_and_display_image(image_path):
    global original_image
    original_image = Image.open(image_path)
    display_image(original_image)

def display_image(image):
    photo = ImageTk.PhotoImage(image=image)
    image_label.config(image=photo)
    image_label.image = photo

def smooth_image():
    global original_image
    if original_image is None:
        messagebox.showinfo("Error", "Please open an image first.")
        return

    current_value = smoothness_slider.get()
    smoothed_image = original_image.filter(ImageFilter.GaussianBlur(radius=current_value))
    display_image(smoothed_image)

root = Tk()
root.title("Image Smoothing App")

original_image = None
image_path = None

open_button = Button(root, text="Open Image", command=open_image)
open_button.pack()

smoothness_slider = Scale(root, from_=0, to=5, orient="horizontal", label="Smoothing")
smoothness_slider.pack()

smooth_button = Button(root, text="Smooth Image", command=smooth_image)
smooth_button.pack()

image_label = Label(root)
image_label.pack()

root.mainloop()
