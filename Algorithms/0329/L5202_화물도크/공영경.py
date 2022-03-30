import sys
sys.stdin = open('input.txt')


def solution(N):
    times = [list(map(int, input().split())) for _ in range(N)]

    # 종료시간을 기준으로 오름차순
    times.sort(key = lambda x: x[1])

    # 화물차의 개수, 가장 최근 화물차의 종료 시간
    car_count = 0
    last_time = 0

    for time in times:
        # 현재 화물차의 시작시간이 마지막 종료시간 보다 크거나 같다면
        if time[0] >= last_time:
            # 종료시간을 현재 화물차의 종료시간으로
            last_time = time[1]
            car_count += 1
    
    return car_count


T = int(input())

for tc in range(T):
    N = int(input())
    answer = solution(N)

    print(f'#{tc+1} {answer}')