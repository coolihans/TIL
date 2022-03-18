from collections import deque
import sys
sys.stdin = open('input.txt')


def BFS(N, M, si, sj, L):
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append([si, sj])
    visited[si][sj] = 1
    cnt = 1
    while queue:
        ci, cj = queue.popleft()
        if visited[ci][cj] == L:
            return cnt
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                queue.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1
                cnt += 1
    return cnt


T = int(input())
for testcase in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0],
            [1, 0, 1, 0]]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    opp = [1, 0, 3, 2]
    ans = BFS(N, M, R, C, L)
    print(f'#{testcase} {ans}')
