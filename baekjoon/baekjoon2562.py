arr = [int(input()) for _ in range(9)]

max_number = 0
max_index = 0

for i, num in enumerate(arr):
    if num > max_number:
        max_number = num
        max_index = i + 1

print(max_number)
print(max_index)
