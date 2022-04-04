import sys
sys.stdin = open('input.txt')


def more_work_more(containers):                 # 종료시간 기준으로 오름차순 정렬된 화물차들
    cnt = 1                                     # 쥐어짜낼 화물차 수
    temp = containers[0]                        # 비교군
    for i in range(1, len(containers)):
        if containers[i][0] >= temp[1]:         # 앞 차 종료 시간보다 시작 시간이 같거나 큰 경우만, 
            cnt += 1                            # 쥐어짜낸다.
            temp = containers[i]                # 비교군 갱신

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    containers = [list(map(int, input().split())) for _ in range(N)]
    containers.sort(key=lambda x: (x[1], x[0]))
    ans = more_work_more(containers)
    print(f'#{tc} {ans}')