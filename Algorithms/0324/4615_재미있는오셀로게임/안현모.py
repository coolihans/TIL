import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N//2][N//2] = 2
    arr[N//2 + 1][N//2+1] = 2
    arr[N//2 + 1][N//2] = 1
    arr[N//2][N//2 + 1] = 1
    directions = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1))
    for _ in range(M):
        si, sj, saek = map(int, input().split())
        arr[si][sj] = saek
        for di, dj in directions:
            tmp_lst = []
            for k in range(1, N):
                ni, nj = si + di*k, sj + dj*k
                if 1 <= ni <= N and 1 <= nj <= N:
                    if arr[ni][nj] == 0:
                        break
                    elif arr[ni][nj] == saek:
                        for ci, cj in tmp_lst:
                            arr[ci][cj] = saek
                        break
                    else:
                        tmp_lst.append([ni, nj])
                else:
                    break
    cnt1, cnt2 = 0, 0
    for lst in arr:
        cnt1 += lst.count(1)
        cnt2 += lst.count(2)

    print(f'#{tc} {cnt1} {cnt2}')

