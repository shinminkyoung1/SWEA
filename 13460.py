# boj 13460: 구슬탈출 2

from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dx, dy):
    move_count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_count += 1
    return x, y, move_count


def bfs():
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set([(rx, ry, bx, by)])

    while queue:
        crx, cry, cbx, cby, count = queue.popleft()

        if count >= 10:
            continue

        for i in range(4):
            nrx, nry, r_move = move(crx, cry, dx[i], dy[i])
            nbx, nby, b_move = move(cbx, cby, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                print(count + 1)
                return

            if nrx == nbx and nry == nby:
                if r_move > b_move:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, count + 1))

    print(-1)

bfs()