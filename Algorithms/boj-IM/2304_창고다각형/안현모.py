import sys
sys.stdin = open("input.txt")


N = int(input())
positions = []
heights = []
col_infos = []
for _ in range(N):
    L, H = list(map(int, input().split()))
    col_infos.append([L, H])
    positions.append(L)
    # heights.append(H)
# 가장 오른쪽 기둥의 L
rightL = 0
for i in positions:
    if rightL < i:
        rightL = i
# 가장 왼쪽 기둥의 L
# leftL = 1001
# for i in positions:
#     if leftL > i:
#         leftL = i
# 가장 긴 기둥의 idx
maxh = 0
for i in col_infos:
    if i[1] > maxh:
        maxh = i[1]
        maxh_idx = i[0]

# 빈곳은 0으로 채워진 새로운 col_info 필요
new_info = [0] * (rightL + 1)
for L, H in col_infos:
    new_info[L] = H
# 가장 긴 기둥 기준 왼쪽 면적 // 가운데 기둥 포함
left_area = 0
tmp_h = 0
for i in range(maxh_idx + 1):
    if tmp_h < new_info[i]:
        tmp_h = new_info[i]
    left_area += tmp_h

# 가장 긴 기둥 기준 오른쪽 면적 // 끝에서부터 //
right_area = 0
tmp_h2 = 0
for i in range(rightL, maxh_idx, -1):
    if tmp_h2 < new_info[i]:
        tmp_h2 = new_info[i]
    right_area += tmp_h2

total = left_area + right_area

print(total)
