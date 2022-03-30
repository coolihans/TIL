import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]

    times = []                                      # 시간을 측정해서
    for idx, truck in enumerate(trucks):
        times.append([truck[1]-truck[0], idx])
    times.sort()                                    # 시간이 가장 적게 걸리는 도크부터 사용

    count = 0
    check = [0] * 24

    for time in times:
        truck_idx = time[1]
        already = False
        for i in range(time[0]):
            if check[trucks[truck_idx][0]+i] != 0:  # 해당 시간동안 누군가 썼다면
                already = True
        if not already:                             # 아무도 쓰지 않았으면
            count += 1                              # 도크 수 갱신
            for i in range(time[0]):
                check[trucks[truck_idx][0] + i] = 1 # 사용 처리

    print(f"#{tc} {count}")


