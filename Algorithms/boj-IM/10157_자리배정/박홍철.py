import sys
sys.stdin = open("input3.txt")

width, height = map(int, input().split())
number = int(input())

if number > width * height:
    print(0)
    exit()

board = [[True] * width for _ in range(height)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
d = 0
location = [0, 0]
board[location[0]][location[1]] = False

for _ in range(number-1):
    if not (0 <= location[0] + di[d % 4] < height and 0 <= location[1] + dj[d % 4] < width and board[location[0] + di[d % 4]][location[1] + dj[d % 4]]):
        d += 1
    location = [location[0] + di[d % 4], location[1] + dj[d % 4]]
    board[location[0]][location[1]] = False

print(f'{location[1] + 1} {location[0] + 1}')

# 풀리긴 하지만 시간 너무 오래 걸려 빠듯했음(테스트 당 거의 1초)
