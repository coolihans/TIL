import sys
sys.stdin = open('input.txt')


def solve(now):
    global answer, cnt, tmp
    visited[now] = 1
    cnt += 1
    # 정답 조건
    if cnt == N:
        tmp += battery[now][1]
        if tmp < answer:
            answer = tmp
        tmp -= battery[now][1]
        return

    for i in range(1, N+1):
        if not visited[i]:
            tmp += battery[now][i]
            solve(i)
            tmp -= battery[now][i]
            visited[i] = 0
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery = [[0]*(N+1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]
    visited = [0]*(N+1)
    tmp = 0
    cnt = 0
    answer = 123123123
    solve(1)
    print(f'#{tc} {answer}')