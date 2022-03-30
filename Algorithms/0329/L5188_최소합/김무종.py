import sys

sys.stdin = open('input.txt')

def DFS(row, col, tmp):
    global answer
    if row == N-1 and col == N-1:
        answer = min(tmp, answer)
        return
    if tmp > answer:
        return
    to_visits = [[row, col]]
    while to_visits:
        current_row, current_col = to_visits.pop()
        for i in range(2):
            next_row, next_col = current_row+dxs[i][0], current_col+dxs[i][1]
            if 0<=next_row<N and 0<=next_col<N:
                DFS(next_row, next_col, tmp+matrix[next_row][next_col])


dxs = [(1, 0), (0, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000
    DFS(0, 0, matrix[0][0])
    print(f'#{tc}', answer)
