import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    home_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home_lst.append([i, j])
    answer = 0
    for i in range(N):
        for j in range(N):
            for k in range(N+1, 0, -1):
                cnt = 0
                for home in home_lst:
                    if abs(i-home[0])+abs(j-home[1]) < k:
                        cnt += 1
                if cnt*M >= k**2 + (k-1)**2:
                    if answer < cnt:
                        answer = cnt

    print(f'#{tc} {answer}')

