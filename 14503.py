# boj 14503: 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, d):
    cnt = 0
    while True:
        if area[x][y] == 0:
            area[x][y] = -1
            cnt += 1

        for _ in range(4):
            d = (d-1) % 4 # 방향 전환
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<N and 0<=ny<M and area[nx][ny] == 0:
                x, y = nx, ny
                break
        else:
            x, y = x + dx[d] * (-1), y + dy[d] * (-1)
            if 0<=x<N and 0<=y<M and area[x][y] == 1 or not 0<=x<N and 0<=y<M :
                print(cnt)
                return

bfs(r, c, d)