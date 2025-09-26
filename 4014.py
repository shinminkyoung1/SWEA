# [모의 SW 역량테스트] 4014: 활주로 건설

def check_slope(row):
    count = 1
    for i in range(1, N):
        if row[i] == row[i-1]:
            count += 1
        elif row[i] - row[i-1] == 1 and count >= X:
            count = 1
        elif row[i] - row[i-1] == -1 and count >= 0: # 낮아지면
            count = -X+1
        else:
            return 0

    if count >= 0:
        return 1
    return 0

T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    A = []
    result = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        result += check_slope(A[i])

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(A[j][i])
        result += check_slope(temp)

    print(f"#{tc+1} {result}")