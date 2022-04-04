import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    _ = input()
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    row_sum_list = []
    col_sum_list = []
    dia_sum_list = []
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += matrix[i][j]
        row_sum_list.append(row_sum)
    for i in range(N):
        col_sum = 0
        for j in range(N):
            col_sum += matrix[j][i]
        col_sum_list.append(col_sum)

    dia_sum = 0
    for i in range(N):
        dia_sum += matrix[i][i]
    dia_sum_list.append(dia_sum)

    dia_sum = 0
    for i in range(N):
        dia_sum += matrix[i][N-1-i]
    dia_sum_list.append(dia_sum)

    max_sum = max(row_sum_list + col_sum_list + dia_sum_list)

    print(f'#{tc} {max_sum}')
