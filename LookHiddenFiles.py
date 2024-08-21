import os
import ctypes

def is_hidden(filepath):
    """Check if a file or directory is hidden in Windows."""
    attribute = ctypes.windll.kernel32.GetFileAttributesW(filepath)
    return attribute & 2  # 2 is the file attribute for hidden files/directories

def find_hidden_items(directory):
    """Find all hidden files and directories in the given directory."""
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return []
    
    hidden_items = []

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            # Check if the file is hidden
            if is_hidden(file_path):
                hidden_items.append(file_path)
        
        for name in dirs:
            dir_path = os.path.join(root, name)
            # Check if the directory is hidden
            if is_hidden(dir_path):
                hidden_items.append(dir_path)
    
    return hidden_items

def main():
    # Define the path to the "resources" directory in the "Downloads" folder
    downloads_folder = os.path.expanduser('~/Downloads')
    resources_folder = os.path.join(downloads_folder, 'challenge-1')

    # Find hidden files and directories in the resources directory
    hidden_items = find_hidden_items(resources_folder)
    
    if hidden_items:
        print("\nHidden files and directories found:")
        for item in hidden_items:
            print(item)
        
        # Write hidden items to a text file
        hidden_items_path = os.path.join(downloads_folder, 'hidden_items.txt')
        with open(hidden_items_path, 'w') as f:
            for item in hidden_items:
                f.write(f"{item}\n")
        
        print(f"\nHidden items list written to: {hidden_items_path}")
    else:
        print("\nNo hidden files or directories found.")

if __name__ == "__main__":
    main()
