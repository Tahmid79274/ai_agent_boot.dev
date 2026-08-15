from functions.get_file_content import get_file_content

# print(f'Result for Current Directory:\n{get_file_content("calculator", ".")}')
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result = get_file_content("calculator", "main.py")
print(result)
# print(f"Result: {result}")
# print(f"main.py length: {len(result)}")
# print(f"main.py truncated: {'truncated' in result}")

result = get_file_content("calculator", "pkg/calculator.py")
print(result)
# print(f"Result: {result}")
# print(f"pkg/calculator.py length: {len(result)}")
# print(f"pkg/calculator.py truncated: {'truncated' in result}")

result = get_file_content("calculator", "/bin/cat")
print(result)
# print(f"Result: {result}")
# print(f"/bin/cat length: {len(result)}")
# print(f"/bin/cat truncated: {'truncated' in result}")

result = get_file_content("calculator", "pkg/does_not_exist.py")
# print(f"Result: {result}")
print(result)
# print(f"pkg/does_not_exist.py length: {len(result)}")
# print(f"pkg/does_not_exist.py truncated: {'truncated' in result}")