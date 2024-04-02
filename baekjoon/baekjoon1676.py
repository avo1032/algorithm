import math

n = int(input())
factorial = math.factorial(n)
result = 0
for i in str(factorial)[::-1]:
    if i != '0':
        break
    else:
        result += 1
print(result)
