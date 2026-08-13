import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        print(f'Working Path Before: {working_directory}')
        print(f'File Path Before: {file_path}')
        abs_working_directory_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(file_path)
        common_path_between_working_directory_and_file_path  = os.path.commonpath([abs_working_directory_path,abs_file_path])
        print(f'Working Directory: {abs_working_directory_path}')
        print(f'File Path: {abs_file_path}')
        print(f'Commonpath between: {common_path_between_working_directory_and_file_path}')
        joined_path = os.path.normpath(os.path.join(abs_working_directory_path,abs_file_path))
        parent_directory = os.path.dirname(file_path)
        print(f'Parent Directory: {parent_directory}')
        print(f'Joined Path: {joined_path}')
        # if not :
        #     return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(joined_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            # actual_file_path = os.makedirs(name=abs_file_path,exist_ok=True)
            with open(abs_file_path, "w") as f:
                 f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
            return f"Error: {e}"