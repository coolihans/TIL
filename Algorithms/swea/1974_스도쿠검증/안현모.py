import sys
sys.stdin = open('input.txt')


def check_col_row(s, lst):
    for i in range(9):
        row_lst = []
        col_lst = []
        for j in range(9):
            row_lst.append(s[i][j])
            col_lst.append(s[j][i])
        row_lst = sorted(row_lst)
        col_lst = sorted(col_lst)
        if row_lst == lst and col_lst == lst:
            continue
        else:
            return 0
    return 1

def check_box(s, sl, lst):
    for [i, j] in sl:
        box_lst = []
        for k in range(3):
            for m in range(3):
                box_lst.append(s[i+k][j+m])
        box_lst = sorted(box_lst)
        if box_lst == lst:
            continue
        else:
            return 0
    return 1

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_lst = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    print(f'#{tc} {check_box(sudoku,start_lst, lst) and check_col_row(sudoku,lst)}')
