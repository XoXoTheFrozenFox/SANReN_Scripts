import json
import os
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

def extract_png_metadata(png_file):
    metadata = {}
    
    try:
        # Open the PNG image file
        with Image.open(png_file) as img:
            # Extract basic image properties
            metadata['Format'] = img.format
            metadata['Mode'] = img.mode
            metadata['Size'] = img.size
            
            # Extract image info, including comments and other metadata
            info = img.info
            metadata['Image Info'] = info
            
            # Extract EXIF data if available (though uncommon for PNG)
            exif_data = {}
            if 'exif' in info:
                exif = img._getexif()
                if exif:
                    for tag, value in exif.items():
                        tag_name = TAGS.get(tag, tag)
                        exif_data[tag_name] = value
            metadata['EXIF Data'] = exif_data
            
            # Extract comments if available
            if 'comment' in info:
                metadata['Comment'] = info['comment']
            elif 'Description' in info:
                metadata['Comment'] = info['Description']
            else:
                metadata['Comment'] = "No comments found"

    except UnidentifiedImageError:
        print(f"Warning: Could not identify image file {png_file}.")
    except Exception as e:
        print(f"Error processing {png_file}: {e}")
    
    return metadata

def save_metadata_to_json(metadata, json_file):
    # Write the metadata to a JSON file
    with open(json_file, 'w') as json_f:
        json.dump(metadata, json_f, indent=4)

if __name__ == "__main__":
    # Define the directory containing PNG images
    png_dir = r'C:\Users\S_CSIS-PostGrad\Downloads\screenshots\screenshots'
    output_dir = os.path.join(png_dir, 'metadata')
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each file in the directory
    for filename in os.listdir(png_dir):
        if filename.lower().endswith('.png'):
            # Construct full file path
            png_file = os.path.join(png_dir, filename)
            
            # Extract metadata
            metadata = extract_png_metadata(png_file)
            
            if metadata:  # Only save if metadata is found
                # Save metadata to JSON file
                json_filename = f"{os.path.splitext(filename)[0]}_metadata.json"
                json_file = os.path.join(output_dir, json_filename)
                save_metadata_to_json(metadata, json_file)
                
                print(f"Metadata extracted and saved to {json_file}")
            else:
                print(f"No metadata found for {png_file}.")
