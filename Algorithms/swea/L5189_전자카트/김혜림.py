# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
# 1번은 사무실을, 2번부터 N번은 관리구역 번호
# 1-2-3-1, 1-3-2-1
import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    lst = list(range(2, N+1))
    perms = list(permutations(lst))
    
    min_fee = 1000000000000
    for p in perms:
        tmp_fee = 0
        for idx in range(N-1):
            if idx == 0:
                tmp_fee += arr[1][p[idx]]
            if idx == N-2:
                tmp_fee += arr[p[idx]][1]
            else:
                tmp_fee += arr[p[idx]][p[idx+1]]
        if tmp_fee < min_fee:
            min_fee = tmp_fee
    
    print(f'#{tc} {min_fee}')
    