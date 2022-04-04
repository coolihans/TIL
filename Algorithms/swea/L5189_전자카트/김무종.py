import sys
sys.stdin = open('input.txt')
# 유형 완전탐색/ 모든 순열 구하기
def DFS(current, tmp, step):
    global answer
    if step == N:
        # 방문 싹 다 했을 경우는 tmp에다가 matrix[current][0]을 더해줌(visited의 모든 원소가 1일시 마지막 값을 누락했었기 때문)
        answer = min(answer, tmp+matrix[current][0])
        return
    for _next in range(1, N):
        if visited[_next] == 0:
            # 간 곳은 방문 안하게 설정
            visited[_next] = 1
            # next를 방문했다고 표시. 그 후 현재 위치를 next로 변경 후 tmp 에다가 matrix[current][next]를 더함
            DFS(_next, tmp+matrix[current][_next], step+1)
            visited[_next] = 0
            # 다음 반복을 위해 초기화


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    # 사무실은 idx 0으로 고정, 갈 곳은 1부터 n-1까지
    answer = 1000
    DFS(0, 0, 1)
    print(f'#{tc}', answer)


