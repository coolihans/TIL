import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    time = sorted(time,key=lambda x: x[1])

    cnt = 0
    i = 0
    while i<len(time)-1:

        if time[i][1] <= time[i+1][0]:
            cnt+=1
            i+=1
        else:
            time.remove(time[i+1])

    print(f'#{t+1} {cnt+1}')