import sys
sys.stdin = open('input.txt')


def get_min(r, temp_total):
    global mmin
    if temp_total < mmin:
        if False not in visited:            # 모든 구역을 방문했을 때
            temp_total += matrix[r][0]
            if temp_total < mmin:
                mmin = temp_total
                return

        for i in range(1, N):                           # 모든 구역을 재귀로 방문
            if matrix[r][i] != 0 and not visited[i]:
                visited[i] = True
                get_min(i, temp_total + matrix[r][i])
                visited[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    mmin = 10000
    for i in range(1, N):
        visited = [False] * N
        visited[0] = visited[i] = True      # 0번째는 마지막에 방문하기 위해 True로 초기화
        get_min(i, matrix[0][i])
    print(f'#{tc} {mmin}')
