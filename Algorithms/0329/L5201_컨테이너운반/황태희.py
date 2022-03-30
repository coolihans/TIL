import sys
sys.stdin = open('input.txt')


import heapq


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_N = list(map(lambda x: -int(x), input().split()))
    list_M = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(list_M)
    heapq.heapify(list_N)

    answer = 0
    while list_N and list_M:
        n, m = -heapq.heappop(list_N), -heapq.heappop(list_M)
        while list_N and n > m:
            n = -heapq.heappop(list_N)
        if n > m:
            break
        else:
            answer += n

    print(f'#{tc} {answer}')
