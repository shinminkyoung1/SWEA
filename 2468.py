# boj 2468: 안전영역
from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            if not visited[next_x][next_y] and grid[next_x][next_y] > h:
                visited[next_x][next_y] = True
                queue.appendleft((next_x, next_y))

max_safe_zones = 0

max_height = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] > max_height:
            max_height = grid[i][j]

for h in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    current_safe_zones = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > h:
                bfs(i, j, h, visited)
                current_safe_zones += 1

    if current_safe_zones > max_safe_zones:
        max_safe_zones = current_safe_zones

if max_safe_zones == 0:
    print(1)
else:
    print(max_safe_zones)