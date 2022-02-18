import sys
sys.stdin = open('input.txt')
# 사다리같이 뒤에서부터? 가장 뒤 -1 이 -2 보다 작으면 지나감... 그 다음 -2 가 -3 보다 작으면 또 지나감..
# -3 이 -4 보다 크면? 차이를 누적.하고 지나감... -3 이 -5 보다 또 크면? 또 누적하고 -3 기준 유지.
# -3 이 -6 보다 작음..그럼 이제 -6이 최대값으로 바뀜

# 앞에서부터
# 0 < 1 이면 지나감 1 < 2 지나감... 2 > 3 이면 흠..

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    all_list = list(map(int, input().split())) #바본가
    big_v = all_list[-1]
    total_profit = 0
    for i in range(N-1, -1, -1):   # N 첫번째 비교는 넘기고
        if all_list[i] >= big_v:    # 이때는 그냥 넘어가고 big_v도 다음 수로 넘어감
            big_v = all_list[i]
        elif all_list[i] < big_v:
            total_profit += big_v - all_list[i]     # 차이가 수익이므로 누적하고 그 다음에 넘어감 big_v는 유지

    print(f'#{tc} {total_profit}')

