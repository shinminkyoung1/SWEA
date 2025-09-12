# 1953. [모의 SW 역량테스트] 탈주범 검거

import sys
from collections import deque

input = sys.stdin.readline

# 각 파이프 타입이 연결될 수 있는 방향을 정의 (상, 하, 좌, 우)
pipe_types = {
    1: [(0, 1), (0, -1), (1, 0), (-1, 0)],
    2: [(1, 0), (-1, 0)],
    3: [(0, 1), (0, -1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)],
}

def solve():
    N, M, R, C, L = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    
    # 방문 여부를 기록할 2차원 배열
    visited = [[False] * M for _ in range(N)]
    
    # BFS 사용
    q = deque()
    # 시작 지점 
    if tunnel_map[R][C] == 0:
        return 0
        
    q.append((R, C, 1)) # (행, 열, 시간)
    visited[R][C] = True
    count = 1

    while q:
        r, c, time = q.popleft()

        # 시간 제한
        if time == L:
            continue

        # 현재 위치의 파이프 타입
        current_pipe_type = tunnel_map[r][c]
        
        # 현재 파이프에서 갈 수 있는 방향 탐색
        for dr, dc in pipe_types[current_pipe_type]:
            nr, nc = r + dr, c + dc
            
            # 맵의 범위를 벗어나지 않고, 아직 방문하지 않은 곳인지 확인
            if not (0 <= nr < N and 0 <= nc < M and not visited[nr][nc]):
                continue

            # 이동할 곳에 파이프가 있는지 확인
            next_pipe_type = tunnel_map[nr][nc]
            if next_pipe_type == 0:
                continue

            # 현재 파이프와 다음 파이프가 연결되는지 확인
            # 다음 파이프가 현재 파이프 방향으로 연결 부위가 있는지 체크
            if (-dr, -dc) in pipe_types[next_pipe_type]:
                visited[nr][nc] = True
                q.append((nr, nc, time + 1))
                count += 1
                
    return count

T = int(input())
for test_case in range(1, T + 1):
    result = solve()
    print(f"#{test_case} {result}")