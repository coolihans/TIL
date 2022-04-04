import sys
sys.stdin = open("input.txt")


def cnt_search(end_page, target_p):
    cnt = 0
    l = 1
    r = end_page
    for _ in range(10):
        cnt += 1
        middle = int((l + r)/2)
        if middle == target_p:
            break
        elif middle < target_p < r:
            l = middle
        elif l < target_p < middle:
            r = middle

    return cnt


T = int(input())

for tc in range(1, T+1):
    end_page, Pa, Pb = map(int, input().split())

    cnt_a = cnt_search(end_page, Pa)
    cnt_b = cnt_search(end_page, Pb)

    if cnt_a < cnt_b:
        winner = 'A'
    elif cnt_b < cnt_a:
        winner = 'B'
    elif cnt_a == cnt_b:
        winner = 0

    print(f'#{tc} {winner}')
