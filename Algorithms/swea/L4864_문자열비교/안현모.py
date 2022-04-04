import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def is_include(s1, s2):
    for i in range(len(s2) - len(s1) + 1):
        check_str = []
        for j in range(len(s1)):
            check_str += s2[i+j]
        if check_str == s1:
            return 1

    return 0


T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())

    is_include(str1, str2)
    print(f'#{tc} {is_include(str1, str2)}')

# result = 0
#     for i in range(len(str2)-len(str1)+1):
#         if str2[i:i+len(str1)] == str1:
#             result = 1
# 이렇게 슬라이싱 해서 비교 하는게 깔끔한 것 같기도.