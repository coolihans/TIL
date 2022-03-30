from itertools import permutations
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = list(permutations([i for i in range(1, N)])) # (N-1)! 에 해당하는 순열 리스트

    results = 1000
    for P_set in P: # 순열에서 하나 꺼내서 돌아주기
        sum_result = 0
        r = 0       # 0에서부터 시작해줘서
        for c in P_set:  # 0-1 1-2 2-3 3-4 for문으로 돌고
            sum_result += arr[r][c]
            r = c
        sum_result += arr[r][0]  # 4-0 이런식으로 끝나게
        if sum_result <= results: # 현재 더한 값이 기존 값보다 작으면 갱신
            results = sum_result

    print(f'#{tc} {results}')
