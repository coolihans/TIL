import sys
sys.stdin = open('input.txt')


def solution(start):
    global time, my_max

    if my_max < time:
        my_max = time

    for t in range(start+1, len(trucks)):
        if temp[-1][1] <= trucks[t][0]:
            temp.append(trucks[t])
            time += 1
            solution(t)
            time -= 1
            temp.pop()
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort()

    my_max = 1
    for i in range(N-1):
        trucks = times[i:N]
        temp = [times[i]]
        time = 1
        solution(0)

    print(f'#{tc} {my_max}')
