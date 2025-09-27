# 달팽이 배열
# 1. 안에서 밖으로

def spiral_from_center(n: int):
    """센터에서 시작해 좌→하→우→상 순으로 나선 채우기 (센터는 0 유지)"""
    arr = [[0]*n for _ in range(n)]
    y = x = n // 2           # 시작: 중앙
    num = 0                  # 채울 값 (센터는 0 유지)
    dist = 1                 # 한 번에 이동할 칸 수
    d_idx = 0                # 현재 방향 인덱스 (0:좌,1:하,2:우,3:상)
    dy=[0,1,0,-1]
    dx=[-1,0,1,0]
    # 전체 칸 n*n 중, 센터를 비워 두면 채워야 할 칸은 n*n - 1
    while num < n*n - 1:
        # 같은 dist로 두 번 진행하면(좌→하) dist를 1 늘리는 패턴
        for _ in range(2):
            _dy=dy[d_idx]
            _dx=dx[d_idx]
            for _ in range(dist):
                y += _dy
                x += _dx
                if 0 <= y < n and 0 <= x < n:
                    num += 1
                    arr[y][x] = num
            d_idx = (d_idx + 1) % 4
        dist += 1
    return arr

arr=spiral_from_center(5)

for i in range(len(arr)):
    print(arr[i])