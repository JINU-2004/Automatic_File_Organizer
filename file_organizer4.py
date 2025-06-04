import streamlit as st
import os
import shutil
import base64

# --- File type categories ---
FILE_TYPES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"]
}

# --- Organize files based on extension ---
def organize_files(upload_dir):
    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(upload_dir, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(upload_dir, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

# --- Folder structure visualization ---
def display_folder_structure(upload_dir):
    output = ""
    for root, dirs, files in os.walk(upload_dir):
        level = root.replace(upload_dir, '').count(os.sep)
        indent = "    " * level
        output += f"{indent}📁 {os.path.basename(root)}\n"
        subindent = "    " * (level + 1)
        for f in files:
            output += f"{subindent}📄 {f}\n"
    return output

# --- Set background image ---
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}

        /* Blue border styling for input text boxes */
        input[type="text"] {{
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 8px;
        }}

        /* Optional: change button appearance */
        button[kind="primary"] {{
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Streamlit App ---
st.set_page_config(page_title="Smart File Organizer", layout="centered")
set_background("file3.avif")  # Make sure this file exists in your working directory

st.markdown("<h1 style='text-align: center; color: black;'>📁 Smart File Organizer</h1>", unsafe_allow_html=True)

# --- Choose Mode ---
option = st.radio("Choose Mode:", ["Organize existing folder", "Upload files to a custom folder"])

# --- Mode 1: Organize existing folder ---
if option == "Organize existing folder":
    folder_path = st.text_input("Enter full path of the folder to organize:")
    if folder_path:
        if os.path.exists(folder_path):
            if st.button("Organize Existing Folder"):
                organize_files(folder_path)
                st.success("✅ Files organized successfully!")
                st.text(display_folder_structure(folder_path))
        else:
            st.error("❌ The provided folder path does not exist.")

# --- Mode 2: Upload files into a system folder ---
else:
    target_path = st.text_input("Enter the system folder path to save and organize uploaded files:")
    uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

    if uploaded_files and target_path:
        if os.path.exists(target_path):
            for file in uploaded_files:
                save_path = os.path.join(target_path, file.name)
                with open(save_path, "wb") as f:
                    f.write(file.read())
            st.success("✅ Files uploaded successfully.")
            if st.button("Organize Uploaded Files"):
                organize_files(target_path)
                st.success("📂 Uploaded files organized successfully!")
                st.text(display_folder_structure(target_path))
        else:
            st.error("❌ The path you entered does not exist.")
