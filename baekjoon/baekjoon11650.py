import sys


n = int(input())

data_list = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    data_list.append(data)

sorted_data = sorted(data_list, key=lambda x: (x[0], x[1]))
for j in sorted_data:
    print(j[0], end=" ")
    print(j[1])