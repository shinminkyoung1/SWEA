# boj 2664: 촌수계산
from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(a, b):
    queue = deque([a])
    visited[a] = 0

    while queue:
        people = queue.popleft()
        visited[a] = 0

        if people == b:
            return visited[b]

        for i in graph[people]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[people] + 1
    return -1

print(bfs(x, y))


