import sys

n = int(input())  
data = [sys.stdin.readline().rstrip() for i in range(n)] # a = ["1 2 3", "4 5 6"]

for j in data:
    output = ""
    arr = j.split()
    for z in list(arr[1]):
        output += z * int(j[0])
    print(output)
