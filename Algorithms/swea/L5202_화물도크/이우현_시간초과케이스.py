import sys
sys.stdin = open('input.txt')


# 경우의 수 다 구하면, 시간 초과!
def dfs(now):
    global ans, cnt

    now_key = ''.join(map(str, now))                        # 중복 방지 딕셔너리, 키 값으로 리스트가 불가능하기 때문에, str로 변환
    visited.setdefault(now_key, 0)                          # 딕셔너리에 키와 벨류 생성(visited[now_key] = 0)
    visited[now_key] = 1                                    # 방문 도장 쾅!
    cnt += 1                                                # 현재까지 화물차 수

    for i in range(N):
        new = containers[i]
        if new[0] >= now[1]:                                # 다음 화물차 스케줄을 소화할 수 있고,
            new_key = ''.join(map(str, new))
            visited.setdefault(new_key, 0)
            if not visited[new_key]:                        # 이미 지나간 화물차가 아니라면,
                dfs(new)                                    # 다음 화물차로 이동!
                visited[new_key] = 0
                cnt -= 1

    if cnt > ans:                                           # 진행할 수 있는 스케줄이 없다면, 최댓값과 비교해,
        ans = cnt                                           # 최댓값 갱신!


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    containers = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for k in range(N):
        visited = {}
        cnt = 0
        dfs(containers[k])
    print(f'#{tc} {ans}')
