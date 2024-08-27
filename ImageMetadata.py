import os
from PIL import Image
import shutil

# Path to the source folder and target folders
source_folder = os.path.expanduser("~/Downloads/screenshots")
repaired_folder = os.path.expanduser("~/Downloads/screenshots1")
failed_folder = os.path.expanduser("~/Downloads/screenshots2")

# Create target folders if they do not exist
os.makedirs(repaired_folder, exist_ok=True)
os.makedirs(failed_folder, exist_ok=True)

def repair_image_metadata(file_path, repaired_file_path):
    try:
        with Image.open(file_path) as img:
            # Save the repaired image to the specified folder
            img.save(repaired_file_path)
            print(f"Repaired: {file_path} -> {repaired_file_path}")
            return True
    except Exception as e:
        print(f"Failed to repair {file_path}: {e}")
        return False

def scan_and_repair_images(source_folder, repaired_folder, failed_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                repaired_file_path = os.path.join(repaired_folder, file)
                if repair_image_metadata(file_path, repaired_file_path):
                    # If repaired successfully, delete the original file
                    os.remove(file_path)
                    # If repair failed, move the original file to the failed folder
                    failed_file_path = os.path.join(failed_folder, file)
                    shutil.move(file_path, failed_file_path)

if __name__ == "__main__":
    scan_and_repair_images(source_folder, repaired_folder, failed_folder)
