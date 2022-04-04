import sys
sys.stdin = open('input.txt')


def get_min_sum(r, c, temp):
    global mmin
    if temp > mmin:         # 이미 구한 최소합보다 클 경우
        return

    if r == N - 1 and c == N - 1:       # 오른쪽 아래에 도착한 경우
        temp += matrix[r][c]            # 마지막 지점의 숫자도 더한 후 최소값 비교
        if mmin > temp:
            mmin = temp
            return

    if 0 <= r < N and 0 <= c < N and not visited[r][c]:     # 완전 탐색
        visited[r][c] = True
        get_min_sum(r + 1, c, temp + matrix[r][c])
        visited[r][c] = False
        get_min_sum(r, c + 1, temp + matrix[r][c])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    mmin = 260              # 3 <= N <= 13
    get_min_sum(0, 0, 0)
    print(f'#{tc} {mmin}')
