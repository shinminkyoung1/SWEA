# boj 5014: 스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()
MAX = 1000000
dist = [0]*(MAX + 1)

def bfs():
    queue.append(S)
    dist[S] = 1
    
    while queue:
        floor = queue.popleft()
        moves = [floor+U, floor-D]

        if floor == G:
            return dist[G]
        
        for next_floor in moves: # moves는 리스트
            if 1<=next_floor<=F and not dist[next_floor]:
                dist[next_floor] = dist[floor] + 1
                queue.append(next_floor)
    return None
                
result = bfs()
if result is None:
    print("use the stairs")
else:
    print(result-1)