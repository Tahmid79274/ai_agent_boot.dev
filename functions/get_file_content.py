import os
from config import MAX_CHARS

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_content",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # print(f'Checking validity for {file_path} and {working_directory}')
        working_dir_abs = os.path.abspath(working_directory)
        # print(f'{working_directory}\'s Absolute Path: {working_dir_abs}')
        # file_path_abs = os.path.abspath(file_path)
        # print(f'{file_path}\'s Absolute Path: {file_path_abs}')
        # print(f'Common Path between {working_directory} and {file_path} is {os.path.commonpath([working_dir_abs,file_path_abs])}')
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # print(f'{file_path}\'s  ultimate path: {target_dir}')
        # print(f'Common Path between: {working_directory} and {file_path} is {os.path.commonpath([working_dir_abs, target_dir])}')
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        # print(f'Validity between {working_directory} and {file_path} is {valid_target_dir}')
        is_file_available = os.path.isfile(target_dir)
        # print(f'Is the {target_dir} found in {working_dir_abs}: {os.path.isfile(target_dir)}')
        if valid_target_dir == False:
            # print(f'Validity Failed for {file_path}')
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        elif is_file_available == False:
            # print(f'{file_path} is Not a file')
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(target_dir, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                # After reading the first MAX_CHARS...
                if f.read(1):
                    file_content_string += f'[...File "{target_dir}" truncated at {MAX_CHARS} characters]'
                return file_content_string
    except Exception as e:
        return f"Error: {e}"