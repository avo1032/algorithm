import math


[n, k] = list(map(int, input().split()))

n_factorial = math.factorial(n)
k_factorial = math.factorial(k)
n_k_factorial = math.factorial(n-k)

print(math.ceil(n_factorial/(k_factorial*n_k_factorial)))