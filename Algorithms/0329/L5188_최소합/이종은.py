import sys
sys.stdin = open('input.txt', 'r')

def dfs(r, c):
    global result, min_result

    # 현재 좌표에 해당하는 값 result에 더하기
    result += arr[r][c]

    # 구해놓은 최소합을 이미 초과한다면 return
    if result > min_result:
        return

    if r == N-1 and c == N-1:
        if result < min_result:
            min_result = result
        return

    for dr, dc in [[0, 1], [1, 0]]:
        nr, nc = r + dr, c + dc
        if N > nr >= 0 and N > nc >= 0:
            dfs(nr, nc)
            result -= arr[nr][nc]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    min_result = 1000
    dfs(0, 0)
    print(f'#{tc} {min_result}')