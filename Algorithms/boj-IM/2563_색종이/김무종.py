import sys
sys.stdin = open('input.txt')

metrix = [[0 for i in range(100)] for _ in range(100)]
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            metrix[row][col] = 1

cnt = 0
for row in range(100):
    for col in range(100):
        if metrix[row][col] >= 1:
            cnt += 1
print(cnt)