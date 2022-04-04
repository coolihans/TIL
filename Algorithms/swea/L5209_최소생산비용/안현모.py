import sys
sys.stdin = open('input.txt')


def dfs(n, tmp):
    global answer

    if n == N:
        if answer > tmp:
            answer = tmp
        return

    if answer < tmp:
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            dfs(n+1, tmp + matrix[n][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    answer = 123123123
    dfs(0, 0)
    print(f'#{tc} {answer}')

