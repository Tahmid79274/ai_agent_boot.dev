import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        if not os.path.isdir(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(os.path.join(working_directory, file_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            with open(os.path.join(working_directory,file_path), "r") as file:
                content = file.read(MAX_CHARS)
                # print(f'Got content')
                # After reading the first MAX_CHARS...
                if file.read(1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return content
    except Exception as e:
        return f"Error: {e}"