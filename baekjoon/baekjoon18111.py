import sys


[n, m, b] = list(map(int, sys.stdin.readline().split()))
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
index = 0
for floor in range(257):
    addBlock = 0
    subtractBlock = 0
    for i in range(n):
        for j in  range(m):
            if data[i][j] > floor:
                subtractBlock += data[i][j] - floor
            else:
                addBlock += floor - data[i][j]
    if addBlock > subtractBlock + b:
        continue
    if (subtractBlock * 2) + addBlock <= answer:
        answer = (subtractBlock * 2) + addBlock
        index = floor

print(answer, index)