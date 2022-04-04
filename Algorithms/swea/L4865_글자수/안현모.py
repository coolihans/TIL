import sys
sys.stdin = open('input.txt', encoding='UTF-8')


# s1 이 비교할 문자열. s2 가 비교 당하는 문자열
def get_max_cnt(s1, s2):
    max_cnt = 0
    for i in range(len(s1)):
        cnt = 0
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                cnt += 1
        if max_cnt <= cnt:
            max_cnt = cnt

    return max_cnt


T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    N = len(str1)
    M = len(str2)
    result = get_max_cnt(str1, str2)

    print(f'#{tc} {result}')
