a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

data_set = set()
for i in range(a):
    data_set.add(b[i])

for j in range(c):
    if d[j] in data_set:
        print(1)
    else:
        print(0)