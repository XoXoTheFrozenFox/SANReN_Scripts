import os
from pathlib import Path

# Dynamically find the path to the Downloads folder
downloads_folder = str(Path.home() / "Downloads")
input_file_path = os.path.join(downloads_folder, 'outputfixed.txt')
output_file_path = os.path.join(downloads_folder, 'outputdecimal.txt')

# Read the binary values from the input file
with open(input_file_path, 'r') as file:
    binary_values = file.readlines()

# Convert binary values to decimal and write to the output file
with open(output_file_path, 'w') as file:
    for binary_value in binary_values:
        # Strip any whitespace or newline characters
        binary_value = binary_value.strip()
        
        # Convert binary to decimal
        decimal_value = int(binary_value, 2)
        
        # Write the decimal value to the output file
        file.write(str(decimal_value) + '\n')

print(f"Conversion complete. Decimal values saved to {output_file_path}.")
