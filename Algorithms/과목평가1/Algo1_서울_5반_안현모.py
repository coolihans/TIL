def get_max(lst):
    max_v = lst[0]
    for i in range(1, len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]

    return max_v


T = int(input())

for tc in range(1, T+1):
    N, k = map(int, input().split())
    matrix = [list(map(int, input().split())) + [0]*(k-1) for _ in range(N)]
    part_sum_lst =[]
    for i in range(N):
        part_sum = 0
        for j in range(i, i+k):
            part_sum += matrix[i][j]
        part_sum_lst.append(part_sum)

    print(f'#{tc} {get_max(part_sum_lst)}')
