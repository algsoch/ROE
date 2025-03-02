import os
import zipfile
import shutil
import subprocess

def extract_zip(zip_path, extract_dir):
    """Extract zip file to specified directory"""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Extracted {zip_path} to {extract_dir}")

def move_files_to_target(source_dir, target_dir):
    """Move all files from subfolders to target directory"""
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Walk through all directories and files
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_dir, file)
            # Move the file
            shutil.move(source_path, target_path)
    
    print(f"Moved all files to {target_dir}")

def rename_files_with_digit_rule(directory):
    """Rename all files replacing each digit with the next one"""
    files = os.listdir(directory)
    
    for old_name in files:
        # Create new filename by replacing digits
        new_name = ""
        for char in old_name:
            if char.isdigit():
                # Replace digit with next one (9 becomes 0)
                new_name += str((int(char) + 1) % 10)
            else:
                new_name += char
        
        # Rename the file
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
    
    print(f"Renamed all files in {directory}")

def get_checksum(directory):
    """Run the grep and sha256sum command to get checksum"""
    # Change to the directory first
    current_dir = os.getcwd()
    os.chdir(directory)
    
    # Run the command
    cmd = "grep . * | LC_ALL=C sort | sha256sum"
    
    try:
        # For Windows, we need to use WSL or Git Bash
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"Command output: {result.stdout}")
    except Exception as e:
        print(f"Error running command: {e}")
    
    # Change back to original directory
    os.chdir(current_dir)

def main():
    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(base_dir, 'qmove.zip')
    extract_dir = os.path.join(base_dir, 'qmove_extracted')
    target_dir = os.path.join(base_dir, 'qmove_result')
    
    # Step 1: Extract zip
    extract_zip(zip_path, extract_dir)
    
    # Step 2: Move all files to target directory
    move_files_to_target(extract_dir, target_dir)
    
    # Step 3: Rename files according to the rule
    rename_files_with_digit_rule(target_dir)
    
    # Step 4: Get checksum
    get_checksum(target_dir)
    
    print("Done!")

if __name__ == "__main__":
    main()