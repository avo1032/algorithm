import sys


n = int(input())

stack = []
for i in range(n):
    data = int(sys.stdin.readline())
    if not data == 0:
        stack.append(data)
    else:
        stack.pop()
print(sum(stack))