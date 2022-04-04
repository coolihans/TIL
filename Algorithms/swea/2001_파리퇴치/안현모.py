import sys
sys.stdin = open("input.txt")


def get_start_points(N, M):
    start_points = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            start_points.append([i, j])

    return start_points

def get_max_v(arr):
    max_v = arr[0]
    for i in range(1, len(arr)):
        if max_v < arr[i]:
            max_v = arr[i]

    return max_v
# 시작점을 다 구하고 (list)
# 시작점에서 이중 for 문 돌려서 합 구하고??
# 합들의 리스트에서 가장 큰 값 찾기.


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    start_points = get_start_points(N, M)
    sum_list = []

    for start_point in start_points:
        i = start_point[0]
        j = start_point[1]
        sum_m = 0
        for a in range(M):
            for b in range(M):
                sum_m += matrix[i + a][j + b]

        sum_list.append(sum_m)

    print(f'#{tc} {get_max_v(sum_list)}')




