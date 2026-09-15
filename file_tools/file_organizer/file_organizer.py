import argparse
import os
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Enter directory name")

    args = parser.parse_args()

    categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".ico", ".heic", ".raw"],
    
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpeg", ".mpg", ".3gp"],
    
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".aiff", ".opus"],
    
    "Documents": [".pdf", ".txt", ".doc", ".docx", ".odt", ".rtf", ".md", ".tex"],
    
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".tsv"],
    
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    
    "Archives": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".xz", ".iso"],
    
    "Code": [".py", ".js", ".ts", ".html", ".css", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs", ".php", ".rb", ".swift", ".kt"],
    
    "Scripts": [".sh", ".bash", ".bat", ".ps1", ".cmd"],
    
    "Executables": [".exe", ".msi", ".app", ".dmg", ".deb", ".rpm", ".apk"],
    
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    
    "eBooks": [".epub", ".mobi", ".azw", ".azw3"],
    
    "Databases": [".db", ".sqlite", ".sql", ".mdb"],
    
    "3D_Models": [".obj", ".stl", ".fbx", ".blend", ".dae", ".3ds"],
    
}

    files = check_input(args.directory)
    
    folders_to_create, others = check_extension(categories, files)

    create_folders(folders_to_create, args.directory)

    move_files(categories, others, files, args.directory)


def check_input(directory):
    try:
        files = []
        dir_contents = os.listdir(directory)
        for file in dir_contents:
            if os.path.isfile(os.path.join(directory, file)):
                files.append(file)
                
    except FileNotFoundError:
        print("Directory doesn't exist.")
        raise SystemExit(1)
    return files



# Check files extensions, add directories to be created to a set.
def check_extension(categories, files):
    folders = set()
    files_matched = set()
    others_files = set()

    for category, extension in categories.items():
        if category == "Others":
            continue
    
        for file in files:
            if Path(file).suffix.lower() in extension:
                folders.add(category)
                files_matched.add(file)

    if len(files_matched) != len(files):
        folders.add("Others")

    for other_files in files:
        if not other_files in files_matched:
            others_files.add(other_files)

    
    return folders, others_files

# create the directories
def create_folders(folders, directory):
    for folder in folders:
        folder_path = os.path.join(os.path.abspath(directory), folder)
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass

# Move files to their corresponding directories
def move_files(categories, other, files, directory):
    for category, extension in categories.items():
        if category == "Others":
            continue
        
        for file in files:
            if(Path(file).suffix.lower() in extension):
                try:
                    os.rename(os.path.join(os.path.abspath(directory),file), os.path.join(os.path.abspath(directory), category, file))
                except (FileNotFoundError, FileExistsError, PermissionError) as type:
                    print(f"Error moving '{file}': {type}")

    for other_files in other:
        try:
            os.rename(os.path.join(os.path.abspath(directory),other_files), os.path.join(os.path.abspath(directory), "Others", other_files))
        except (FileNotFoundError, FileExistsError, PermissionError) as type:
            print(f"Error moving '{other_files}': {type}")

if __name__ == "__main__":
    main()
