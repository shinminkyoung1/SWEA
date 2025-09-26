# [모의 SW 역량테스트] 5656: 벽돌 깨기
from collections import deque
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def destroy_bricks(current_grid, x, y):
    if current_grid[y][x] == 0:
        return

    queue = deque([(x, y, current_grid[y][x])])
    current_grid[y][x] = 0 # 터진 건 0으로 바꿈

    while queue:
        cx, cy, power = queue.popleft()

        if power > 1:
            for i in range(4):
                for p in range(1, power):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0<=nx<W and 0<=ny<H and current_grid[ny][nx] != 0:
                        current_grid[ny][nx] = 0

def apply_gravity(current_grid):
    for x in range(W):
        temp_col = []
        for y in range(H-1, -1, -1):
            if current_grid[y][x] > 0:
                temp_col.append(current_grid[y][x])

        for y in range(H-1, -1, -1):
            if temp_col:
                current_grid[y][x] = temp_col.pop()
            else:
                current_grid[y][x] = 0

def count_bricks(current_grid):
    count = 0
    for y in range(H):
        for x in range(W):
            if current_grid[y][x] > 0:
                count += 1

    return count

def solve(count, current_grid):
    global min_bricks

    # 시도 횟수 확인
    if count == N:
        remaining = count_bricks(current_grid)
        min_bricks = min(remaining, min_bricks)
        return

    # 어디에 던질 지 확인
    for x in range(W):
        new_grid = copy.deepcopy(current_grid)

        top_bricks_y = -1
        for y in range(H):
            if new_grid[y][x] > 0:
                top_bricks_y = y
                break

        if top_bricks_y != -1:
            destroy_bricks(new_grid, x, top_bricks_y)
            apply_gravity(new_grid)

        solve(count+1, new_grid)

T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    min_bricks = float('inf') # 일단 초기화

    solve(0, grid) # 시도 횟수

    print(f"#{tc+1} {min_bricks}")