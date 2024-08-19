import numpy as np
from PIL import Image
import os

# Define the path to the Downloads directory
downloads_path = os.path.expanduser('~/Downloads/')

# Load images
def load_image(image_name):
    full_path = os.path.join(downloads_path, image_name)
    print(f"Loading image from: {full_path}")  # Debugging statement
    return np.array(Image.open(full_path))

# Save image
def save_image(image_array, output_name):
    full_path = os.path.join(downloads_path, output_name)
    print(f"Saving image to: {full_path}")  # Debugging statement
    Image.fromarray(image_array).save(full_path)

# Main function to compute d
def compute_d(a_name, b_name, c_name, y_name, output_name):
    # Load images
    a = load_image(a_name)
    b = load_image(b_name)
    c = load_image(c_name)
    y = load_image(y_name)
    
    # Check if all images are of the same shape
    if not (a.shape == b.shape == c.shape == y.shape):
        raise ValueError("All images must have the same dimensions.")
    
    # Perform the equation: d = y - 6a - 3b + 2c
    d = y - 6 * a - 3 * b + 2 * c
    
    # Ensure pixel values are within [0, 255]
    d = np.clip(d, 0, 255).astype(np.uint8)
    
    # Save the result image
    save_image(d, output_name)

# Example usage
compute_d('a.png', 'b.png', 'c.png', 'y.png', 'd.png')