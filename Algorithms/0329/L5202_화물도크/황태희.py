import sys
sys.stdin = open('input.txt')


import heapq


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    q = []
    for _ in range(N):
        s, e = map(int, input().split())
        heapq.heappush(q, [e, s])

    t = cnt = 0

    while t <= 24 and q:
        e, s = heapq.heappop(q)

        if s >= t:
            t = e
            cnt += 1

        if t > 24:
            cnt -= 1

    print(f'#{tc} {cnt}')
