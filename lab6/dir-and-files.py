import os
import string
import time

#exercise 1. List only directories, files, and all directories and files in a specified path:
def list_directories_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return dirs, files, all_items

#exercise2. Check for access to a specified path (existence, readability, writability, executability):
def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

#exercise 3. Test whether a given path exists and find the filename and directory portion:
def check_path_and_extract_parts(path):
    exists = os.path.exists(path)
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    return exists, filename, directory

#exercise 4. Count the number of lines in a text file:
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

#exercise 5. Write a list to a file:
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

#exercise 6. Generate 26 text files named A.txt, B.txt, and so on up to Z.txt:
def generate_text_files():
    for letter in string.ascii_uppercase:
        file_path = letter + ".txt"
        with open(file_path, 'w') as file:
            file.write(f"Content for {letter}.txt\n")

#exercise 7. Copy the contents of a file to another file:
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
        destination_file.write(source_file.read())

#exercise 8. Delete a file by a specified path after checking access and existence:
def delete_file(path):
    if os.access(path, os.W_OK) and os.path.exists(path):
        os.remove(path)
        return True
    return False