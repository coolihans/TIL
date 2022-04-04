import sys
sys.stdin = open("input.txt")


def get_max(r):
    max_v = r[0]
    for i in range(1, len(r)):
        if max_v < r[i]:
            max_v = r[i]

    return max_v


def get_min_cnt(r, ml):
    for s, e in ml:
        if s % 2 == 1 and e % 2 == 0:
            for i in range(s, e+1):
                r[i] += 1
        if s % 2 == 1 and e % 2 == 1:
            for i in range(s, e+2):
                r[i] += 1
        if s % 2 == 0 and e % 2 == 0:
            for i in range(s-1, e+1):
                r[i] += 1
        if s % 2 == 0 and e % 2 == 1:
            for i in range(s-1, e+2):
                r[i] += 1
    min_cnt = get_max(r)

    return min_cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [0] * 401
    move_lst = []
    for _ in range(N):
        [start, end] = map(int, input().split())
        if start >= end:
            start, end = end, start
        move_lst.append([start, end])

    print(f'#{tc} {get_min_cnt(rooms, move_lst)}')