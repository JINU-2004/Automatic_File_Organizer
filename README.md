# 📁 Automatic_File_Organizer

Automatically organize files into folders by file type. 

This is a simple Python script that organizes files in a specified directory into categorized subfolders based on their file extensions.

## 🚀 Features

- Automatically moves files into folders like:
  - `Documents`
  - `Images`
  - `Videos`
  - `Audio`
  - `Code_Files`
  - `Others` (for uncategorized files)
- Handles errors gracefully
- Skips files without extensions
- Cross-platform (Windows, macOS, Linux)

## 🛠️ How It Works

The script checks each file's extension in the given directory and places it into a subfolder corresponding to its category.

### File Type Categories:

```python
FILE_TYPES = {
    'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
    'Videos': ['mp4', 'mkv', 'mov', 'avi', 'flv'],
    'Audio': ['mp3', 'wav', 'aac', 'flac', 'ogg', 'm4a', 'wma'],
    'Code_Files': ['py', 'java', 'cpp', 'c', 'js', 'ts', 'html', 'css', 'php', 'json', 'xml', 'yaml', 'yml', 'sh', 'bat', 'rb', 'go', 'rs'],
}
```
### ▶️ Usage
- Save the script as organize_files.py
- Open a terminal or command prompt.
- Run the script:
```
python organize_files.py
```
### 📂 Example
- If your directory has:
```
    project/
       ├── resume.pdf
       ├── image.jpg
       ├── music.mp3
       ├── script.py
```
- After running the script:
```
  project/
    ├── Documents/
    │   └── resume.pdf
    ├── Images/
    │   └── image.jpg
    ├── Audio/
    │   └── music.mp3
    ├── Code_Files/
        └── script.py
```
