import sys
sys.stdin = open('input.txt')


def across_remove(list, temp_idx):  # 주사위 전개도 리스트, 주사위 밑면or윗면 인덱스
    if temp_idx == 0 or temp_idx == 5:
        new_list = list[1:5]
        return new_list
    elif temp_idx == 1 or temp_idx == 3:
        new_list = list[0] + list[2] + list[4] + list[5]
        return new_list
    elif temp_idx == 2 or temp_idx == 4:
        new_list = list[0] + list[1] + list[3] + list[5]
        return new_list


def across_idx_search(under_num_idx):  # 반대편 인덱스 리턴
    if under_num_idx == 0:
        return 5
    elif under_num_idx == 1:
        return 3
    elif under_num_idx == 2:
        return 4
    elif under_num_idx == 3:
        return 1
    elif under_num_idx == 4:
        return 2
    elif under_num_idx == 5:
        return 0


T = int(input())

temp_start_idx = 0
temp_end_idx = 0
cnt = 0
a = 0

for tc in range(1, T+1):
    dice_list = list(map(int, input().split()))

    if cnt == 0:
        a = dice_list[across_idx_search(temp_start_idx)]

    else:
        idx = dice_list.index(a)
        b = dice_list[across_idx_search(temp_start_idx)]
    print(dice_list, a)
# a = 0
# tmp_max_list = []
# tmp_idx = -1

# for _ in range(0, 6):
#     tmp_under_idx = _
#     for tc in range(1, T+1):
#         dice_num_list = list(map(int, input().split()))
#         print(dice_num_list)
#         if tmp_idx == -1:
#             a = next_under_num_search(dice_num_list, tmp_under_idx)  # 4 리턴.
#             tmp_max_list.append(max(across_remove(dice_num_list, tmp_under_idx)))  # 밑면과 맞은편 숫자 제외한 숫자 리스트 중 최대값
#             tmp_idx = dice_num_list.index(a)
#         else:
#             a = next_under_num_search(dice_num_list, tmp_idx)
#             tmp_max_list.append(max(across_remove(dice_num_list, tmp_idx)))
#             tmp_idx = dice_num_list.index(a)
#
#         print(dice_num_list, across_remove(dice_num_list, tmp_under_idx), a, tmp_idx)
#         print(sum(tmp_max_list))
#
#     tmp_max_list = []
#     tmp_idx = -1
