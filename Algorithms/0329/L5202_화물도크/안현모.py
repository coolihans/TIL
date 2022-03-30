import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se_lst = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간 기준 정렬
    se_lst = sorted(se_lst, key=lambda x: x[1])
    answer = 0
    end_time = 0
    for i in range(N):
        # 가장 빠른 종료 시간을 가진 s, e == 첫 번째
        s = se_lst[i][0]
        e = se_lst[i][1]
        # 다음 작업의 시작 시간 확인(앞의 작업의 끝나는 시간과 비교) and 종료 시간 제일 빠른 거 고르기(자동)
        if s >= end_time:
            answer += 1
            end_time = e
    print(f'#{tc} {answer}')
