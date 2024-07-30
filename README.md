# Tkinter Image Viewer

This is a simple image viewer application built using Tkinter and Pillow (PIL) in Python. The application allows you to open, view, and navigate through images. It also features a zoom-in effect when hovering over the image and resets to the original view on double-click.

## Features

- Open individual image files.
- Open and navigate through images in a directory.
- Zoom into the image on mouse hover.
- Reset the image to its original state on double-click.
- Navigate to the next and previous images in a directory.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pillow library

## Installation

1. **Clone the repository or download the source code.**

   ```bash
   git clone https://github.com/yourusername/tkinter-image-viewer.git
   cd tkinter-image-viewer

  ## 2. Install the Required Python Packages 
  ```bash
pip install pillow
```
## Usage

Run the application.

bash
Copy code
python image_viewer.py
Use the application.

- Click Open Image to open a single image file.
- Click Open Directory to select a directory and load the first image.
- Use Previous and Next buttons to navigate through images in the selected directory.
- Hover over the image to zoom in.
- Double-click on the image to reset it to its original state.

## Code Overview

- load_image(file_path): Loads and displays the specified image file.
- open_image(): Opens a file dialog to select a single image file.
- open_directory(): Opens a directory dialog to select a directory containing images.
- next_image(): Loads the next image in the directory.
- prev_image(): Loads the previous image in the directory.
- zoom(event): Handles mouse movement to zoom into the image.
- reset_image(event): Resets the image to its original state on double-click.

### Copy the code in your Python IDE and see how it works.
   
