import sys
sys.stdin = open('input3.txt')

width, height = map(int, input().split())
directions = ["right", "down", "left", "up"]
target = int(input())
metrix = [[0] * height for i in range(width)]
row = 0
col = 0
final_row = 1
final_col = 1
direction = 0
idx = 1
if target > width * height:
    print(0)
else:
    while idx <= target:
        if directions[direction] == 'right':
            metrix[row][col] = idx
            if idx == target:
                final_row += row
                final_col += col
            col += 1
            idx += 1
            if col >= height or metrix[row][col] != 0:
                col -= 1
                row += 1
                direction = 1

        elif directions[direction] == 'down':
            metrix[row][col] = idx
            if idx == target:
                final_row += row
                final_col += col
            row += 1
            idx += 1
            if row >= width or metrix[row][col] != 0:
                col -= 1
                row -= 1
                direction = 2

        elif directions[direction] == 'left':
            metrix[row][col] = idx
            if idx == target:
                final_row += row
                final_col += col
            col -= 1
            idx += 1
            if col < 0 or metrix[row][col] != 0:
                row -= 1
                col += 1
                direction = 3


        elif directions[direction] == 'up':
            metrix[row][col] = idx
            if idx == target:
                final_row += row
                final_col += col
            row -= 1
            idx += 1
            if row < 0 or metrix[row][col] != 0:
                row += 1
                col += 1
                direction = 0

    print(final_row, final_col)
