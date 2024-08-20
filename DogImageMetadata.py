import exifread
import os

def extract_metadata(image_path):
    """Extract metadata from an image file."""
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
        
        if not tags:
            print("No EXIF metadata found.")
            return
        
        for tag in tags.keys():
            print(f"{tag}: {tags[tag]}")
    except Exception as e:
        print(f"Error reading metadata: {e}")

def main():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    image_path = os.path.join(downloads_folder, 'dogs.jpg')
    
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return

    extract_metadata(image_path)

if __name__ == "__main__":
    main()