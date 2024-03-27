import sys

n = int(input())
data = [sys.stdin.readline().rstrip() for i in range(n)]

for i in data:
    i_list = list(i)
    result = 0
    addValue = 0
    for j in i_list:
        if j == "O":
            addValue += 1
            result += addValue
        else:
            addValue = 0
    print(result)