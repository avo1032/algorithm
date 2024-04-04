from collections import deque
import sys


n = int(input())
queue = deque()
data = [sys.stdin.readline().rstrip() for i in range(n)]

for i, action in enumerate(data):
    if action.startswith("push"):
        [push, num] = action.split(" ")
        queue.append(num)
    if action == "size":
        print(len(queue))
    if action == "empty":
        if queue:
            print(0)
        else:
            print(1)
    if action == "pop":
        if queue:
            pop = queue.popleft()
            print(pop)
        else:
            print(-1)
    if action == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if action == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
