from PIL import Image
import numpy as np
import os

def decode_lsb(image_path):
    """Decode a message hidden in the least significant bits of the image."""
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)
    
    binary_message = ''
    for row in pixels:
        for pixel in row:
            for color in pixel:
                binary_message += str(color & 1)
    
    # Convert binary message to text
    def binary_to_text(binary_str):
        binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        return ''.join(ascii_characters)
    
    message = binary_to_text(binary_message)
    return message

def main():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    image_path = os.path.join(downloads_folder, 'dogs.jpg')
    
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    hidden_message = decode_lsb(image_path)
    print(f"Hidden message: {hidden_message}")

if __name__ == "__main__":
    main()
