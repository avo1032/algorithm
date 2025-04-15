import sys

n = int(sys.stdin.readline())
wine = [0] + [int(sys.stdin.readline()) for _ in range(n)]  # 1‑based 인덱스

if n == 1:                 # 예외 처리
    print(wine[1])
    sys.exit()

# dp[i] : i번째 잔까지 고려했을 때 최대 마신 양
dp = [0]*(n+1)
dp[1] = wine[1]
dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(
        dp[i-1],                         # i번째 잔을 마시지 않음
        dp[i-2] + wine[i],               # (i-1) 잔을 건너뛰고 i 잔 마심
        dp[i-3] + wine[i-1] + wine[i]    # i, i-1 잔을 연속으로 마심
    )

print(dp[n])