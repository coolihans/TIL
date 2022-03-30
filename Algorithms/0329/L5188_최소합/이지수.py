import sys
sys.stdin = open('input.txt')


T = int(input())


def dfs(row, col):
    global total, pathsum
    dx, dy = [1, 0], [0, 1] # 우, 하로만 이동 가능
    if total < pathsum:
        return
    if row == N - 1 and col == N - 1: # 도착점 도착
        total = pathsum
        return
    for dir in range(2):
        nx, ny = row + dx[dir], col + dy[dir]
        if 0 <= nx < N and 0 <= ny < N and [nx, ny] not in visited:
            visited.append((nx, ny))
            pathsum += arr[nx][ny]
            dfs(nx, ny)
            visited.remove((nx, ny))
            pathsum -= arr[nx][ny]


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 999999
    pathsum = arr[0][0]
    visited = []
    dfs(0,0)
    print(f'#{tc} {total}')