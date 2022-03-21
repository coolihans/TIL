import sys
sys.stdin = open('input2.txt')


def make_storage(columns):
    max_height = my_max(columns, 0)
    area = 0
    width, height = columns[0][0], columns[0][1]

    for c in range(N):
        if height <= columns[c][1]:
            area += height * (columns[c][0] - width)
            width, height = columns[c][0], columns[c][1]
            if columns[c][1] == max_height:
                area += max_height
                if c == N-1:
                    return area
                n = c + 1
                height = my_max(columns, n)
                break

    for c in range(n, N):
        if c == N-1:
            area += height * (columns[c][0] - width)
        elif height == columns[c][1]:
            area += height * (columns[c][0] - width)
            width, height = columns[c][0], my_max(columns, c+1)

    return area


def my_sort(columns):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if columns[j][0] > columns[j + 1][0]:
                columns[j], columns[j + 1] = columns[j + 1], columns[j]


def my_max(columns, i):
    if N == 1:
        return columns[0][1]
    mmax = columns[i][1]
    for n in range(i, len(columns)):
        if columns[n][1] > mmax:
            mmax = columns[n][1]
    return mmax


N = int(input())
columns = [list(map(int, input().split())) for _ in range(N)]
my_sort(columns)
ans = make_storage(columns)
print(ans)
