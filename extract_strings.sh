#!/bin/bash

# Define the directory containing the files
DIRECTORY="$HOME/Downloads/screenshots"
# Define the output file
OUTPUT_FILE="$HOME/Downloads/strings_output.txt"

# Check if the directory exists
if [ ! -d "$DIRECTORY" ]; then
  echo "Directory $DIRECTORY does not exist."
  exit 1
fi

# Check if the directory is empty
if [ -z "$(ls -A "$DIRECTORY")" ]; then
  echo "Directory $DIRECTORY is empty."
  exit 1
fi

# Create or clear the output file
: > "$OUTPUT_FILE"

# Process each file in the directory
for FILE in "$DIRECTORY"/*; do
  # Check if the file exists and is a regular file
  if [ -f "$FILE" ]; then
    echo "Processing $FILE..." >> "$OUTPUT_FILE"
    strings "$FILE" >> "$OUTPUT_FILE"
    echo -e "\n" >> "$OUTPUT_FILE"  # Add a newline for separation between files
  else
    echo "$FILE is not a valid file." >> "$OUTPUT_FILE"
  fi
done

echo "Strings have been written to $OUTPUT_FILE"
