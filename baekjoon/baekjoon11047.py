import sys


[N, K] = list(map(int, input().split()))
coin = [int(sys.stdin.readline()) for _ in range(N)]
answer = 0
for index, j in enumerate(coin[::-1]):
    if j > K:
        continue
    answer += K // j
    K = K % j

print(answer)