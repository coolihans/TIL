import sys
sys.stdin = open("input.txt")

def color_matrix(start_x, start_y, end_x, end_y, color):
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            matrix[i][j] += color
    return matrix

def cnt_purple(matrix):
    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [[0 for _ in range(10)] for _ in range(10)]

    for _ in range(n):
        start_x, start_y, end_x, end_y, color = map(int, input().split())
        matrix = color_matrix(start_x, start_y, end_x, end_y, color)

    print(f'#{tc} {cnt_purple(matrix)}')
