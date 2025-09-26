# [모의 SW 역량테스트] 5653: 줄기세포배양

from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

T=int(input())

for t in range(1,T+1):
    N,M,K=map(int,input().split())

    room=[]
    visited=dict()
    sell_num=0
    #1. 먼저 줄기세포를 방아준다
    for x in range(N):
        tmp=list(map(int,input().split()))
        for y in range(M):
            if tmp[y]>0:
                sell_num=max(sell_num,tmp[y])

        room.append(tmp)
    #sell=[deque()]*(sell_num+1)로하니, 모든 큐에 좌표가 다 넣어져서 수정
    sell=[deque()for _ in range(sell_num+1)]

    for x in range(N):
        for y in range(M):
            if room[x][y]>0:

                num=room[x][y]

                sell[num].append((x,y))
                visited[x,y]=[0,num]

    #2 줄기세포 번식
    for time in range(0,K):
        # print(time)
        # print(sell)
        for go in range(sell_num,0,-1):

            #직접 노트에 활성화되는 규칙을 찾아본 결과
            #(생명력+1)*K+(생명력) 주기로 활성화되더라고요.
            flag=(time-go)%(go+1)

            if flag==0:
                tmp=set()

                for _ in range(len(sell[go])):
                    x,y=sell[go].popleft()

                    for d in range(4):
                        nx=x+dx[d]
                        ny=y+dy[d]

                        if visited.get((nx,ny)):
                            continue

                        visited[nx,ny]=[time,go]
                        tmp.add((nx,ny))

                for tx,ty in tmp:
                    sell[go].append((tx,ty))

    cnt=0
    for fx,fy in visited:


        grid=visited.get((fx,fy))
        put_time=grid[0]
        life=grid[1]
        #투입시간+생명력-->활성시간
        #활성시간+생명력+1-->죽음
        #따라서 투입시간+생명력 *2 값이 K보다 크거나 같으면 생존
        if put_time+(life*2)>=K:

            cnt+=1

    print("#%d %d"%(t,cnt))