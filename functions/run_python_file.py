import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir_with_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # print(f'Target File with full dir: {target_dir_with_path}')
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir_with_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir_with_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_dir_with_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        else:
            command = ["python", target_dir_with_path]
            # if len(args) > 0:
            command.extend(args)
            completed_process = subprocess.run(args=command, stdin=None, input=None, stdout=working_dir_abs, stderr=None, capture_output=True, shell=False, cwd=working_dir_abs, timeout=30, check=False, encoding=None, errors=None, text=True, env=None, universal_newlines=None,)
            print(f'{file_path}\'s Return Code: {completed_process.returnCode}')
            print(f'{file_path}\'s Std Out: {completed_process.stdout}')
            print(f'{file_path}\'s Std Err: {completed_process.stderr}')
            # output_str = ''
            # if completed_process.returnCode != 0:
            #     output_str += f"Process exited with code {completed_process.returnCode}"
            # if len(completed_process.stdout) == 0 and len(completed_process.stderr) == 0:
            #     output_str += f"No output produced"
            # elif len(completed_process.stdout) != 0:
            #     output_str += f"STDOUT:{completed_process.stdout}"
            # elif len(completed_process.stdout) != 0:
            #     output_str += f"STDERR:{completed_process.stderr}"
            # return output_str
    except Exception as e:
        return f"Error: executing Python file: {e}"