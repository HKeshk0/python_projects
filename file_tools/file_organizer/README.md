# File Organizer

A Python command-line tool that automatically organizes files in a directory based on their file extensions.

## Features
* Organizes files into categories such as Images, Videos, Audio, Documents, Code, and Archives
* Handles uppercase and lowercase file extensions
* Creates category folders automatically
* Places unsupported file types into an Others folder
* Handles missing directories and file operation errors
* Uses command-line arguments with argparse

## Usage

Run the program with:
```
python file_organizer.py <directory>
```
Example:
```
python file_organizer.py Downloads
```

Before:
```
Downloads/  
├── photo.jpg  
├── report.pdf  
├── song.mp3  
├── script.py  
└── archive.zip  
```
After:  
```
Downloads/  
├── Images/  
│   └── photo.jpg   
├── Documents/  
│   └── report.pdf  
├── Audio/  
│   └── song.mp3  
├── Code/  
│   └── script.py  
└── Archives/  
    └── archive.zip  
```
## Python Concepts Practiced

This project was built to practice Python programming and cybersecurity automation concepts, including:

* argparse  
* Functions  
* Dictionaries
* Sets
* Loops
* File and directory handling
* pathlib
* os
* Exception handling
* File extensions
* Moving files with os.rename()
