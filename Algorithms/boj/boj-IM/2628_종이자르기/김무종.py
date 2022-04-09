import sys
sys.stdin = open('input.txt')

def row_cut(number, row):
    row.append(number)
    row.sort()
    return row
def col_cut(number, col):
    col.append(number)
    col.sort()
    return col



width, height = map(int, input().split())
T = int(input())
row = [0, height]
col = [0, width]
for i in range(T):
    direction, number = map(int, input().split())
    if direction == 0:
        row = row_cut(number, row)
    else:
        col = col_cut(number, col)

max_sum = 0
for i in range(1, len(row)):
    tmp_row = row[i] - row[i-1]
    for j in range(1, len(col)):
        tmp_col = col[j] - col[j-1]
        if max_sum < tmp_row * tmp_col:
            max_sum = tmp_row * tmp_col
print(max_sum)