import sys
sys.stdin = open("input.txt")

T = 10

# def get_start_point(matrix, i, j):
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j] == 2:
#                 break
#
#     return i, j

for tc in range(1, T+1):
    t = int(input())
    N = 100
    i = 0
    j = 0
    matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    i = 99
    j = 0
    for x in range(N+2):
        if matrix[99][x] == 2:
            j = x
            break
    di = [0, 0, -1]
    dj = [-1, 1, 0]
    direction = 0

    while i > 0:
        if matrix[i][j-1]:
            direction = 0
            while True:
                i += di[direction]
                j += dj[direction]
                if matrix[i][j-1] == 0:
                    break

        elif matrix[i][j+1]:
            direction = 1
            while True:
                i += di[direction]
                j += dj[direction]
                if matrix[i][j+1] == 0:
                    break
        direction = 2
        i += di[direction]
        j += dj[direction]

    print(f'#{tc} {j-1}')
