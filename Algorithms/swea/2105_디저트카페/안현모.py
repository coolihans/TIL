import sys
sys.stdin = open("input.txt")

direction = ((1, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
def solve(dir, ci, cj, v, cnt):
    global si, sj, answer
    # 종료조건
    if dir > 3:
        return
    # 정답 체크 조건 dir == 3,
    if dir == 3 and ci == si and cj == sj and answer < cnt:
        answer = cnt
    for k in range(dir, dir + 2):
        ni, nj = ci + direction[k][0], cj + direction[k][1]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            solve(k, ni, nj, v + [arr[ni][nj]], cnt + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = []
    answer = -1
    for i in range(N):
        for j in range(N-1):
            si = i
            sj = j
            solve(0, si, sj, v, 0)
    print(f'#{tc} {answer}')
