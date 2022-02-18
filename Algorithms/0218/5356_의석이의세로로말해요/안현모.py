import sys
sys.stdin = open('input.txt')

def get_v_word(m, N):
    words = ''
    for j in range(max_len):
        for i in range(N):
            if len(m[i]) <= j:
                continue
            else:
                words += m[i][j]

    return words


T = int(input())

for tc in range(1, T+1):
    N = 5
    matrix = [input() for _ in range(N)]
    max_len = len(matrix[0])
    for i in range(N):
        if len(matrix[i]) >= max_len:
            max_len = len(matrix[i])

    print(f'#{tc} {get_v_word(matrix, N)}')