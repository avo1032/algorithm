import sys
sys.setrecursionlimit(10_000)

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dirs = (-1, 0, 1)        # ↙, ↓, ↘  (열 변위)
INF  = 10**9
best = INF               # 최소 연료

def dfs(r: int, c: int, prev_dir: int, fuel: int):
    """
    r, c     : 현재 위치
    prev_dir : 직전에 사용한 방향(-2 = 시작)
    fuel     : 지금까지 사용한 연료
    """
    global best
    if r == N - 1:       # 달에 도착
        best = min(best, fuel)
        return
    for d in dirs:
        if d == prev_dir:          # 같은 방향 X
            continue
        nc = c + d
        if 0 <= nc < M:
            dfs(r + 1, nc, d, fuel + board[r + 1][nc])

for start_col in range(M):
    dfs(0, start_col, -2, board[0][start_col])

print(best)