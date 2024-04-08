from collections import deque
import sys

n = int(sys.stdin.readline())

for i in range(n):
    [a, b] = list(map(int, sys.stdin.readline().split()))
    data = deque(list(map(int, sys.stdin.readline().split())))
    index_list = deque([i for i in range(len(data))])
    now = 1
    while data:
        if data[0] == max(data):
            if index_list[0] == b:
                print(now)
                break
            data.popleft()
            index_list.popleft()
            now += 1
        else:
            data.append(data.popleft())
            index_list.append(index_list.popleft())
