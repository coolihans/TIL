import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    # 일이 끝나는 시간을 기준으로 정렬
    works.sort(key=lambda x: x[1])

    last_work = [0, 0]
    cnt = 0
    # 작업 시간이 겹치지 않는 경우를 선택/ 선택할 때마다 작업 횟수 += 1
    for work in works:
        if work[0] >= last_work[1]:
            last_work = work
            cnt += 1
    print(f'#{tc}', cnt)
