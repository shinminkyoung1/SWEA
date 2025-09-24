# boj 7569: 토마토
from collections import deque

# M: 가로(x), N: 세로(y), H: 높이(z)
M, N, H = map(int, input().split())
# 3차원 격자 생성: grid[z][y][x] 순서로 접근
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [0, 0, 1, -1, 0, 0]  # x좌표(가로) 변화량
dy = [1, -1, 0, 0, 0, 0]  # y좌표(세로) 변화량
dz = [0, 0, 0, 0, 1, -1]  # z좌표(높이) 변화량

queue = deque()


# BFS 함수
def bfs():
    while queue:
        # 1. 큐에서 꺼낼 때 z, y, x 순서로 일관성 유지
        z, y, x = queue.popleft()

        # 6방향 탐색
        for i in range(6):
            # 다음 좌표 계산: dx는 x에, dy는 y에, dz는 z에 적용
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]

            # 2. 범위 확인 수정: next_x는 M, next_y는 N, next_z는 H와 비교
            if 0 <= next_x < M and 0 <= next_y < N and 0 <= next_z < H:
                # 3. 격자 접근 순서 수정: grid[z][y][x]
                if grid[next_z][next_y][next_x] == 0:
                    grid[next_z][next_y][next_x] = grid[z][y][x] + 1
                    # 4. 큐에 추가할 때 순서 유지
                    queue.append((next_z, next_y, next_x))


# 시작 토마토(1)를 찾아서 큐에 넣기 (z, y, x 순서로 순회)
for z in range(H):
    for y in range(N):
        for x in range(M):
            if grid[z][y][x] == 1:
                queue.append((z, y, x))

# BFS 실행
bfs()

cannot_complete = False
day = 0
# 결과 확인
for z_plane in grid:
    for y_row in z_plane:
        for tomato in y_row:
            if tomato == 0:
                cannot_complete = True
            day = max(day, tomato)

if cannot_complete:
    print(-1)
else:
    print(day - 1)