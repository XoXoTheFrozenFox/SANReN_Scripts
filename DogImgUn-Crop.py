from PIL import Image, ImageOps
import exifread
import os

def read_exif_metadata(image_path):
    """Read the EXIF metadata from an image file."""
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
    return tags

def get_original_dimensions(tags):
    """Extract original dimensions from EXIF metadata, if available."""
    try:
        # Example EXIF tags for original dimensions
        width = tags.get('EXIF ExifImageWidth')
        height = tags.get('EXIF ExifImageLength')
        if width and height:
            return int(width.values), int(height.values)
    except (AttributeError, ValueError):
        pass
    return None

def uncrop_image(image_path, output_path, original_dimensions):
    """Uncrop an image to its original dimensions."""
    with Image.open(image_path) as img:
        original_width, original_height = original_dimensions
        current_width, current_height = img.size
        
        # Calculate new size
        new_width = max(original_width, current_width)
        new_height = max(original_height, current_height)
        
        # Create a new image with the original dimensions
        new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
        new_img.paste(img, (0, 0))
        
        # Save the uncropped image
        new_img.save(output_path)
        print(f"Uncropped image saved to: {output_path}")

def main():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    input_path = os.path.join(downloads_folder, 'dogs.jpg')
    output_path = os.path.join(downloads_folder, 'uncropped_dogs.jpg')

    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    # Read EXIF metadata
    tags = read_exif_metadata(input_path)

    # Extract original dimensions
    original_dimensions = get_original_dimensions(tags)
    
    if not original_dimensions:
        print("Original dimensions not found in metadata.")
        return
    
    # Uncrop the image
    uncrop_image(input_path, output_path, original_dimensions)

if __name__ == "__main__":
    main()
