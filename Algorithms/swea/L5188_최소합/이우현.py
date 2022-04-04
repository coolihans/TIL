import sys
sys.stdin = open('input.txt')


def dfs(now_r, now_c):
    global min_sum, now_sum

    now_sum += mat[now_r][now_c]                            # 현재까지의 합계

    if now_r == N-1 and now_c == N-1:                       # 맨 우측 하단에 도착한 경우,
        if now_sum < min_sum:                               # 최솟값 비교해 갱신
            min_sum = now_sum
        return

    if now_sum >= min_sum:                                  # 도중에 최솟값보다 커지면 중단!
        return

    for move in moves:                                      # 이동은 우측과 하단만,
        new_r, new_c = now_r + move[0], now_c + move[1]
        if 0 <= new_r < N and 0 <= new_c < N:               # mat를 벗어나지 않는 범위에서,
            dfs(new_r, new_c)                               # 새 좌표로 이동!
            now_sum -= mat[new_r][new_c]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    moves = [[0, 1], [1, 0]]
    now_sum = 0
    min_sum = 1700
    dfs(0, 0)
    print(f'#{tc} {min_sum}')