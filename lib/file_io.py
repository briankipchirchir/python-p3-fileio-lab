import os

def write_file(file_name, file_content):
    """Write content to a .txt file, overwriting any existing content."""
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Append content to a .txt file without overwriting existing content."""
    file_name_with_extension = f"{file_name}.txt"
    with open(file_name_with_extension, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """Read content from a .txt file and return it as a string."""
    file_name_with_extension = f"{file_name}.txt"
    if not os.path.isfile(file_name_with_extension):
        raise FileNotFoundError(f"The file {file_name_with_extension} does not exist.")
    
    with open(file_name_with_extension, 'r') as file:
        return file.read()
