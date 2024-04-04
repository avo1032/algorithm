from collections import deque
import sys


n = int(input())
queue = deque()
data = [sys.stdin.readline().rstrip() for i in range(n)]

for i, action in enumerate(data):
    if action.startswith("push_front"):
        [push, num] = action.split(" ")
        queue.appendleft(num)
    if action.startswith("push_back"):
        [push, num] = action.split(" ")
        queue.append(num)

    if action == "pop_front":
        if queue:
            pop = queue.popleft()
            print(pop)
        else:
            print(-1)
    if action == "pop_back":
        if queue:
            pop = queue.pop()
            print(pop)
        else:
            print(-1)

    if action == "size":
        print(len(queue))
    if action == "empty":
        if queue:
            print(0)
        else:
            print(1)
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
