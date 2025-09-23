# boj 2667: 단지번호붙이기
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            if grid[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                count += 1
    return count

N = int(input())
grid = [list(map(int, input())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

ans = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == False:
            ans.append(bfs(i, j))
print(len(ans))
for i in sorted(ans):
    print(i)