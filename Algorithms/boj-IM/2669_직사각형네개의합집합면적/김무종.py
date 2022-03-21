import sys
sys.stdin = open('input.txt')

metrix = [[0 for i in range(101)] for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            metrix[row][col] = 1

cnt = 0
for row in range(101):
    for col in range(101):
        if metrix[row][col] >= 1:
            cnt += 1
print(cnt)