import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(n, cnt):
    q = deque()
    q.append([n, 0])
    visited = set()
    visited.add(n)

    while q:
        # 현재 값, 횟수 뽑기
        n, cnt = q.popleft()
        # 결과에 도달
        if n == M:
            break

        if n + 1 not in visited and n + 1 <= 1000000:
            q.append([n+1, cnt+1])
            visited.add(n+1)

        if n - 1 not in visited and 0 < n - 1 <= 1000000:
            q.append([n - 1, cnt+1])
            visited.add(n + 1)

        if n * 2 not in visited and n * 2 <= 1000000:
            q.append([n * 2, cnt+1])
            visited.add(n * 2)

        if n - 10 not in visited and 0 < n - 10 <= 1000000:
            q.append([n - 10, cnt+1])
            visited.add(n - 10)
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N, 0)}')


