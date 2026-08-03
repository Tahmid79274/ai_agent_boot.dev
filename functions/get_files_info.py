import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        # print(f"Absolute Path: {working_dir_abs}")
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # print(f"target_dir: {target_dir}")
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        # print(f"Is Valid Path: {valid_target_dir}")
        if not valid_target_dir:
            return f'Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'"{directory}" is not a directory'
        else:
            return f'Success: "{directory}" is within the working directory'
    except TypeError as e:
        # Fires if working_directory/directory isn't a str or os.PathLike —
        # e.g. someone passes None or an int by mistake.
        return f'Invalid path type provided - {e}'

    except ValueError as e:
        # Fires from os.path.commonpath — mixed absolute/relative paths in the
        # list, or (on Windows) paths pointing at different drives.
        return f'Could not resolve path - {e}'

    except OSError as e:
        # Broad filesystem-level catch-all: permission denied, broken symlink
        # loops, path too long, etc. Rare here since isdir() swallows most of
        # these itself, but future code added inside this try (e.g. os.listdir())
        # could raise these.
        return f'OS error while accessing path - {e}'

    except Exception as e:
        # Last-resort catch so the function never crashes the caller with an
        # unhandled traceback — but log it, since a bare Exception here means
        # something you didn't anticipate slipped through.
        print(f'[get_files_info] Unexpected error: {e}')
        return f'Error: {e}'