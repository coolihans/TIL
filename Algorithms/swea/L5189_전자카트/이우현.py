import sys
sys.stdin = open('input.txt')


def dfs(now):
    global cnt, battery_power, ans

    visited[now] = 1                        # 방문 도장 쾅!
    cnt += 1                                # 동선 길이 +1

    if cnt == N:                            # 동선이 N만큼 됐다면,
        battery_power += mat[now][1]        # 출발지로 돌아가는 배터리 사용량 더해주고,
        if battery_power < ans:             # 가장 작은 값인지 비교
            ans = battery_power
        battery_power -= mat[now][1]
        return

    for i in range(1, N+1):                 # 동선이 N보다 작을 때,
        if not visited[i]:                  # 방문하지 않았다면,
            battery_power += mat[now][i]    # 배터리 사용량 더해주고,
            dfs(i)                          # 다음 행선지로!
            battery_power -= mat[now][i]
            visited[i] = 0
            cnt -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]   # 상단, 좌측을 0으로 감쌈
    visited = [0] * (N+1)
    battery_power = cnt = 0
    ans = 99999999999999
    dfs(1)
    print(f'#{tc} {ans}')
