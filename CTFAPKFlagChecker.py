import os
import re

# Define the directory path
directory_path = os.path.join(os.path.expanduser("~"), "Downloads", "challenge-1")

# Output file
output_file = os.path.join(directory_path, "ctf_flags.txt")

# Regex pattern to match CTF{...}
pattern = re.compile(r'CTF')

# List to store found CTF flags along with their file paths
found_flags = []

# Walk through all files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(f"Processing file: {file_path}")
        
        # Open and read each file
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Find all matches in the content
                matches = pattern.findall(content)
                
                # Store each match along with the file path
                if matches:
                    for match in matches:
                        found_flags.append(f"Found in {file_path}: {match}")
                        print(f"Flag found: {match}")
                else:
                    print(f"No flags found in {file_path}")
        except (UnicodeDecodeError, IOError) as e:
            print(f"Skipping file {file_path} due to error: {e}")

# Write all found flags and their file paths to the output file
if found_flags:
    with open(output_file, 'w', encoding='utf-8') as f:
        for flag in found_flags:
            f.write(f"{flag}\n")
    print(f"Found flags and their locations have been saved to: {output_file}")
else:
    print("No flags were found in any files.")
