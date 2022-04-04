import sys
from itertools import permutations
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    combi_list = list(permutations(list(range(2,N+1)),N-1))
    min_result = float('inf')
    for c in combi_list:
        c = [1]+list(c)
        c.append(1)
        result = 0

        for i in range(len(c)-1):
            result += matrix[c[i]-1][c[i+1]-1]
            if result>min_result:
                break

        if result < min_result:
            min_result = result

    print(f'#{t+1} {min_result}')

