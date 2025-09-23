# boj 2606: 바이러스
from collections import deque

def dfs(start_node):
    visited[start_node] = True

    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)

N = int(input())
M = int(input())
# 2차원 배열
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 확인
visited = [False] * (N+1)
dfs(1)
cnt = visited.count(True) - 1
print(cnt)
