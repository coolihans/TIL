import sys
sys.stdin = open('input.txt')


def func(now, visits, ssum):
    global answer

    # backtracking
    if ssum >= answer:
        return

    # 종료조건
    if not visits:
        # 마지막으로 사무실 복귀
        ssum += matrix[now][0]
        if ssum < answer:
            answer = ssum
        return

    # 다음 구역으로 이동/ 방문한 구역은 제외
    for i in range(len(visits)):
        next = visits[i]
        func(next, visits[:i] + visits[i+1:], ssum + matrix[now][next])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 1000
    # visits에 앞으로 방문할 구역들을 기록
    visits = list(range(1, N))
    func(0, visits, 0)

    print(f'#{tc}', answer)
