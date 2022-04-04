import sys
sys.stdin = open('input.txt')

import itertools

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    numbers = [i for i in range(1, N)]
    perm = list(itertools.permutations(numbers, len(numbers)))

    my_min = N * 100
    for p in perm:
        index = [0] + list(p) + [0]
        current = 0
        for i in range(len(index)-1):
            current += matrix[index[i]][index[i+1]]
        if my_min > current:
            my_min = current

    print(f'#{tc} {my_min}')
