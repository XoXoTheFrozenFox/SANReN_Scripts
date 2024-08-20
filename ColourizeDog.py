from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
import os

def show_image(image, title):
    """Display an image with a title using matplotlib."""
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')

def process_image(image_path):
    """Apply various image processing techniques and display results."""
    # Open image
    img = Image.open(image_path)
    
    # Convert to RGB if not already
    img = img.convert('RGB')

    # 1. Original Image
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    axs[0, 0].imshow(img)
    axs[0, 0].set_title('Original')
    axs[0, 0].axis('off')

    # 2. Adjust Brightness
    enhancer = ImageEnhance.Brightness(img)
    bright_img = enhancer.enhance(2)  # Increase brightness
    axs[0, 1].imshow(bright_img)
    axs[0, 1].set_title('Brightened')
    axs[0, 1].axis('off')

    # 3. Adjust Contrast
    enhancer = ImageEnhance.Contrast(img)
    contrast_img = enhancer.enhance(2)  # Increase contrast
    axs[0, 2].imshow(contrast_img)
    axs[0, 2].set_title('High Contrast')
    axs[0, 2].axis('off')

    # 4. Grayscale
    gray_img = img.convert('L')  # Convert to grayscale
    axs[1, 0].imshow(gray_img, cmap='gray')
    axs[1, 0].set_title('Grayscale')
    axs[1, 0].axis('off')

    # 5. Inverted Colors
    img_array = np.array(img)
    inverted_img_array = 255 - img_array  # Invert colors for all channels
    inverted_img = Image.fromarray(inverted_img_array)
    axs[1, 1].imshow(inverted_img)
    axs[1, 1].set_title('Inverted Colors')
    axs[1, 1].axis('off')

    # 6. RGB Channels
    r, g, b = img.split()
    r_img = Image.merge('RGB', (r, Image.new('L', img.size), Image.new('L', img.size)))
    g_img = Image.merge('RGB', (Image.new('L', img.size), g, Image.new('L', img.size)))
    b_img = Image.merge('RGB', (Image.new('L', img.size), Image.new('L', img.size), b))
    
    # Display RGB Channels
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(r_img)
    axs[0].set_title('Red Channel')
    axs[0].axis('off')

    axs[1].imshow(g_img)
    axs[1].set_title('Green Channel')
    axs[1].axis('off')

    axs[2].imshow(b_img)
    axs[2].set_title('Blue Channel')
    axs[2].axis('off')

    plt.show()

def main():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    image_path = os.path.join(downloads_folder, 'dogs.jpg')
    
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    process_image(image_path)

if __name__ == "__main__":
    main()
