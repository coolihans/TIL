import sys
sys.stdin = open('input.txt')

def dfs(n, tmp):
    global answer
    if answer >= tmp:
        return
    # 50번 사람 까지 진행후 탈출
    if n == N:
        if answer <= tmp:
            answer = tmp
            return
    # j 는 일 번호
    for j in range(N):
        if not done_job[j]:
            done_job[j] = 1
            dfs(n+1, tmp*matrix[n][j])
            done_job[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    done_job = [0]*N
    answer = 0
    dfs(0, 1)
    print(f'#{tc} {answer*100 :6f}')

