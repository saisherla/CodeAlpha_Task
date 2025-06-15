import os
import shutil

# Define file categories and their extensions
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

# Path to organize (e.g., Downloads folder)
DOWNLOAD_FOLDER = os.path.expanduser("~/Downloads")

def get_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    print(f"📁 Organizing files in: {folder_path}")

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            category = get_category(file)
            category_folder = os.path.join(folder_path, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            dest_path = os.path.join(category_folder, file)
            shutil.move(full_path, dest_path)
            print(f"✅ Moved: {file} → {category}/")

if __name__ == "__main__":
    organize_files(DOWNLOAD_FOLDER)
