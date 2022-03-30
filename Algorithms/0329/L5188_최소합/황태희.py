import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0:
                if j == 0:
                    dp[i][j] = matrix[i][j]
                dp[i][j] = dp[i][j-1] + matrix[i][j]

            elif j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]

            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    print(f'#{tc} {dp[-1][-1]}')
