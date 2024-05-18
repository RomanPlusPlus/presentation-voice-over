import os
import shutil

def recreate_directory(dir_path):
    """
    Creates a directory. If the directory already exists, deletes it and then creates it again.
    
    :param dir_path: Path to the directory to be created.
    """
    # Check if the directory exists
    if os.path.exists(dir_path):
        # Remove the directory
        print(f"Directory '{dir_path}' already exists. Deleting the directory...")
        shutil.rmtree(dir_path)
    
    # Create the directory
    os.makedirs(dir_path)
    print(f"Directory '{dir_path}' has been recreated.")

# Example usage
# recreate_directory('example_directory')