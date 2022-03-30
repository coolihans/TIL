import sys
sys.stdin = open('input.txt')


def solution(row, col):
    global temp, my_min
    temp += matrix[row][col]
    # 백트래킹
    if my_min < temp:
        return

    # (row, col)이 마지막 (N-1, N-1)에 도착
    if row == N-1 and col == N-1:
        if my_min > temp:
            my_min = temp
            return

    # 우, 하 방향으로 재귀 돌리며 검사
    for move in moves:
        if 0 <= row + move[0] < N and 0 <= col + move[1] < N:
            solution(row + move[0], col + move[1])
            temp -= matrix[row + move[0]][col + move[1]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    moves = [[0, 1], [1, 0]]  # 우로 이동, 하로 이동
    my_min = 20 * N
    temp = 0
    solution(0, 0)

    print(f'#{tc} {my_min}')
