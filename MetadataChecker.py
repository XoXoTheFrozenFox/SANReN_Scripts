from PIL import Image
from PIL.ExifTags import TAGS
import os
from datetime import datetime

def get_image_metadata(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Extract EXIF data
        exif_data = img._getexif()

        if not exif_data:
            print("No EXIF metadata found.")
            return None

        # Convert EXIF data to a readable format
        metadata = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            # Check if the value is a date and format it
            if tag_name in ['DateTime', 'DateTimeOriginal', 'DateTimeDigitized']:
                value = format_datetime(value)
            metadata[tag_name] = value
        
        return metadata
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def format_datetime(date_str):
    """Format a datetime string from EXIF data."""
    try:
        # Parse the EXIF datetime string and format it
        dt = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
        return dt.strftime("%d-%m-%Y %H:%M")
    except ValueError:
        # Return the original string if parsing fails
        return date_str

def get_file_creation_date(file_path):
    try:
        # Get file creation time
        creation_time = os.path.getctime(file_path)
        # Convert to datetime object
        creation_date = datetime.fromtimestamp(creation_time)
        return format_datetime(creation_date.strftime("%Y:%m:%d %H:%M:%S"))
    except Exception as e:
        print(f"An error occurred while getting creation date: {e}")
        return None

def main():
    downloads_folder = os.path.expanduser("~/Downloads")
    image_filename = "input.png"  # Change this to your actual image filename
    image_path = os.path.join(downloads_folder, image_filename)

    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return

    # Get image metadata
    metadata = get_image_metadata(image_path)
    if metadata:
        print("Metadata:")
        for tag, value in metadata.items():
            print(f"{tag}: {value}")

    # Get file creation date
    creation_date = get_file_creation_date(image_path)
    if creation_date:
        print(f"Creation Date: {creation_date}")

if __name__ == "__main__":
    main()
