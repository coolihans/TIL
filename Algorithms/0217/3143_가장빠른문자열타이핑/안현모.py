import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def get_least_cnt(s1, s2):
    cnt = 0
    i = 0
    while i < (len(s2)-len(s1)+1):
        if s2[i:i+len(s1)] == s1:
            cnt += 1
            i += len(s1)
        else:
            i += 1
    total_cnt = len(s2) - cnt*(len(s1)-1)
    return total_cnt


T = int(input())

for tc in range(1, T+1):
    str2, str1 = input().split()

    print(f'#{tc} {get_least_cnt(str1, str2)}')
