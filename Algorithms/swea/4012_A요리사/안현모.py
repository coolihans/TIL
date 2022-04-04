import sys
sys.stdin = open('input.txt')


def DFS(n, lstA, lstB):
    global ans
    # 종료 조건
    if n == N:
        if len(lstA) == len(lstB):
            asum = bsum = 0
            x = len(lstA)
            for i in range(x):
                for j in range(x):
                    asum += synergy[lstA[i]][lstA[j]]
                    bsum += synergy[lstB[i]][lstB[j]]
            if ans > abs(asum - bsum):
                ans = abs(asum - bsum)
        return
    # A 음식에 추가, B 음식에 추가.
    DFS(n+1, lstA + [n], lstB)
    DFS(n + 1, lstA, lstB + [n])


T = int(input())
for testcase in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    ans = 123123123
    DFS(0, [], [])
    print(f'#{testcase} {ans}')
