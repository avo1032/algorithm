import sys

n = int(input())

data = [sys.stdin.readline().rstrip() for i in range(n)]

for i in data:
    H = int(i.split()[0])
    W = int(i.split()[1])
    N = int(i.split()[2])
    result = [0, 1]
    for j in range(N):
        if H > result[0]:
            result[0] += 1
        elif H == result[0]:
            result[0] = 1
            result[1] += 1
    if result[1] < 10:
            result[1] = "0" + str(result[1])
    else:
        result[1] = str(result[1])
    print(str(result[0]) + result[1])

# print(type(data[0].split()[0]))

# print(data)

# import math


# print(math.floor(12 / 6))