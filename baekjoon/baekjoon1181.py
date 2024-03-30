import sys


n = int(input())

data = set([sys.stdin.readline().rstrip() for i in range(n)])
sorted_word = sorted(data, key=lambda x: (len(x), x))
for i in sorted_word:
    print(i)