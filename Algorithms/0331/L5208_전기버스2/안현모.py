import sys
sys.stdin = open('input.txt')


def dfs(n, cnt):
    global answer
    # 가지 치기
    if cnt >= answer:
        return
    # 탈출 조건
    if n >= N:
        if cnt < answer:
            answer = cnt
        return

    left_battery = battery_charge[n]    # 더하는 게 아니라 다른걸 로 교체

    # 갈아낀 배터리로 갈 수 있는 경우를 모두 가보기..
    for i in range(left_battery, 0, -1):
        dfs(n+i, cnt+1)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0] - 1
    battery_charge = arr[1:]
    answer = 123123
    dfs(0, -1)
    print(f'#{tc} {answer}')
