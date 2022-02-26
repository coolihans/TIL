import sys
sys.stdin = open("input.txt")

K = int(input())
data = []
directions = []
lengths = []
for _ in range(6):
    D, L = map(int, input().split())
    data.append([D, L])
    directions.append(D)
    lengths.append(L)

# 어떤 모양인지 판별 = > 뭐가 두 번 나왔는 지 판별
cnt_lst = [0] * 5
for direction in directions:
    if direction == 1:
        cnt_lst[direction] += 1
    elif direction == 2:
        cnt_lst[direction] += 1
    elif direction == 3:
        cnt_lst[direction] += 1
    else:
        cnt_lst[direction] += 1

# 바깥 사각형 길이 두 개 / 작은 사각형 길이 두 개 구하기
big_lengths = []
small_lengths = []
# index? == 첫 번 째 것만 구해줌
# 313142 에서 3131 중에 '13' 부분의 값이 작은 상자 가로 세로 길이
# 따라서 한 번 나오는 큰 가로 세로 먼저 구하고 거기서 -3 자리씩 하면 구해짐
for i in range(1, 5):
    if cnt_lst[i] == 1:
        big_lengths.append(lengths[directions.index(i)])
        idx = directions.index(i) - 3
        if idx < 0:
            idx = directions.index(i) + 3
        small_lengths.append(lengths[idx])

total = big_lengths[0] * big_lengths[1] - small_lengths[0] * small_lengths[1]

print(K * total)
