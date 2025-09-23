# boj 2178: 미로 탐색
from collections import deque

N, M = map(int, input().split())

# 2차원 격자 받기
grid = [list(map(int, input())) for _ in range(N)]

queue = deque([(0, 0)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:
            if grid[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                grid[next_x][next_y] = grid[x][y] + 1

print(grid[N-1][M-1])