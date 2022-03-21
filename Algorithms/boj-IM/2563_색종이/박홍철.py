import sys
sys.stdin = open("input.txt")

board = [[0] * 100 for _ in range(100)]

num_of_paper = int(input())

for _ in range(num_of_paper):
    x, y = map(int, input().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            board[i][j] += 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] > 0:
            result += 1
print(result)


