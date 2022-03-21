import sys
sys.stdin = open('input.txt')

def top_choice(bottom):
    top = 0
    if bottom == 0:
        top = 5
    elif bottom == 1:
        top = 3
    elif bottom == 2:
        top = 4
    elif bottom == 3:
        top = 1
    elif bottom == 4:
        top = 2
    elif bottom == 5:
        top = 0
    return top


def get_dice(start, floor):
    total = 0
    idx = 0
    bottom = start
    tmp_list = []

    while idx < T:
        top = top_choice(bottom)
        tmp_top = floor[idx][top]
        for i in range(6):
            if i != top and i != bottom:
                tmp_list.append(floor[idx][i])
        total += max(tmp_list)
        idx += 1
        if idx <= T-1:
            for j in range(6):
                if floor[idx][j] == tmp_top:
                    bottom = j
        else:
            return total
        tmp_list = []




T = int(input())
total = 0
floor = [list(map(int, input().split())) for _ in range(T)]
total_list = []
for i in range(6):
    total_list.append(get_dice(i, floor))
print(max(total_list))



