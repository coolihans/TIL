import sys
sys.stdin = open('input.txt')


def merge_sort(m):
    if len(m) == 1:
        return m

    lst_left = m[0:len(m)//2]
    lst_right = m[len(m)//2:]

    lst_left = merge_sort(lst_left)
    lst_right = merge_sort(lst_right)

    return merge(lst_left, lst_right)


def merge(left, right):
    global cnt
    result = []
    left_idx = right_idx = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif left_idx < len(left):
            result.append(left[left_idx])
            left_idx += 1
        elif right_idx < len(right):
            result.append(right[right_idx])
            right_idx += 1
    return result

T = int(input())
for tc in range(1, T+1):
    L = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(lst)
    print(f'#{tc} {result[L//2]} {cnt}')