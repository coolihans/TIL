import sys
sys.stdin = open('input.txt')


def max_tasks():
    selected = [docks[0]]                   # 작업 순서
    for i in range(1, len(docks)):
        if docks[i][0] >= selected[-1][1]:   # 다음 작업시작시간이 앞 작업종료시간보다 크거나 같을 때
            selected.append(docks[i])

    return len(selected)    # 작업 순서의 개수를 반환


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    docks = [list(map(int, input().split())) for _ in range(N)]
    docks.sort(key=lambda x: x[1])      # 종료시간 오름차순으로 정렬
    print(f'#{tc} {max_tasks()}')
