import sys
sys.stdin = open('input.txt')


from itertools import permutations


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ways = list(permutations(range(1, N), N-1))
    answer = float('inf')

    for way in ways:
        now = 0
        tmp = 0
        for position in way:
            tmp += matrix[now][position]
            now = position
        tmp += matrix[now][0]
        answer = min(answer, tmp)

    print(f'#{tc} {answer}')
