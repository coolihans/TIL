import sys
sys.stdin = open('input.txt')


def DFS(n, ssum):
    global ans
    if ssum >= B+ans:
        return
    if n == N:
        # 종료 조건
        if ssum >= B and ans > ssum - B:
            ans = ssum - B
        return
    DFS(n+1, ssum + lst[n])
    DFS(n+1, ssum)


T = int(input())
for testcase in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))   # 점원들의 키 리스트 순서대로
    ans = 12345678
    DFS(0, 0)
    print(f'#{testcase} {ans}')
