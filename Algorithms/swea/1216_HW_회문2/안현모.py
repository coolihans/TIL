import sys
sys.stdin = open('input.txt', encoding='UTF-8')
# 가장 긴 회문... 사다리 문제 같이... 뒤에서부터? 100짜리 있는지 확인. 99짜리 확인 98 짜리 확인 ...


def get_longest_pelindrome_length(m, N):
    answer = 100
    N = 100
    while answer > 1:
        for i in range(N):
            for j in range(N - answer + 1):
                test_row = []
                test_col = []
                for k in range(answer):
                    test_row += m[i][j+k]
                    test_col += m[j+k][i]
                if test_row == test_row[::-1] or test_col == test_col[::-1]:
                    return answer
        answer -= 1


T = 10
for tc in range(1, T+1):
    N = 100
    test_num = int(input())
    matrix = [list(input()) for _ in range(N)]    # 왜 안됐지
    print(f'#{tc} {get_longest_pelindrome_length(matrix, N)}')


# import sys
# sys.stdin = open('input.txt', encoding='UTF-8')
#
# def get_longest_pelindrome_length(m, N):
#     answer = 100
#     N = 100
#     while answer > 1:
#         for i in range(N):
#             for j in range(N - answer + 1):
#                 test_row = []
#                 test_col = []
#                 for k in range(answer):
#                     test_row += m[i][j+k]
#                     test_col += m[j+k][i]
#                 if test_row == test_row[::-1] or test_col == test_col[::-1]:
#                     return answer
#         answer -= 1
#
#
# T = 10
# for tc in range(1, T+1):
#     N = 100
#     test_num = int(sys.stdin.readline())
#     matrix = [sys.stdin.readline().strip() for _ in range(N)]   # 왜 안됐지
#     print(f'#{tc} {get_longest_pelindrome_length(matrix, N)}')