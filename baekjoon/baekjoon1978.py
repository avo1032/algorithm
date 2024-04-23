import math

n = int(input())
nums = list(map(int, input().split()))
result = 0

for i in nums:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result += 1

print(result)
