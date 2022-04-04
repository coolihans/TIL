import sys
sys.stdin = open("input.txt")

T = int(input())


def battery(now, end):                      # 첫 자리 수부터 한 자리씩 오른쪽으로 가며 끝까지 탐색
    global lowest_battery

    if now == end:                                          # 끝까지 다 탐색을 했을 때
        case = [1] + nums + [1]                             # 사무실 넣고
        case_battery = 0
        for c in range(len(case)-1):
            case_battery += matrix[case[c]-1][case[c+1]-1]  # 관리구역 번호는 인덱스보다 1 크므로 -1
        if case_battery < lowest_battery:
            lowest_battery = case_battery

    else:
        for i in range(now, end):                           # 내가 있는 자리수부터 내 뒤의 자리수들을 고려
            nums[now], nums[i] = nums[i], nums[now]         # 나와 고려할 자리수를 바꾸고
            battery(now+1, end)                             # 다음 자리수로 전진
            nums[now], nums[i] = nums[i], nums[now]         # 나와 고려할 자리수를 다시 되돌려놓기

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    lowest_battery = float("inf")
    nums = [x for x in range(2, N+1)]

    battery(0, N-1)
    print(f"#{tc} {lowest_battery}")
