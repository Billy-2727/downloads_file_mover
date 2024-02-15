import shutil
import os
import getpass

# Grabs the currenly logged in user's username
username = getpass.getuser()

# Sets required variables for directory creation
basepath = f"C:/Users/{username}/Downloads/"
soft_dir = f"C:/Users/{username}/Downloads/Software"
doc_dir = f"C:/Users/{username}/Downloads/Documents"
img_dir = f"C:/Users/{username}/Downloads/Images"
zips_dir = f"C:/Users/{username}/Downloads/Zips"
scripts_dir = f"C:/Users/{username}/Downloads/Scripts"
videos_dir = f"C:/Users/{username}/Downloads/Videos"

dir_list = [soft_dir, doc_dir, img_dir, zips_dir, scripts_dir]
# Loops through each directory and creates file if it doesn't already exist
for dir in dir_list:
    if not os.path.exists(dir):
        os.makedirs(dir)

# Checks for files in directory ending in exe_extenstions and moves them to Software folder
for files in os.listdir(basepath):
    exe_extensions = (".exe", ".msi", ".msix")
    if files.endswith(exe_extensions):
        shutil.move(os.path.join(basepath, files), soft_dir)

# Checks for files in directory ending in doc_extenstions and moves them to Documents folder
for files in os.listdir(basepath):
    doc_extensions = (
        ".doc",
        ".docx",
        ".pdf",
        ".ppt",
        ".pptx",
        ".xls",
        ".xlsx",
        ".txt",
        ".csv",
    )
    if files.endswith(doc_extensions):
        shutil.move(os.path.join(basepath, files), doc_dir)

# Checks for files in directory ending in img_extenstions and moves them to Images folder
for files in os.listdir(basepath):
    img_extensions = (
        ".png",
        ".jpg",
        ".JPG",
        ".jpeg",
        ".gif",
        ".bmp",
        ".tiff",
        ".psd",
        ".svg",
        ".pur",
        ".excalidraw",
    )
    if files.endswith(img_extensions):
        shutil.move(os.path.join(basepath, files), img_dir)

# Checks for files in directory ending in zip_extenstions and moves them to Zips folder
for files in os.listdir(basepath):
    zip_extensions = (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".tar.gz")
    if files.endswith(zip_extensions):
        shutil.move(os.path.join(basepath, files), zips_dir)

# Checks for files in directory ending in script_extenstions and moves them to Scripts folder
for files in os.listdir(basepath):
    script_extensions = (".bat", ".cmd", ".ps1", ".psm1")
    if files.endswith(script_extensions):
        shutil.move(os.path.join(basepath, files), scripts_dir)

# Checks for files in directory ending in video_extenstions and moves them to Videos folder
for files in os.listdir(basepath):
    script_extensions = (
        ".mov",
        ".avi",
        ".mp4",
        ".mpg",
        ".mpeg",
        ".wmv",
    )
    if files.endswith(script_extensions):
        shutil.move(os.path.join(basepath, files), scripts_dir)
