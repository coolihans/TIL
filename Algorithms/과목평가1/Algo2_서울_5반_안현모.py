import sys
sys.stdin = open("algo2_sample_in.txt")


def get_box_sum(m):
    if N < 3:
        box_sum = [0]
        return box_sum
    else:
        center_lst = []
        for i in range(2, N):
            for j in range(2, N):
                center_lst.append([i, j])

        box_sum = 0
        box_sum_lst = []
        for i, j in center_lst:
            for k in range(-1, 2):
                for l in range(-1, 2):
                    box_sum += m[i+k][j+l]
            box_sum_lst.append(box_sum)
        return box_sum_lst


def get_sec_sum_lst(m):
    center_lst = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            center_lst.append([i, j])
    sec_sum_lst = []
    for i, j in center_lst:
        sec_sum = 0
        n = m[i][j]

        for k in range(1-n, n):
            sec_sum += m[i][j+k]
            sec_sum += m[i+k][j]
        sec_sum -= m[i][j]
        sec_sum_lst.append(sec_sum)
    return sec_sum_lst


def get_max(lst):
    max_v = lst[0]
    for i in range(1, len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]

    return max_v


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    m = [0]*(N+1)
    matrix = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    box_sum_lst = get_box_sum(matrix)
    second_sum_lst = get_sec_sum_lst(matrix)
    total_lst = box_sum_lst + second_sum_lst
    answer = get_max(total_lst)
    print(f'#{tc} {answer}')
