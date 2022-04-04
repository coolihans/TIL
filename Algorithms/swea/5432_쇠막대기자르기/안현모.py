import sys
sys.stdin = open('input.txt')


def cnt_stick(lst):
    cnt = total = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            cnt += 1
        else:
            if lst[i-1] == "(":
                cnt -= 1
                total += cnt
            else:
                cnt -= 1
                total += 1
    return total


T = int(input())

for tc in range(1, T+1):
    lst = input()

    print(f'#{tc} {cnt_stick(lst)}')
