# 이동 중 벽에 부딪혀서 방향이 전환되는 경우
# d: 1 = 위, 2 = 아래, 3 = 오른쪽, 4 = 왼쪽

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

# 행, 열, 속도, 방향, 전체 행, 전체 열 (s는 이동해야 할 칸 수를 의미)
def move(r, c, s, d, R, C):
    if d in (1, 2):
        # 객체가 한쪽 끝에서 반대쪽 끝까지 갔다가 다시 원래 자리로 돌아오는 데 필요한 총 이동 횟수
        cycle = 2 * (R - 1) if R > 1 else 1
        # 순수 이동량 계산
        steps = s % cycle

        for _ in range(steps):
            if r == 0 and d == 1: # 맨 위에서 위로 가려면 튕겨서 아래로
                d = 2
            elif r == R - 1 and d == 2: # 맨 아래에서 아래로 가려면 튕겨서 위로
                d = 1
            r += dr[d]

    else:
        cycle = 2 * (C - 1) if C > 1 else 1
        steps = s % cycle

        for _ in range(steps):
            if c == 0 and d == 4:
                d = 3
            elif c == C - 1 and d == 3:
                d = 4
            c += dc[d]
    return r, c, d
