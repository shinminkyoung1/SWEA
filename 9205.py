# boj 9205: 맥주 마시면서 걸어가기
from collections import deque

def bfs():
    n = int(input())
    locations = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        locations.append((x, y))

    # bfs 시작
    visited = [False] * (n+2)

    queue = deque([0])
    visited[0] = True # 집 방문 처리

    while queue:
        current = queue.popleft()

        if current == n+1: # 페스티벌 인덱스
            print("happy")
            return

        for next_idx in range(n+2):
            if not visited[next_idx]:
                dist = abs(locations[current][0] - locations[next_idx][0]) + abs(locations[current][1] - locations[next_idx][1])

                if dist <= 1000:
                    visited[next_idx] = True
                    queue.append(next_idx)

    print("sad")
    return

t = int(input())
for _ in range(t):
    bfs() # 테스트 케이스가 나뉘니까 아예 bfs 안에서 해결하고 출력할 수 있도록