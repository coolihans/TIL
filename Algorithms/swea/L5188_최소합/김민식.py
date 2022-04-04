from collections import deque
import sys
sys.stdin = open('input.txt')


stack = deque()
def dfs(row, col, temp_sum):
    global min_sum
    temp_sum += arr[row][col]
    # 가지치기
    if temp_sum > min_sum:
        return
    # 재귀 종료
    if row == N-1 and col ==N-1:
        min_sum = temp_sum
    # 재귀호출
    if row + 1 < N:
        dfs(row+1, col, temp_sum)
    if col + 1 < N:
        dfs(row, col+1, temp_sum)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10 * N**2
    # 가지치기 효율성을 위해 dfs사용
    dfs(0, 0, 0)

    print(f'#{tc+1} {min_sum}')
