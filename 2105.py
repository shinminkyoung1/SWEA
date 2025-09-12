# 2105. [모의 SW 역량테스트] 디저트 카페

import sys

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(r, c, direction, count):

    global max_desserts, start_r, start_c

    for d in range(direction, direction + 2):
        # 4번 이상 안 됨
        if d > 3:
            continue

        nr, nc = r + dr[d], c + dc[d]

        # 시작점으로 돌아와야 사각형 완성됨
        if nr == start_r and nc == start_c:
            # 최댓값 갱신
            max_desserts = max(max_desserts, count)
            return

        # 맵의 범위를 벗어나거나, 이미 먹은 디저트인 경우
        if not (0 <= nr < N and 0 <= nc < N) or desserts[cafe_map[nr][nc]]:
            continue

        # 디저트 먹기 -> 방문 처리
        desserts[cafe_map[nr][nc]] = True

        dfs(nr, nc, d, count + 1)
        # 백트래킹 -> 방문 처리 원상 복구 
        desserts[cafe_map[nr][nc]] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cafe_map = [list(map(int, input().split())) for _ in range(N)]

    max_desserts = -1

    # 모든 지점을 시작점으로 선정
    for r in range(N):
        for c in range(N):
            start_r, start_c = r, c
            # 먹은 디저트 종류를 기록하는 배열 
            desserts = [False] * 101

            # 시작점의 디저트 먹기
            desserts[cafe_map[r][c]] = True
            dfs(r, c, 0, 1)

    print(f"#{test_case} {max_desserts}")