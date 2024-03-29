import sys

for line in sys.stdin:
    data = list(map(int, line.split()))
    print(data[0] + data[1])