import sys

n = int(sys.stdin.readline());

fibonacci_arr = [1, 1, 1];
if (n > 3):
    for i in range(3, n):
        fibonacci_num = fibonacci_arr[i-1] + fibonacci_arr[i-3];
        fibonacci_arr.append(fibonacci_num);

print(fibonacci_arr[n-1]);
