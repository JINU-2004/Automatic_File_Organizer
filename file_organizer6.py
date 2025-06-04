import streamlit as st
import os
import shutil
from pathlib import Path

# --- Define File Type Categories ---
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".m4a", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

# --- Organize Files into Folders ---
def organize_files(upload_dir):
    for file in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, file)
        if os.path.isfile(file_path):
            ext = Path(file).suffix.lower()
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = os.path.join(upload_dir, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(upload_dir, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

# --- Streamlit UI ---
st.title("📁 Smart File Organizer")
st.write("Upload multiple files and access them in organized folders directly.")

uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

if uploaded_files:
    base_dir = Path("organized_files")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    # Save uploaded files
    for file in uploaded_files:
        with open(base_dir / file.name, "wb") as f:
            f.write(file.read())

    # Organize them
    organize_files(base_dir)
    st.success("✅ Files organized successfully!")

    # Show organized folders
    st.subheader("📂 Organized Folders with Files")

    for folder in sorted(base_dir.iterdir()):
        if folder.is_dir():
            st.markdown(f"### 📁 {folder.name}")
            for f in folder.iterdir():
                with open(f, "rb") as file_obj:
                    st.download_button(
                        label=f"📄 Download {f.name}",
                        data=file_obj,
                        file_name=f.name,
                        mime="application/octet-stream"
                    )
