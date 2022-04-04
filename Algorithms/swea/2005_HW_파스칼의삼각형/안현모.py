import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tri = [[1] * i for i in range(1, N+1)]

    for i in range(1, N-1):     # 가장 아랫줄 위까지만
        for j in range(i):
            tri[i+1][j+1] = tri[i][j] + tri[i][j+1]

    print(f'#{tc}')
    for i in tri:
        print(*i)
