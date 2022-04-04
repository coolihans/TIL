import sys
sys.stdin = open("input.txt")


def solve(N, M, K):
    visit_time = list(map(int, input().split()))
    visit_time = sorted(visit_time)
    now = 0  # 시각
    fish = 0
    while now <= 11111:
        now += M
        fish += K
        if visit_time[0] < M:
            return "Impossible"
        for i in range(N):
            if now <= visit_time[i] < now + M:
                fish -= 1
        if fish < 0:
            return "Impossible"
    return "Possible"


T = int(input())
for tc in range(1, T+1):
    # N, M, K = 사람수, M초의 시간 동안 K개의 붕어빵
    N, M, K = map(int, input().split())
    result = solve(N, M, K)
    print(f'#{tc} {result}')


# 한번에 해야 되네..