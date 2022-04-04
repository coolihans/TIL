import sys
sys.stdin = open('input.txt')


def quick_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    pivot = nums[0]
    left, right = [], []
    center = [pivot]
    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + center + quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(nums)[N//2]}')
