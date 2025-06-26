import os
import shutil
from pathlib import Path

FILE_TYPES = {
    'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
    'Videos': ['mp4', 'mkv', 'mov', 'avi', 'flv'],
    'Audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma'],
    'Code_Files': ['py', 'java', 'cpp', 'c', 'js', 'ts', 'html', 'css', 'php', 'json','xml', 'yaml', 'yml', 'sh', 'bat', 'rb', 'go', 'rs'],
}

def get_category(ext):
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return category
    return 'Others'


def organize_directory(source):
    source_path = Path(source)
    if not source_path.is_dir():
        print("Not a valid directory.")
        return
    if not source_path.exists():
        print("Directory does not exist.")
        return

    print(f"Organizing files in {source_path}.....")

    for item in source_path.iterdir():
        if item.is_file():
            extension = item.suffix.lower()

            if not extension:
                print(f"Skipping {item.name} as it has no extension")
                continue

            
            destination = get_category(extension[1:]) if extension.startswith('.') else extension
            destination_dir = source_path / destination
            destination_dir.mkdir(exist_ok=True)

            try:
                shutil.move(str(item), str(destination_dir))
                print(f"Moved {item.name} to {destination_dir.name}")
            except shutil.Error as e:
                print(f"Shutil error while moving {item.name}: {e}")
            except OSError as e:
                print(f"OS error while moving {item.name}: {e}")
            except Exception as e:
                print(f"Unexpected error while moving {item.name}: {e}")


if __name__ == "__main__":
    target = input("Enter the path of the directory to organize: ").strip()
    organize_directory(target)
