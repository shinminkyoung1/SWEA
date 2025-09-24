# boj 1697: 숨바꼭질
from collections import deque

N, K = map(int, input().split())

MAX = 100000
queue = deque()
dist = [0] * (MAX+1)

def bfs():
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            break

        for j in (x-1, x+1, x*2):
            if 0<=j<=MAX and not dist[j]:
                dist[j] = dist[x] + 1
                queue.append(j)

bfs()