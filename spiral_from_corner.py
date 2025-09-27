# 달팽이 배열
# 2. 밖에서 안으로

def spiral_from_corner(n: int):
    arr = [[0] * n for _ in range(n)]
    y = x = 0 # (0, 0)에서 시작
    num = 1
    dirs = [[0, 1], (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상
    d_idx = 0

    top, left, bottom, right = 0, 0, n-1, n-1
    while top <= bottom and left <= right:
        # 우
        for c in range(left, right+1):
            arr[top][c] = num; num += 1
        top += 1

        # 하
        for r in range(top, bottom+1):
            arr[r][right] = num; num += 1
        right -= 1
        if top > bottom or left > right: break

        # 좌
        for c in range(right, left-1, -1):
            arr[bottom][c] = num; num += 1
        bottom -= 1

        # 상
        for r in range(bottom, top-1, -1):
            arr[r][left] = num; num += 1
        left += 1
    return arr

arr=spiral_from_corner(5)

for i in range(len(arr)):
    print(arr[i])