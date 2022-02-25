import sys
sys.stdin = open("input.txt")


def get_samepass(p):
    p = p - 15 * share
    return p


def get_min(lst):
    min_v = lst[0]
    for i in range(1, len(lst)):
        if min_v > lst[i]:
            min_v = lst[i]
    return min_v


for tc in range(1, 11):
    _ = int(input())
    password = list(map(int, input().split()))
    min_v = get_min(password)
    share = min_v // 15
    samepass = list(map(get_samepass, password))

    k = 1
    while 1:
        tmp = samepass.pop(0) - k
        if tmp <= 0:
            tmp = 0
            samepass.append(tmp)
            break
        else:
            samepass.append(tmp)
        k += 1
        if k == 6:
            k = 1

    print(f'#{tc}', end=' ')
    print(*samepass)
