import os
import binascii
import struct

# Define the path to the screenshots folder
screenshots_folder = os.path.join(os.path.expanduser('~'), 'Downloads', 'screenshots')

# Check if the screenshots folder exists
if not os.path.exists(screenshots_folder):
    print(f"The folder '{screenshots_folder}' does not exist.")
else:
    # Iterate through all the files in the screenshots folder
    for filename in os.listdir(screenshots_folder):
        filepath = os.path.join(screenshots_folder, filename)

        # Check if the current file is a regular file (not a directory)
        if os.path.isfile(filepath):
            print(f"Processing file: {filename}")
            with open(filepath, "rb") as f:
                misc = f.read()

            # Ensure the file is long enough to perform the slicing
            if len(misc) >= 29:
                for i in range(1024):
                    data = misc[12:16] + struct.pack('>i', i) + misc[20:29]
                    crc32 = binascii.crc32(data) & 0xffffffff
                    if crc32 == 0x932f8a6b:
                        print(f"Match found in file {filename} with index {i}")
            else:
                print(f"File {filename} is too short to process.")

# This message indicates that no matches were found
print("Processing complete. No matches found.") 