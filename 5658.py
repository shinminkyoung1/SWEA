# [모의 SW 역량테스트] 5658: 보물상자 비밀번호

# 리스트 슬라이싱

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = list(input())

    turn = N // 4
    result_set = set()

    for _ in range(turn): # 원점으로 돌아올 때까지 회전
        for i in range(0, N, turn):
            num_str = ''.join(A[i:i+turn]) # 당시 회전에서 나올 수 있는 수들
            result_set.add(int(num_str, 16)) # 다시 하나로 만들기

        A.insert(0, A.pop())

    sorted_result = sorted(list(result_set), reverse=True)
    print("{} {}".format(tc+1, sorted_result[K-1]))