import sys

n = int(input())
people_list = []
for i in range(n):
    people = sys.stdin.readline().rstrip().split()
    people_list.append([i, int(people[0]), people[1]])

sorted_list = sorted(people_list, key=lambda x: (int(x[1]), x[0]))
for j in sorted_list:
    printing = f"{j[1]} {j[2]}"
    print(printing)