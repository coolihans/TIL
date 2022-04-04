import sys
sys.stdin = open('input.txt')


def func(r, c, ssum):
    global answer
    ssum += matrix[r][c]

    # backtracking
    if ssum >= answer:
        return

    # 종료조건
    if (r, c) == (N - 1, N - 1):
        if ssum < answer:
            answer = ssum
            return

    # 오른쪽 or 아래로 이동/ 이동할 수 있는 방향이 하나만 남은 경우 그 방향으로만 이동
    elif r == N - 1:
        func(r, c + 1, ssum)
    elif c == N - 1:
        func(r + 1, c, ssum)
    else:
        func(r, c + 1, ssum)
        func(r + 1, c, ssum)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 250
    func(0, 0, 0)

    print(f'#{tc}', answer)
