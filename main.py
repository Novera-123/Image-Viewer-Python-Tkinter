import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os


root = tk.Tk()
root.title("Image Viewer")
root.geometry("800x600")


image_paths = []
current_image_index = 0
current_image = None


def load_image(file_path):
    global current_image
    current_image = Image.open(file_path)
    current_image.thumbnail((800, 600))
    photo = ImageTk.PhotoImage(current_image)
    img_label.config(image=photo)
    img_label.image = photo


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        load_image(file_path)


def open_directory():
    global image_paths, current_image_index
    dir_path = filedialog.askdirectory()
    if dir_path:
        image_paths = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        image_paths.sort()
        current_image_index = 0
        if image_paths:
            load_image(image_paths[current_image_index])


def next_image():
    global current_image_index
    if image_paths:
        current_image_index = (current_image_index + 1) % len(image_paths)
        load_image(image_paths[current_image_index])


def prev_image():
    global current_image_index
    if image_paths:
        current_image_index = (current_image_index - 1) % len(image_paths)
        load_image(image_paths[current_image_index])


def zoom(event):
    if current_image:
        
        x, y = event.x, event.y
        width, height = current_image.size
        zoom_factor = 1.5  # Reduced zoom factor
        box_size = 200  # Increased size of the zoomed area

        # Calculate the bounding box for the zoomed area
        left = max(0, min(width - box_size, int(x * zoom_factor) - box_size // 2))
        upper = max(0, min(height - box_size, int(y * zoom_factor) - box_size // 2))
        right = left + box_size
        lower = upper + box_size

        # Crop and resize the zoomed area
        cropped_image = current_image.crop((left, upper, right, lower))
        resized_image = cropped_image.resize((800, 600), Image.LANCZOS)

        # Display the zoomed area
        photo = ImageTk.PhotoImage(resized_image)
        img_label.config(image=photo)
        img_label.image = photo

# Function to reset the image to its original state
def reset_image(event):
    if current_image:
        photo = ImageTk.PhotoImage(current_image)
        img_label.config(image=photo)
        img_label.image = photo

# Create a label to display the image
img_label = tk.Label(root)
img_label.pack(expand=True)

# Bind the mouse movement to the zoom function
img_label.bind('<Motion>', zoom)

# Bind double-click event to reset the image
img_label.bind('<Double-1>', reset_image)

# Create buttons for navigation and opening images
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT)

open_dir_button = tk.Button(root, text="Open Directory", command=open_directory)
open_dir_button.pack(side=tk.LEFT)

prev_button = tk.Button(root, text="Previous", command=prev_image)
prev_button.pack(side=tk.LEFT)

next_button = tk.Button(root, text="Next", command=next_image)
next_button.pack(side=tk.LEFT)

# Run the main event loop
root.mainloop()
