import os

def find_hidden_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return []
    
    # List to store hidden file paths
    hidden_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            # Print all files
            print(f"Found file: {file_path}")
            
            # Check if the file is hidden
            if name.startswith('.'):
                hidden_files.append(file_path)
    
    return hidden_files

def main():
    # Define the path to the "resources" directory in the "Downloads" folder
    downloads_folder = os.path.expanduser('~/Downloads')
    resources_folder = os.path.join(downloads_folder, 'resources')

    # Find hidden files in the resources directory
    hidden_files = find_hidden_files(resources_folder)
    
    if hidden_files:
        print("\nHidden files found:")
        for file in hidden_files:
            print(file)
        
        # Write hidden files to a text file
        hidden_files_path = os.path.join(downloads_folder, 'hidden_files.txt')
        with open(hidden_files_path, 'w') as f:
            for file in hidden_files:
                f.write(f"{file}\n")
        
        print(f"\nHidden files list written to: {hidden_files_path}")
    else:
        print("\nNo hidden files found.")

if __name__ == "__main__":
    main()