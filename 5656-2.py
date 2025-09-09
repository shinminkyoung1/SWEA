# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())
b, c = map(int, input().split())
d = float(input())
e, f, g = map(float, input().split())
h = input()
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)
print(b, end = " ")
print(c, d, e)
print(f)
'''

import sys
from collections import deque
from copy import deepcopy

'''
     아래의 구문은 input.txt 를 read only 형식으로 연 후,
     앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
     여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
     아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

     따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
     아래 구문을 사용하기 위해서는 import sys가 필요합니다.

     단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

# --- 알고리즘에 필요한 함수 정의 ---

# 연쇄 폭발을 처리하는 함수 (BFS 사용)
def explode(start_r, start_c, board, W, H):
    q = deque([(start_r, start_c, board[start_r][start_c])])
    board[start_r][start_c] = 0 # 처음 맞은 벽돌은 바로 제거

    while q:
        r, c, power = q.popleft()
        
        # 벽돌의 파워만큼 연쇄 폭발 처리
        if power > 1:
            # 상하 방향
            for i in range(1, power):
                nr_up, nr_down = r - i, r + i
                if 0 <= nr_up < H and board[nr_up][c] > 0:
                    q.append((nr_up, c, board[nr_up][c]))
                    board[nr_up][c] = 0
                if 0 <= nr_down < H and board[nr_down][c] > 0:
                    q.append((nr_down, c, board[nr_down][c]))
                    board[nr_down][c] = 0
            # 좌우 방향
            for i in range(1, power):
                nc_left, nc_right = c - i, c + i
                if 0 <= nc_left < W and board[r][nc_left] > 0:
                    q.append((r, nc_left, board[r][nc_left]))
                    board[r][nc_left] = 0
                if 0 <= nc_right < W and board[r][nc_right] > 0:
                    q.append((r, nc_right, board[r][nc_right]))
                    board[r][nc_right] = 0

# 폭발 후 벽돌을 아래로 내리는 함수 (중력 적용)
def apply_gravity(board, W, H):
    for c in range(W):
        stack = []
        for r in range(H):
            if board[r][c] > 0:
                stack.append(board[r][c])
        
        for r in range(H):
            board[r][c] = 0

        row_idx = H - 1
        while stack:
            board[row_idx][c] = stack.pop()
            row_idx -= 1

# 남은 벽돌 개수를 세는 함수
def count_bricks(board, W, H):
    count = 0
    for r in range(H):
        for c in range(W):
            if board[r][c] > 0:
                count += 1
    return count

# 모든 경우의 수를 탐색하는 메인 재귀 함수 (DFS)
def solve(n, board, N, W, H):
    global min_remaining
    
    # 가지치기: 이미 남은 벽돌이 0이면 더 탐색할 필요가 없음
    if min_remaining == 0:
        return

    # 종료 조건: N개의 구슬을 모두 사용했을 때
    if n == N:
        remaining = count_bricks(board, W, H)
        min_remaining = min(min_remaining, remaining)
        return

    # 재귀 실행: W개의 모든 열에 구슬을 쏴보는 경우를 시도
    can_shoot = False
    for c in range(W):
        # 쏠 벽돌 찾기
        r = -1
        for i in range(H):
            if board[i][c] > 0:
                r = i
                break
        
        # 쏠 벽돌이 있는 경우
        if r != -1:
            can_shoot = True
            # 다음 재귀를 위해 현재 상태를 깊은 복사
            next_board = deepcopy(board)
            
            # 시뮬레이션: 폭발 -> 중력
            explode(r, c, next_board, W, H)
            apply_gravity(next_board, W, H)
            
            # 다음 구슬 쏘기 (재귀 호출)
            solve(n + 1, next_board, N, W, H)

    # 조기 종료 조건: 구슬이 남았는데 더 이상 쏠 벽돌이 없는 경우
    if not can_shoot:
        remaining = count_bricks(board, W, H)
        min_remaining = min(min_remaining, remaining)
        return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
    '''
    N, W, H = map(int, input().split())
    initial_board = [list(map(int, input().split())) for _ in range(H)]
    
    # 각 테스트 케이스마다 최솟값을 저장할 변수 초기화
    min_remaining = W * H

    # 0번째 구슬부터 시작해서 모든 경우의 수 탐색
    solve(0, initial_board, N, W, H)
    
    print(f"#{test_case} {min_remaining}")
    # ///////////////////////////////////////////////////////////////////////////////////