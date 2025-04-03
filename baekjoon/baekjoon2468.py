from collections import deque
import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, h, visited, area, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and area[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in area)

result = 0
for height in range(0, max_height):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visited[i][j]:
                bfs(i, j, height, visited, area, n)
                cnt += 1
    result = max(result, cnt)

print(result)