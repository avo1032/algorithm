import sys


[n, m] = list(map(int, sys.stdin.readline().split()))
doc = {}
for i in range(n):
    [a, b] = sys.stdin.readline().split()
    doc[a] = b
for i in range(m):
    print(doc[sys.stdin.readline().strip()])
