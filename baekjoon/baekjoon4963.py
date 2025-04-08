import sys
sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y, w, h, graph):
    graph[y][x] = 0  # 방문처리
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
            dfs(nx, ny, w, h, graph)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(j, i, w, h, graph)
                cnt += 1
    print(cnt)
