import sys
sys.stdin = open("input.txt")


def func(r, c, temp_sum):
    global min_sum

    if r == N-1 and c == N-1:
        temp_sum += matrix[r][c]
        if temp_sum < min_sum:
            min_sum = temp_sum
            return
    else:
        temp_sum += matrix[r][c]
        for i in range(2):
            new_r = r + dxs[i]
            new_c = c + dys[i]
            if new_r < N and new_c < N and temp_sum < min_sum:
                func(new_r, new_c, temp_sum)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dxs = [0, 1]
    dys = [1, 0]
    row, col = 0, 0
    min_sum = float("inf")
    func(row, col, 0)
    print(f"#{tc} {min_sum}")

