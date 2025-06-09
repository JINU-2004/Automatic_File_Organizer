import os
import shutil

# Define file type categories and their associated extensions
FILE_TYPES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv'],
}

# Function to get the category of a file based on its extension
def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

# Function to organize files in the given directory
def organize_directory(path):
    if not os.path.isdir(path):
        print("The directory does not exist.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            folder = get_category(ext)
            folder_path = os.path.join(path, folder)

            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))

            print(f"Moved: {filename} -> {folder}/")

# Entry point of the script
if __name__ == "__main__":
    target = input("Enter the path of the directory to organize: ").strip()
    organize_directory(target)
