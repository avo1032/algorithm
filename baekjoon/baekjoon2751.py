import sys


n = int(input())
num_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)
sorted_list = sorted(num_list)
for j in sorted_list:
    print(j)
