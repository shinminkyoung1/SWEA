# # boj 2573: 빙산
# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(N)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def bfs(x, y, visited):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not visited[nx][ny] and grid[nx][ny] > 0: # 녹지 않은 곳
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#
# year = 0
# while True:
#     # 작업 A
#     visited = [[False] * M for _ in range(N)]
#     iceberg_count = 0
#
#     for i in range(N):
#         for j in range(M):
#             if not visited[i][j] and grid[i][j] > 0:
#                 bfs(i, j, visited) # 새로운 덩어리
#                 iceberg_count += 1
#
#     if iceberg_count >= 2:
#         print(year)
#         break
#     if iceberg_count == 0:
#         print(0)
#         break
#
#     # 작업 B
#     # 각 칸이 얼마나 녹을지 먼저 계산
#     melt_info = [[0] * M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j] > 0: # 녹지 않은 것에 대해
#                 sea_count = 0
#                 for k in range(4):
#                     ni, nj = i + dx[k], j + dy[k]
#                     if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 0:
#                         sea_count += 1
#                 melt_info[i][j] = sea_count
#
#     for i in range(N):
#         for j in range(M):
#             grid[i][j] = max(0, grid[i][j] - melt_info[i][j])
#     year += 1
#
# # 작업 A: 빙산 덩어리 개수 세기
#     # 덩어리가 2개 이상이면, 결과 출력
#     # 덩어리가 0개이면 (모두 녹았으면) 0을 출력
# # 작업 B: 빙산 녹이기
#     # 덩어리가 1개라면, 1년 동안 빙산을 녹임
#     # 빙산을 녹일 때, 현재 grid 수정 x (모든 루프를 돌기 전에 결과가 영향을 받을 수 있음)

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M:
                if not visited[next_x][next_y] and grid[next_x][next_y] > 0:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))


# 1. 최초 빙산 위치 목록을 루프 시작 전에 한 번만 생성
iceberg_locations = []
for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            iceberg_locations.append((i, j))

year = 0
while True:
    visited = [[False] * M for _ in range(N)]
    iceberg_count = 0
    # 현재 빙산 목록만 순회
    for i, j in iceberg_locations:
        if not visited[i][j]:
            bfs(i, j, visited)
            iceberg_count += 1

    if iceberg_count >= 2:
        print(year)
        break
    if iceberg_count == 0:
        print(0)
        break

    melt_info = [[0] * M for _ in range(N)]
    # 현재 빙산 목록만 순회하여 녹는 양 계산
    for i, j in iceberg_locations:
        sea_count = 0
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 0:
                sea_count += 1
        melt_info[i][j] = sea_count

    # 2. 다음 해의 빙산 목록을 담을 리스트 준비
    next_iceberg_locations = []
    for i, j in iceberg_locations:
        grid[i][j] = max(0, grid[i][j] - melt_info[i][j])
        # 녹고 난 후에도 빙산이 남아있으면 다음 목록에 추가
        if grid[i][j] > 0:
            next_iceberg_locations.append((i, j))

    # 3. 빙산 목록을 다음 해의 것으로 교체
    iceberg_locations = next_iceberg_locations
    year += 1