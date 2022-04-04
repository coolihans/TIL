import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    mat = [[100]*(N+1)]+[[100]+list(map(int,input().split())) for _ in range(N)]
    mat[0][0] = mat[0][1] = 0

    for row in range(1,N+1):
         for col in range(1,N+1):
             mat[row][col] += min(mat[row][col-1],mat[row-1][col])  # 위쪽 vs 왼쪽 비교해서 작은값 누적
    print(f'#{t+1} {mat[row][col]}')