import sys

sys.stdin = open("input.txt")


def get_guard_loc(r):
    for i in range(N):
        for j in range(N):
            if r[i][j] == 2:
                return i, j


def change_room(r, i, j):
    for d in range(4):  # 4방향 순서대로
        for k in range(1, N):  # 보이는만큼 바꾸기
            new_i = i + di[d] * k
            new_j = j + dj[d] * k
            if 0 <= new_i < N and 0 <= new_j < N:  # room 을 벗어나지 않을 경우.
                if r[new_i][new_j] == 1:  # 벽을 만나면 == 1을 만나면 그 방향은 break 하고 다음 방향으로 넘어감.
                    break
                r[new_i][new_j] = -1


def solve(r):
    result = 0
    for i in range(N):
        for j in range(N):
            if r[i][j] == 0:
                result += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    # 경비원 위치 찾기
    guard_i, guard_j = get_guard_loc(room)
    # 상하좌우 방향
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 보이는 곳 3으로 바꾸기. (아무 딴 수)
    change_room(room, guard_i, guard_j)
    # 0 인 곳 카운트 후 프린트

    print(f'#{tc} {solve(room)}')