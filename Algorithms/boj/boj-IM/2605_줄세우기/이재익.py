N = int(input())
T = list(map(int, input().split()))
K = [0]*N
for i in range(N):
    if T[i] == 0:
        K[i] = i+1
    if T[i] > 0:
        for j in range(i, i-T[i], -1):
            K[j] = K[j-1]
        K[i-T[i]] = i+1
for i in range(N):
    print(K[i], end=' ')