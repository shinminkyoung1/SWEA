# 2112. [모의 SW 역량테스트] 보호 필름

import sys


def check_performance(film):
    for c in range(W):
        max_consecutive = 1
        current_consecutive = 1
        for r in range(1, D):
            if film[r][c] == film[r - 1][c]:
                current_consecutive += 1
            else:
                current_consecutive = 1
            max_consecutive = max(max_consecutive, current_consecutive)
        
        # 한 열이라도 K개 연속이 안 되면 실패
        if max_consecutive < K:
            return False
            
    # 모든 열이 통과하면 성공
    return True

def inject_chemicals_dfs(depth, selected_rows, chemicals):
    if depth == len(selected_rows):
        # 원본 필름을 깊은 복사하여 임시 필름 생성
        temp_film = [row[:] for row in film_original]
        
        for i in range(len(selected_rows)):
            row_idx = selected_rows[i]
            chemical = chemicals[i]
            temp_film[row_idx] = [chemical] * W
        
        # 성능 검사 수행
        if check_performance(temp_film):
            return True # 통과
        return False

    # A(0)를 주입하는 경우
    chemicals[depth] = 0
    if inject_chemicals_dfs(depth + 1, selected_rows, chemicals): return True
    
    # B(1)를 주입하는 경우
    chemicals[depth] = 1
    if inject_chemicals_dfs(depth + 1, selected_rows, chemicals): return True
    
    return False

def choose_rows_dfs(start_idx, count, selected_rows):
    if count == d:
        chemicals = [0] * d
        if inject_chemicals_dfs(0, selected_rows, chemicals):
            return True # 최종 성공
        return False

    # 조합
    for i in range(start_idx, D):
        if choose_rows_dfs(i + 1, count + 1, selected_rows + [i]):
            return True
            
    return False

T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    film_original = [list(map(int, input().split())) for _ in range(D)]

    for d in range(K + 1):
        if d == 0:
            if check_performance(film_original):
                ans = 0
                break
            else:
                continue

        if choose_rows_dfs(0, 0, []): 
            ans = d
            break
    
    print(f"#{test_case} {ans}")