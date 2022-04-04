import sys
sys.stdin = open("input.txt")


def get_score(lst):
    cnt_max = 0
    score = 0
    for i in range(100, -1, -1):
        cnt = lst.count(i)
        if cnt_max < cnt:
            cnt_max = cnt
            score = i

    return score


T = int(input())

for tc in range(1, T+1):
    t = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {get_score(lst)}')
