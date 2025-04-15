import sys

M, N = map(int, sys.stdin.readline().split())
snacks = list(map(int, sys.stdin.readline().split()))

left, right = 1, max(snacks)        # 가능한 최소·최대 길이
best = 0

while left <= right:
    mid = (left + right) // 2       # 시도해 볼 과자 길이 L
    pieces = sum(s // mid for s in snacks)

    if pieces >= M:                 # 모든 조카에게 줄 수 있다면
        best = mid                  # 길이를 늘려 본다
        left = mid + 1
    else:                           # 부족하다면 길이를 줄인다
        right = mid - 1

print(best)