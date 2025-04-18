MOD = 1_000_000_007

def count_sequences(N, M):
    dp = [0]*(N+1)
    dp[0] = 1                 # 0초를 채우는 방법 1가지(아무것도 안 함)

    for t in range(1, N+1):
        dp[t] = dp[t-1]       # 마지막에 A(1초) 사용
        if t >= M:            # 마지막에 B(M초) 사용
            dp[t] = (dp[t] + dp[t-M]) % MOD
    return dp[N]

N, M = map(int, input().split())
print(count_sequences(N, M))