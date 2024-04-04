import sys


n = int(input())
stack = []
data = [sys.stdin.readline().rstrip() for i in range(n)]

for i, action in enumerate(data):
    if action.startswith("push"):
        [push, num] = action.split(" ")
        stack.append(num)
    if action == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    if action == "size":
        print(len(stack))
    if action == "empty":
        if stack:
            print(0)
        else:
            print(1)
    if action == "pop":
        if stack:
            pop = stack.pop()
            print(pop)
        else:
            print(-1)
