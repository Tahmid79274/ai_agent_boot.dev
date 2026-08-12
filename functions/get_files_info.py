import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        # 1. Get the absolute path of the permitted working directory
        abs_working_dir = os.path.abspath(working_directory)

        # 2. Build the absolute path of the requested file
        target_file = os.path.normpath(
            os.path.join(abs_working_dir, file_path)
        )

        # 3. Make sure the requested file is inside
        #    the permitted working directory
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return (
                f'Error: Cannot read "{file_path}" '
                f'as it is outside the permitted working directory'
            )

        # 4. Make sure the target exists and is a regular file
        if not os.path.isfile(target_file):
            return (
                f'Error: File not found or is not a regular file: '
                f'"{file_path}"'
            )

        # 5. Open the file
        with open(target_file, "r") as file:
            # 6. Read at most MAX_CHARS characters
            content = file.read(MAX_CHARS)

            # 7. Try to read one more character
            #    If we get something, the file was larger
            if file.read(1):
                content += (
                    f'[...File "{file_path}" truncated at '
                    f'{MAX_CHARS} characters]'
                )

            # 8. Return the content
            return content

    # 9. Catch errors from standard library functions
    except Exception as e:
        return f"Error: {e}"