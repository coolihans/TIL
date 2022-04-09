import sys

sys.stdin = open("input.txt")

heights = [int(input()) for _ in range(9)]

heights.sort()

full_height = sum(heights)

for i in range(9):
    for j in range(1, 9-i):
        if full_height - heights[i] - heights[i+j] == 100:
            fake1 = i
            fake2 = i+j
            break

for k in range(9):
    if k != fake1 and k != fake2:
        print(heights[k])
