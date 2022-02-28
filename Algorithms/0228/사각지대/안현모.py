import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    # 경비원 위치 찾기
    for i in range(N):
        for j in range(N):
            if room[i][j] == 2:
                guard_i = i
                guard_j = j
            else:
                continue

    # 상하좌우 방향
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 보이는 곳 3으로 바꾸기. (아무 딴 수)
    for d in range(4):      # 4방향 순서대로
        for k in range(1, N):   # 보이는만큼 바꾸기
            new_i = guard_i + di[d] * k
            new_j = guard_j + dj[d] * k
            if 0 <= new_i < N and 0 <= new_j < N:       # room 을 벗어나지 않을 경우.
                if room[new_i][new_j] == 1:             # 벽을 만나면 == 1을 만나면 그 방향은 break 하고 다음 방향으로 넘어감.
                    break
                room[new_i][new_j] = -1

    result = 0
    for i in range(N):
        for j in range(N):
            if room[i][j] == 0:
                result += 1

    print(f'#{tc} {result}')

