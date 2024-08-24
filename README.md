---

# Image by Numbers Generator

This program automates the process of creating a "paint by numbers" style image using a regular image. It analyzes the colors in an image, simplifies them, and generates a color palette along with a corresponding outline that can be used to create a numbered painting.

## Key Features

- **Color Analysis**: The program analyzes the colors in the input image and generates a simplified color palette.
- **Palette Creation**: Based on the color analysis, it creates a color palette with the most prominent colors in the image.
- **Image Simplification**: The image is transformed into a simplified version with reduced colors, suitable for "paint by numbers" projects.
- **User Interface**: The program uses a graphical user interface (GUI) built with Tkinter, allowing users to easily interact with the tool.

## How It Works

1. **Load Image**: Users can load an image into the program using the drag-and-drop feature or through a file dialog.
2. **Color Analysis**: The program processes the image to identify the most frequent colors, filtering out those that are too insignificant or transparent.
3. **Palette Generation**: After analyzing the image, the program generates a color palette that reflects the colors in the image.
4. **Image Transformation**: The image is then transformed into a "paint by numbers" style image, where each color is assigned a number, and the corresponding palette is created.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DmitroKDS/ImageByNumbers.git
   ```

2. **Install the required packages**:
   ```bash
   pip install pillow tkinterdnd2 ttkthemes opencv-python
   ```

3. **Run the application**:
   ```bash
   python ImageByNumbers.py
   ```

## Requirements

- Python 3.x
- Pillow
- TkinterDnD2
- TTkthemes
- OpenCV

## Usage

- **Load Image**: Drag and drop an image into the application window or use the file dialog to select an image.
- **Generate Palette**: The program will analyze the image and display the resulting color palette.
- **Save or Print**: You can save the generated palette and the simplified image for later use, or print it directly for creating your "paint by numbers" project.

---
