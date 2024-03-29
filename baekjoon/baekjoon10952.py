import sys

for line in sys.stdin:
    data = list(map(int, line.split()))
    result = data[0] + data[1]
    if result == 0:
        break
    print(result)