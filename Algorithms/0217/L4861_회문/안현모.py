import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def get_pelindrome(m, N, M):
    i = 0
    j = 0
    # 가로로 확인
    for i in range(N):
        for j in range(N-M+1):
            row_word = []
            col_word = []
            for k in range(M):
                row_word += m[i][j+k]       # i,j 를 바꿔 넣으면 가로세로 양쪽이 가능. 인덱스에러도 한 방에 해결
                col_word += m[j+k][i]
            if row_word == row_word[::-1]:
                result = row_word
            if col_word == col_word[::-1]:
                result = col_word

    return result


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = list(input() for _ in range(N))
    get_pelindrome(matrix, N, M)
    print(f'#{tc} {"".join(get_pelindrome(matrix, N, M))}')

# import sys
# sys.stdin = open('input.txt')
#
#
# def palindrome(word):
#     for i in range(len(word) // 2):
#         if word[i] != word[-1 - i]:
#             return False
#         else:
#             return True
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     word_board = list(input() for _ in range(N)) # list(input().split() for _ in range(N))
#     palindrome_list = []
#     if N == M:
#         for row in word_board:
#             if palindrome(row):
#                 palindrome_list.append(row)
#         for column in range(len(word_board)):
#             temp = ''
#             for row in range(len(word_board)):
#                 temp += word_board[row][column]
#             if palindrome(temp):
#                 palindrome_list.append(temp)
#         print(f'#{tc} {palindrome_list[0]}')
#
#     else:
#         for row in word_board:
#             for i in range(N - M + 1):
#                 if palindrome(row[i:M + i]):
#                     palindrome_list.append((row[i:M + i]))
#         for column in range(N - M + 1):
#             temp = ''
#             for row in range(N - M + 1):
#                 temp += word_board[row][column]
#             if palindrome(temp):
#                 palindrome_list.append(temp)
#         print(f'#{tc} {palindrome_list[0]}')