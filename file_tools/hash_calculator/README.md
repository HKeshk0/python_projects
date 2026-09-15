# File Hash Calculator

A Python command-line tool that calculates cryptographic hashes for files.

The tool supports MD5, SHA-1, and SHA-256 and reads files in chunks so that large files can be processed without loading the entire file into memory.

## Features
* Calculate MD5, SHA-1, or SHA-256 hashes
* Calculate all supported hashes at once
* Process files incrementally using 4 KB chunks
* Command-line interface using argparse
* Handles files that do not exist

## Usage

Run the program with:
```
python file_hash.py <filename>
```
To calculate a specific hash:
```
python file_hash.py <filename> --algorithm md5
python file_hash.py <filename> --algorithm sha1
python file_hash.py <filename> --algorithm sha256
```
By default, the program calculates all three hashes:
```
python file_hash.py <filename> --algorithm all

File: example.txt  
MD5: 098f6bcd4621d373cade4e832627b4f6  
SHA256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08  
SHA1: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3  
```
## Why This Is Useful in Cybersecurity

File hashes can be used as unique fingerprints for files.

They are commonly used for:

* File integrity verification  
* Malware identification  
* IOC (Indicator of Compromise) analysis  
* Comparing files  
* Investigating suspicious files  

**SHA-256** is generally preferred for modern security applications. MD5 and SHA-1 are included because they are still encountered in legacy systems, existing tools, and security investigations.

## Python Concepts Practiced

This project was built to practice Python programming and cybersecurity automation concepts, including:

* argparse  
* Functions  
* Dictionaries  
* Loops  
* Exception handling  
* File handling  
* Binary file reading  
* Incremental hashing with hashlib  
* Command-line arguments  
