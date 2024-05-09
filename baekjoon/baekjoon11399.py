import sys

n = int(input())
atm_list = list(map(int, sys.stdin.readline().split()))
atm_list.sort()
add_time = 0
answer = 0
for i in atm_list:
    answer += add_time + i
    add_time += i
print(answer)