import sys
sys.stdin = open("input3.txt")

num_of_squares = int(input())
squares = []
areas = []
board = [[True] * 1001 for _ in range(1001)]

for _ in range(num_of_squares):
    squares.append(list(map(int, input().split())))

for square in squares[-1::-1]:
    area = 0
    for x in range(square[0], square[0] + square[2]):
        for y in range(square[1], square[1] + square[3]):
            if board[y][x]:
                area += 1
                board[y][x] = False
    areas.insert(0, area)

for area in areas:
    print(area)

# 53점
# 그런데 100점인 python 3 코드가가 있나??
