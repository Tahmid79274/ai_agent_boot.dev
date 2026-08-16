import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir_with_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # print(f'Target File with full dir: {target_dir_with_path}')
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir_with_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        target_dir_name = os.path.dirname(target_dir_with_path)
        # print(f'Target dir: {target_dir_name}')
        os.makedirs(os.path.dirname(target_dir_name), exist_ok=True)
        if os.path.isdir(target_dir_with_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            with open(target_dir_with_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"