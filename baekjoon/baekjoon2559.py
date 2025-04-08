import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 초기 K개 합 계산
current_sum = sum(arr[:k])
max_sum = current_sum

# 슬라이딩 윈도우 방식으로 합을 갱신하며 최대값을 찾는다.
for i in range(k, n):
    current_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, current_sum)

print(max_sum)