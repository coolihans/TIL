import sys
sys.stdin = open('input.txt')

M = [[0]*101 for _ in range(101)]
# X는 N[0] ~ N[2]
# Y는 N[1] ~ N[3]
for i in range(4):
    N = list(map(int, input().split()))
    for i in range(N[1], N[3]): # y축에 대해
        for j in range(N[0], N[2]): #x축에 대해
            M[i][j] = 1
cnt = 0
for i in range(101):
    cnt += sum(M[i])
print(cnt)