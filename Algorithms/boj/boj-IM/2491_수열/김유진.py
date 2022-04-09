import sys
sys.stdin = open("input3.txt")

def get_increase(lst):
    max_count = 0
    count = 0
    i = 0
    while i <= len(lst) - 2:
        if lst[i + 1] >= lst[i]:
            count += 1
            i += 1
            if max_count < count:
                max_count = count
        else:
            lst = lst[i+1:]
            count = 0
            i = 0
    return max_count+1

def get_decrease(lst):
    max_count = 0
    count = 0
    i = 0
    while i <= len(lst)-2:
        if lst[i + 1] <= lst[i]:
            count += 1
            i += 1
            if max_count < count:
                max_count = count
        else:
            lst = lst[i + 1:]
            count = 0
            i = 0
    return max_count+1

N = int(input())
nums = list(map(int, input().split()))

result1 = get_increase(nums)
result2 = get_decrease(nums)

if result1 > result2:
    print(f'{result1}')
else:
    print(f'{result2}')