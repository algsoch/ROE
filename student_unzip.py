import zipfile
import os
import sys

def unzip_file(zip_path):
    """
    Unzip the given file to the same directory where the zip file is located
    """
    # Get the directory where the zip file is located
    extract_dir = os.path.dirname(os.path.abspath(zip_path))
    
    print(f"Extracting {zip_path} to {extract_dir}")
    
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all contents to the directory
            zip_ref.extractall(extract_dir)
        print(f"Successfully extracted {zip_path}")
        
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file")
    except FileNotFoundError:
        print(f"Error: {zip_path} not found")
    except Exception as e:
        print(f"Error extracting {zip_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unzip_script.py <path_to_zipfile>")
    else:
        zip_path = sys.argv[1]
        unzip_file(zip_path)