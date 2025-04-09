import sys

n = int(sys.stdin.readline())
pattern = sys.stdin.readline().strip()
prefix, suffix = pattern.split('*')

for _ in range(n):
    file_name = sys.stdin.readline().strip()
    if len(file_name) < len(prefix) + len(suffix):
        print("NE")
    elif file_name.startswith(prefix) and file_name.endswith(suffix):
        print("DA")
    else:
        print("NE")