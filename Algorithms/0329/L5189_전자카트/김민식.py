from itertools import permutations
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    energy = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 100 * N**2
    for course in permutations(range(1, N), N-1):
        temp_sum = 0
        to_visit = [0]
        to_visit.extend(course)
        to_visit.append(0)
        for i in range(N):
            temp_sum += energy[to_visit[i]][to_visit[i + 1]]
            if temp_sum > min_sum:
                break
        else:
            min_sum = temp_sum

    print(f'#{tc+1} {min_sum}')
