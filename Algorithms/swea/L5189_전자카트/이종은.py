import sys
sys.stdin = open('input.txt', 'r')


def dfs(_from, _to, cost):
    global min_cost, office

    # _from에서 _to로 이동할 때 필요한 배터리 사용량 cost +=
    cost += arr[_from][_to]
    # _from에서 왔으므로 방문 표시
    visited[_from] = 1

    # 종료 조건
    # N*N 배열이므로 N개의 층이 있는 건물이라고 가정할 때 N개의 층을 모두 방문했으면 return
    # 지금까지 구한 배터리 사용량이 최소 사용량을 넘어서도 return
    if sum(visited) == N or cost > min_cost:
        # 다음 목적지가 오피스면 최소 배터리 사용량 비교 후 갱신
        if _to == office and cost < min_cost:
            min_cost = cost
        return

    # _to 층에서 갈 수 있는 다음 목적지 탐색
    for _next in range(N):
        # 0이면 안되고, 직전 층으로 되돌아가면 안되고, 방문한 적이 없는 층이면 탐색 재개
        if arr[_to][_next] != 0 and _next != _from and not visited[_to]:
            dfs(_to, _next, cost)
            visited[_to] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1000

    # 오피스는 최상층에 위치
    for office in range(0, 1):
        for sector in range(1, N):
            if arr[office][sector] != 0:
                # 이미 갔던 층은 생략하기 위한 visited
                visited = [0] * N
                dfs(office, sector, 0)

    print(f'#{tc} {min_cost}')