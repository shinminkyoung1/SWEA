# [모의 SW 역량테스트] 4013: 특이한 자석

def dfs(number, direction):
    global check
    check[number] = 1

    if number < 3:
        if graph[number][2] != graph[number+1][6] and not check[number+1]:
            dfs(number+1, -1*direction)

    if number > 0:
        if graph[number][6] != graph[number-1][2] and not check[number-1]:
            dfs(number-1, -1*direction)

    if direction == 1:
        graph[number] = [graph[number].pop()] + graph[number]

    else:
        graph[number] = graph[number][1:] + [graph[number][0]]

T = int(input())
for tc in range(T):
    K = int(input())
    graph = [list(map(int, input().split())) for _ in range(4)]
    # 회전 정보
    for _ in range(K):
        number, direction = map(int, input().split())

        check = [0] * 4
        dfs(number-1, direction)


    point = 0
    for i in range(4):
        point += graph[i][0] * 2 ** i
    print(f"#{tc + 1} {point}")