# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#
#     for i in range(len(a)+1):
#         for j in range(1, len(a)):
#             if a[j-1] >= a[j]:
#                 a[j-1], a[j] = a[j], a[j-1]
#
#     max_sum = 0
#     min_sum = 0
#
#         max_sum += a[::-1][i]
#
#     for i in range(M):
#         min_sum += a[i]
#
#     result = max_sum - min_sum
#
#     print(f'#{tc} {result}')

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # 구간합의 변화량을 기록할 리스트 change를 생성한다. 최초값도 포함시키기 위해 0이 필요하다.
    change = [0]
    for i in range(N - M):
        change.append(change[i] - a[i] + a[i + M]) # change[i] 를 포함시켜 누적시키는 것

    # change 리스트에서 최댓값과 최솟값 탐색 = > 구간합의 최대 최소와 헷갈리지 않기.
    max = change[0]
    min = change[0]
    for m in range(len(change)):
        if change[m] > max:
            max = change[m]
        elif change[m] < min:
            min = change[m]

    answer = max - min
    print(f'#{tc + 1} {answer}')

