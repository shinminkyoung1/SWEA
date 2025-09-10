# 5653. [모의 SW 역량테스트] 줄기세포배양

import sys
import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    initial_cells = [list(map(int, input().split())) for _ in range(N)]

    # 우선순위 큐(최소 힙). 형식: (활성화될 시간, 행, 열, 생명력)
    pq = []
    # 점유된 모든 셀. 형식: {(행, 열): 죽는 시간}
    occupied_cells = {}

    # 초기 세포 정보 저장
    for r in range(N):
        for c in range(M):
            if initial_cells[r][c] > 0:
                life = initial_cells[r][c]
                # (활성화 시간, r, c, 생명력)
                heapq.heappush(pq, (life, r, c, life))
                # 이 세포가 죽는 시간 = 비활성 시간 + 활성 시간
                occupied_cells[(r, c)] = life * 2

    # K시간 동안 시뮬레이션
    for time in range(1, K + 1):
        breeding_candidates = {}

        # 현재 시간에 활성화될 모든 세포를 처리
        while pq and pq[0][0] == time:
            _, r, c, life = heapq.heappop(pq)
            
            # 활성화된 세포는 번식을 시작
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in occupied_cells:
                    current_max_life = breeding_candidates.get((nr, nc), 0)
                    breeding_candidates[(nr, nc)] = max(current_max_life, life)

        # 번식 후보들을 확정하고, 다음 활성화 이벤트를 힙에 추가
        for (r, c), life in breeding_candidates.items():
            # 번식한 세포는 (현재 시간+1)에 생성되어 life시간 동안 비활성
            new_activation_time = time + 1 + life
            heapq.heappush(pq, (new_activation_time, r, c, life))
            
            # 새로 점유된 셀의 죽는 시간 기록
            occupied_cells[(r, c)] = time + 1 + (life * 2)

    # 최종 세포 수 계산
    alive_count = 0
    for death_time in occupied_cells.values():
        if death_time > K:
            alive_count += 1
            
    print(f"#{test_case} {alive_count}")