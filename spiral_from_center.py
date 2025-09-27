# 달팽이 배열

# 1. 밖에서 안으로
def spiral_from_center(n: int):
    arr = [[0] * n for _ in range(n)]
    y = x = n // 2
    num = 0
    dist = 1
    d_idx = 0
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    while num < n*n -1:
        for _ in range(2):
            _dy = dy[d_idx]
            _dx = dx[d_idx]

            for _ in range(dist):
                y += _dy
                x += _dx
                if 0 <= y < n and 0 <= x < n:
                    num += 1
                    arr[y][x] = num
            d_idx = (d_idx + 1) % 4 # 방향 바꾸고 한 번 더
        dist += 1 # 두 번 씩 하고 거리 늘림
    return arr
arr = spiral_from_center(5)

for i in range(len(arr)):
    print(arr[i])