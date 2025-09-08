import sys
from collections import deque
from copy import deepcopy

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# 연쇄 폭발을 처리하는 함수 (BFS 사용)
def explode(start_r, start_c, board, W, H):
    q = deque([(start_r, start_c)])
    
    while q:
        r, c = q.popleft()
        power = board[r][c]
        
        # 이미 폭발한 벽돌은 건너뜀 (추가)
        if power == 0:
            continue
            
        # 현재 벽돌 제거
        board[r][c] = 0
        
        # 폭발 범위가 1보다 클 경우 연쇄 반응 처리
        if power > 1:
            # 상하 방향 폭발
            for i in range(1, power):
                nr = r + i
                if 0 <= nr < H and board[nr][c] > 0:
                    q.append((nr, c))
                nr = r - i
                if 0 <= nr < H and board[nr][c] > 0:
                    q.append((nr, c))
            # 좌우 방향 폭발
            for i in range(1, power):
                nc = c + i
                if 0 <= nc < W and board[r][nc] > 0:
                    q.append((r, nc))
                nc = c - i
                if 0 <= nc < W and board[r][nc] > 0:
                    q.append((r, nc))

# 폭발 후 벽돌을 아래로 내리는 함수
def apply_gravity(board, W, H):
    for c in range(W):
        # 0이 아닌 벽돌들만 임시 스택에 저장
        stack = []
        for r in range(H):
            if board[r][c] > 0:
                stack.append(board[r][c])
        
        # 해당 열을 0으로 초기화
        for r in range(H):
            board[r][c] = 0
        
        # 스택의 벽돌을 아래부터 다시 채워넣음
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

def solve(n, board, N, W, H):
    global min_remaining
    
    # N개의 구슬을 모두 사용한 경우
    if n == N:
        remaining = count_bricks(board, W, H)
        min_remaining = min(min_remaining, remaining) # 최솟값을 찾은 경우 갱신
        return

    # W개의 모든 열에 구슬을 떨어뜨리는 경우를 시도 (완전탐색)
    for c in range(W):
        # 다음 단계를 위한 현재 보드 상태를 deepcopy (추가)
        next_board = deepcopy(board)
        
        # c열의 가장 위에 있는 벽돌 찾기
        r = -1
        for i in range(H):
            if next_board[i][c] > 0:
                r = i
                break
        
        # 해당 열에 벽돌이 없는 경우 건너뜀
        if r == -1:
            continue
            
        # 1. 폭발
        explode(r, c, next_board, W, H)
        
        # 2. 중력 적용
        apply_gravity(next_board, W, H)
        
        # 3. 다음 구슬 쏘기 (재귀 호출)
        solve(n + 1, next_board, N, W, H)
        
    # 만약 모든 열이 비어있어서 구슬을 한 번도 못 쐈을 경우,
    # 현재 상태로 남은 벽돌 수를 계산
    if not any(board[r][c] > 0 for r in range(H) for c in range(W)):
         min_remaining = 0
         return
    # 만약 n < N인데 더 이상 깰 벽돌이 없다면, 현재 상태로 종료
    if all(sum(row) == 0 for row in board):
        min_remaining = 0
        return
    if n < N and count_bricks(board, W, H) > 0 and c == W - 1 and r == -1:
        remaining = count_bricks(board, W, H)
        min_remaining = min(min_remaining, remaining)
        return

# 입력 
T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    initial_board = [list(map(int, input().split())) for _ in range(H)]
    
    total_bricks = count_bricks(initial_board, W, H)
    min_remaining = total_bricks

    solve(0, initial_board, N, W, H)
    
    print(f"#{t} {min_remaining}")