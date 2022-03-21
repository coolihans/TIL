import sys
sys.stdin = open('input.txt')

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

M = [[0]*100 for _ in range(100)]
cnt = 0

for i in range(N):
    for j in range(100-P[i][1], 100-P[i][1]-10, -1):
        for k in range(P[i][0], P[i][0]+10):
            M[j][k] = 1
for i in range(100):
    cnt += sum(M[i])
print(cnt)