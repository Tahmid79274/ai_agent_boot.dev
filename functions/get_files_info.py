import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_directory = os.path.abspath(working_directory)
    print(f'Absolute Working Directory Path: {abs_working_directory}')
    abs_directory = os.path.abspath(directory)
    print(f'Absolute Directory Path: {abs_directory}')
    target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))
    print(f'Target Directory Path: {target_dir}')