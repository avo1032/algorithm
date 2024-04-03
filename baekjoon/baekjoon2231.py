n = int(input())

result = 0

while result < n:
    target = result + sum(int(digit) for digit in str(result))
    if target == n:
        break
    result += 1

if result == n:
    print(0)
else:
    print(result)