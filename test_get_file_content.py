from functions.get_file_content import get_file_content


# Test large file
result = get_file_content("calculator", "lorem.txt")

print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")


# Test normal file
print(get_file_content("calculator", "main.py"))


# Test file inside subdirectory
print(get_file_content("calculator", "pkg/calculator.py"))


# Test file outside permitted directory
print(get_file_content("calculator", "/bin/cat"))


# Test nonexistent file
print(get_file_content("calculator", "pkg/does_not_exist.py"))