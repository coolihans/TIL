import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 3, 4
    matrix = [[0]*N for _ in range(N)]  # 빈 정사각 행렬 생성 후 진행

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]      # 우 하 좌 상 순서 (시계 방향)
    i = 0
    j = 0
    way = 0     # 첫 방향 설정을 위해
    for idx in range(N*N):
        matrix[i][j] = idx + 1
        i = i + di[way]
        j = j + dj[way]
        # 1. 인덱스 벗어나거나 숫자가 이미 있을 경우 다시 제자리로
        # 2. 방향 전환 way + 1
        if i < 0 or i >= N or j < 0 or j >= N or matrix[i][j] != 0:
            i -= di[way]
            j -= dj[way]
            way = (way+1) % 4   # 0 1 2 3 을 순환
            # 3. 여기서 진행을 한 칸 시켜줘야 됨.
            i = i + di[way]
            j = j + dj[way]

    print(f'#{tc}')
    for i in matrix:
        print(*i)

    # if 에서 만족하는 경우로 했더니 잘 안돼서 만족 못하는 경우로 수정...




#     def get_sorted(numbers, N):
#     for i in range(N-1):
#         idx = i
#         if i % 2 == 0:
#             for j in range(i+1, N):
#                 if numbers[idx] < numbers[j]:
#                     idx = j
#             numbers[i], numbers[idx] = numbers[idx], numbers[i]
#         else:
#             for j in range(i+1, N):
#                 if numbers[idx] > numbers[j]:
#                     idx = j
#             numbers[i], numbers[idx] = numbers[idx], numbers[i]
#     return ' '.join(map(str, numbers[:10]))
#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr_len = int(input())
#     numbers = list(map(int, input().split()))
#     print(f'#{tc}', get_sorted(numbers, arr_len))
