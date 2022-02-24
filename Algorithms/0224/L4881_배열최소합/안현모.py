import sys
sys.stdin = open("input.txt")


def f(i, m):
    # global 선언
    global min_sum
    global tmp_sum

    # 이미 tmp_sum 이 이전 min_sum 보다 커지면 발 빼야됨. == 백트래킹
    if tmp_sum > min_sum:
        return

    # 다 더한 값을 이전 합과 비교
    if i == N:
        if tmp_sum <= min_sum:
            min_sum = tmp_sum        # min_sum 이 첫 path 에선 100이라서 무조건 진행
        return

    for j in range(N):
        if visited[j] == 0:         # 안 가본 col 일 경우
            visited[j] = 1          # 가 본 것으로 바꾸고
            tmp_sum += m[i][j]      # 더 해주고
            f(i + 1, m)             # 다음 줄로 넘어가기
            visited[j] = 0          # 돌아와서 초기화 시켜주기
            tmp_sum -= m[i][j]      # 이것도 직전 상황으로 초기화// 0으로 하면안됨


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N       # col 수만큼 3개만 필요
    tmp_sum = 0
    min_sum = 100           # 처음 값 선언 100보다 커질 수 없음.
    f(0, matrix)

    print(f'#{tc} {min_sum}')




# import sys
# sys.stdin = open('input.txt')
#
#
# def perm(lst, i, N):
#     global answer
#     global ssum
#
#     if i == N:
#         answer = ssum
#         return
#
#     for j in range(i, N):
#         lst[i], lst[j] = lst[j], lst[i]
#         ssum += matrix[i][lst[i]]
#         if ssum < answer:
#             perm(lst, i + 1, N)
#         ssum -= matrix[i][lst[i]]
#         lst[i], lst[j] = lst[j], lst[i]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     lst1 = [i for i in range(N)]
#     ssum = 0
#     answer = 0
#     for i in range(N):
#         answer += matrix[i][i]
#
#     perm(lst1, 0, N)
#     print(f'#{tc}', answer)
