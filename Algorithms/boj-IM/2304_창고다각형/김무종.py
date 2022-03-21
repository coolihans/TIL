import sys
sys.stdin = open('input.txt')

def get_right(right, max_idx_x):
    global total
    right_height = [right[i][1] for i in range(len(right))]
    max_right_idx = my_max(right_height)
    right_width = right[max_right_idx][0] + 1
    right_height = right[max_right_idx][1]
    total += (right_width-max_idx_x) * right_height
    if max_right_idx >= len(right)-1:
        return
    else:
        return get_right(right[max_right_idx+1:], right_width)

def my_max(list_a):
    max_a = list_a[0]
    max_aidx = 0
    for idx, val in enumerate(list_a):
        if max_a < val:
            max_a = val
            max_aidx = idx
    return max_aidx

def get_left(left):
    global total
    tmp = left[0][1]
    tmp_x = left[0][0]
    if len(left) > 1:
        for i in range(len(left)):
            if tmp < left[i][1]:
                total += (left[i][0] - tmp_x) * tmp
                tmp = left[i][1]
                tmp_x = left[i][0]
            if i == len(left) - 1:
                total += (buildings[max_idx][0] - tmp_x) * tmp
    else:
        total += (buildings[max_idx][0] - tmp_x) * tmp
    return

N = int(input())
buildings = []
for i in range(N):
    buildings.append(list(map(int, input().split())))
buildings = sorted(buildings)
height = [buildings[i][1] for i in range(len(buildings))]
max_idx = my_max(height)

if len(buildings) > 1:
    if 0 < max_idx < len(buildings)-1:
        left = buildings[:max_idx]
        right = buildings[max_idx+1:]

    elif max_idx == 0:
        left = []
        right = buildings[max_idx+1:]

    elif max_idx == len(buildings)-1:
        left = buildings[:max_idx]
        right = []

    total = 0

    if left:
        get_left(left)
        if right:
            get_right(right, buildings[max_idx][0] + 1)
        print(total + buildings[max_idx][1])
    else:
        get_right(right, buildings[max_idx][0] + 1)
        print(total + buildings[max_idx][1])


else:
    print(buildings[i][1])