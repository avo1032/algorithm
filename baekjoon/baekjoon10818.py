n = int(input())
data = list(map(int, input().split()))

max = data[0]
min = data[0]

for i in data:
    if i > max:
        max = i
    if i < min:
        min = i

print(f'{min} {max}')