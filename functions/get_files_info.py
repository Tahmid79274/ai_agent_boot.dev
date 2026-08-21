import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
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


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        # print(f'Absolute Working Directory Path: {working_dir_abs}')
        abs_directory = os.path.abspath(directory)
        # print(f'Absolute Directory Path: {abs_directory}')
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # print(f'Target Directory Path: {target_dir}')
        # print(f'Common Path between: {working_dir_abs} and target diretory {target_dir} is {os.path.commonpath([working_dir_abs, target_dir])}')
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'
        else:
            file_or_folders_in_target_dir = os.listdir(target_dir)
            # print(f'Available files or folders in the {target_dir}: {file_or_folders_in_target_dir}')
            # for file_or_folder_index in range(0,len(file_or_folders_in_target_dir),1):
            #     print(f'- {file_or_folders_in_target_dir[file_or_folder_index]}: file_size={os.path.getsize(file_or_folders_in_target_dir[file_or_folder_index])} bytes, is_dir={os.path.isdir(file_or_folders_in_target_dir[file_or_folder_index])}')
            target_dir_update = ''
            for file_or_folder in file_or_folders_in_target_dir:
                # print(file_or_folder)
                is_directory = os.path.isdir(os.path.normpath(os.path.join(target_dir, file_or_folder)))
                file_or_folder_size = os.path.getsize(os.path.normpath(os.path.join(target_dir, file_or_folder)))
                target_dir_update += f'\t- {file_or_folder}: file_size={file_or_folder_size} bytes, is_dir={is_directory}\n'
                # print(f'- {file_or_folder}: file_size={file_or_folder_size} bytes, is_dir={is_directory}')
            # return f'Success: "{directory}" is within the working directory'
            # print(f'Targeted directory Update: {target_dir_update}')
            return target_dir_update
    except Exception as e:
        return f"Error: {e}"