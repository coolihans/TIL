from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
# 단지의 이름(번호 네이밍)은 필요 없네
def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    map[i][j] = 0   # 없애 버려서 방문 처리
    cnt = 1     # 처음 집 세고 들어감

    while queue:
        si, sj = queue.popleft()
        for di, dj in direction:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and map[ni][nj]:
                queue.append((ni, nj))
                map[ni][nj] = 0    # 방문 처리
                cnt += 1
    cnt_lst.append(cnt)


N = int(input())
map = [list(map(int, input())) for _ in range(N)]

town_num = 0    # 단지 수
cnt_lst = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            bfs(i, j)
            town_num += 1

print(town_num)
for i in sorted(cnt_lst):
    print(i)