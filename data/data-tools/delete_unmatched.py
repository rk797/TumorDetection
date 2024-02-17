import os
#deletes the unmatched annotations from directory1

def find_and_delete_files(directory1, directory2):
    files1 = set(get_file_names(directory1, ".txt"))
    files2 = set(get_file_names(directory2, ".jpg"))

    for file_name in files1:
        if file_name not in files2:
            file_path = os.path.join(directory1, file_name + ".txt")
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_name}")
            else:
                print(f"File not found in directory1: {file_name}")

def get_file_names(directory, extension):
    file_names = []
    for file in os.listdir(directory):
        file_name, ext = os.path.splitext(file)
        if ext == extension:
            file_names.append(file_name)
    return file_names


directory1 = r"file-path"
directory2 = r"file-path"

find_and_delete_files(directory1, directory2)
