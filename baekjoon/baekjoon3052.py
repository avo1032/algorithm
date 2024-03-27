import sys


data = [int(sys.stdin.readline().rstrip()) for i in range(10)]
arr = []

for i in data:
    arr.append(i%42)

print(len(set(arr)))